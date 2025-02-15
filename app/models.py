from pydantic import BaseModel, EmailStr
import uuid

class User(BaseModel):
    id: str = str(uuid.uuid4())  # Generates an automatic ID (default_factory)
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    

    class Config:
        # Make sure the UUID is converted into a string when serialized
        json_encoders = {
            uuid.UUID: str
        }

class HealthMetric(BaseModel):
    id: str = str(uuid.uuid4())
    user_id: str
    date: str
    heart_rate: int
    blood_pressure: str
    glucose_level: float

class Activity(BaseModel):
    id: str = str(uuid.uuid4())
    user_id: str
    date: str
    steps: int
    calories_burned: float
