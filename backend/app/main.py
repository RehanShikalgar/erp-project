from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.config import settings
from app.routes import auth


app = FastAPI(title="Invoice ERP")

app.add_middleware(
    SessionMiddleware,
    secret_key =settings.secret_key,
    max_age = 60 * 60 * 24 * 7,
    same_site = "lax",
    https_only = False
)

app.include_router(auth.router)
@app.get("/")
def root():
    return {"message" : "Invoice ERP is running"}