from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router

app = FastAPI(
    title="file-api-app",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.openapi = OpenApiDocumentation(app).custom_openapi  # type: ignore



app.include_router(api_router, prefix="/api")
