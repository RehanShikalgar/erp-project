from fastapi import FastAPI

from app.routes import auth


app = FastAPI(title="Invoice ERP")

app.include_router(auth.router)
@app.get("/")
def root():
    return {"message" : "Invoice ERP is running"}