from fastapi import APIRouter, HTTPException
from app.models import User
from app.crud import create_user, get_users
from app.database import users_container, health_container, activities_container

router = APIRouter()

@router.post("/", response_model=User)
def add_user(user: User):
    try:
        return create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving user: {str(e)}")

@router.get("/", response_model=list[User])
def get_user_list():
    return get_users()

@router.get("/{user_id}")
def get_user_with_data(user_id: str):
    try:
        # Pobieranie użytkownika
        user_query = list(users_container.query_items(
            query="SELECT * FROM Users u WHERE u.id=@user_id",
            parameters=[{"name": "@user_id", "value": user_id}],
            enable_cross_partition_query=True
        ))

        if not user_query:
            raise HTTPException(status_code=404, detail="User not found")

        user = user_query[0]  # Pobieramy pierwszy wynik

        # Pobieranie powiązanych danych zdrowotnych
        health_query = list(health_container.query_items(
            query="SELECT * FROM HealthMetrics h WHERE h.user_id=@user_id",
            parameters=[{"name": "@user_id", "value": user_id}],
            enable_cross_partition_query=True
        ))

        # Pobieranie powiązanych aktywności
        activities_query = list(activities_container.query_items(
            query="SELECT * FROM Activities a WHERE a.user_id=@user_id",
            parameters=[{"name": "@user_id", "value": user_id}],
            enable_cross_partition_query=True
        ))

        return {
            "user": user,
            "health_metrics": health_query,
            "activities": activities_query
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching user data: {str(e)}")