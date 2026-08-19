from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Base, engine

# Import database models
from app.database.models import (
    StudentDB,
    SubjectDB,
    TimetableDB,
    StudentProfileDB
)
from app.database.user_model import UserDB

# Create all database tables
Base.metadata.create_all(bind=engine)

# Import routes
from app.routes import planner
from app.routes import dashboard
from app.routes import auth
from app.routes import roles
from app.routes import profile
from app.routes import recommendation
from app.routes import analytics
from app.routes import insights
from app.routes import attendance

from app.exceptions.base_exception import BusinessException
from app.middleware.exception_handler import (
    business_exception_handler
)

app = FastAPI(
    title="MentorAI API",
    version="1.0"
)

# ==========================================
# CORS Middleware
# ==========================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Exception Handler
app.add_exception_handler(
    BusinessException,
    business_exception_handler
)

# Register Routers
app.include_router(planner.router)
app.include_router(dashboard.router)
app.include_router(auth.router)
app.include_router(roles.router)
app.include_router(profile.router)
app.include_router(recommendation.router)
app.include_router(analytics.router)
app.include_router(insights.router)
app.include_router(attendance.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to MentorAI API"
    }