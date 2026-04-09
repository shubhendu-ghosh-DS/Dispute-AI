from fastapi import FastAPI
from api.endpoints.auth import router as auth_router


# Initialize fastapi app
app = FastAPI()

# Include router 
app.include_router(auth_router)
