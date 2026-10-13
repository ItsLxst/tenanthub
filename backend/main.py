from fastapi import FastAPI
from auth.routes import router as auth_router
from organizations.routes import router as org_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(org_router, prefix="/organizations")

@app.get("/")
def read_root():
    return {"status": "ok"}