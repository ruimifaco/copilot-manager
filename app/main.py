from fastapi import FastAPI
from app.db.connection import engine
from sqlalchemy import text
from app.api.categories import router as categories_router
from app.api.tasks import router as tasks_router
from app.api.recurringBlocks import router as recurring_router

app = FastAPI(title="Co-piloto API")
app.include_router(categories_router)
app.include_router(tasks_router)
app.include_router(recurring_router)

@app.get("/")
def root():
    return {"message": "Co-piloto API is running"}

@app.get("/health/db")
def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
    return {"status": "conexão feita com sucesso", "valor": result}
