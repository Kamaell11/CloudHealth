from app.models import User, HealthMetric, Activity
from app.database import users_container, health_container, activities_container
import uuid

# User CRUD operations
def create_user(user: User):
    user.id = str(uuid.uuid4())  # Generate a unique ID
    users_container.create_item(user.dict())  # Save to Cosmos DB
    return user

def get_users():
    return list(users_container.read_all_items())

# Health Metric CRUD operations
def create_health_metric(health_metric: HealthMetric):
    health_container.create_item(health_metric.dict())
    return health_metric

def get_health_metrics():
    return list(health_container.read_all_items())

# Activity CRUD operations
def create_activity(activity: Activity):
    activities_container.create_item(activity.dict())
    return activity

def get_activities():
    return list(activities_container.read_all_items())
