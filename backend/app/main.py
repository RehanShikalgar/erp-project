from fastapi import FastAPI

app = FastAPI(title="Invoice ERP")

@app.get("/")
def root():
    return {"message" : "Invoice ERP is running"}