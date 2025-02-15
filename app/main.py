from fastapi import FastAPI
from app.routes import users, health, activities

app = FastAPI(title="CloudHealth API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(activities.router, prefix="/activities", tags=["Activities"])

@app.get("/")
def root():
    return {"message": "CloudHealth API is running"}