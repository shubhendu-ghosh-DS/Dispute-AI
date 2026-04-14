from fastapi import FastAPI
from api.endpoints.auth import router as auth_router
from api.endpoints.complaints import router as complaint_router


# Initialize fastapi app
app = FastAPI()

# Include router 
app.include_router(auth_router)
app.include_router(complaint_router)
