from fastapi import APIRouter, HTTPException
from app.models import HealthMetric
from app.crud import create_health_metric, get_health_metrics
from app.database import health_container

router = APIRouter()

@router.post("/", response_model=HealthMetric)
def add_health_metric(health_metric: HealthMetric):
    try:
        return create_health_metric(health_metric)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving health metric: {str(e)}")

@router.get("/", response_model=list[HealthMetric])
def get_health_metric_list():
    return get_health_metrics()

