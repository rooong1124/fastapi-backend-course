from fastapi import FastAPI
from .database import Base, engine
from .routers import router
from .auth import router as auth_router

# Initialize Fastapi
app = FastAPI()

#Initialize Database's Table
Base.metadata.create_all(bind=engine)

# Resigter Router
app.include_router(router=router, prefix="/api", tags=["todos"])
app.include_router(auth_router)