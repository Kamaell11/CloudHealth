from fastapi import APIRouter, HTTPException
from app.models import Activity
from app.crud import create_activity, get_activities
from app.database import activities_container

router = APIRouter()

@router.post("/", response_model=Activity)
def add_activity(activity: Activity):
    try:
        return create_activity(activity)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving activity: {str(e)}")

@router.get("/", response_model=list[Activity])
def get_activity_list():
    return get_activities()

