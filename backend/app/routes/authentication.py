from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/test/")
def read_root():
    return {"HelloWorld!!": "testing route!"}