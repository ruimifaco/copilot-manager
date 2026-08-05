from app.schemas.category import CategoryResponse # Importa classe do schema de saída
from app.schemas.category import CategoryCreate # Chama classe que herda de BaseModel
from fastapi import APIRouter # Importa APIRouter (que serve pra expandir rota do main.py, porque app mora exclusivamente no main.py)
from app.repositories.category_data import get_all_categories, insert_category_db
from app.repositories.category_data import get_category_by_id
from fastapi import HTTPException
from fastapi import status



router = APIRouter()

@router.get("/categories", response_model=list[CategoryResponse]) # responsável por solicitar dados de uma categoria
def list_categories():
    return get_all_categories()

@router.get("/categories/{id}", response_model=CategoryResponse)
def list_category_id(id: int):
    category_searched = get_category_by_id(id)
    if category_searched is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return category_searched

@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED) # responsável por inserir dados de uma categoria
def insert_category(category: CategoryCreate): # Aqui tá a classe que fica em schemas

    user_category_data = {
        "category_name": category.category_name,
        "is_anchor": category.is_anchor,
        "user_id": category.user_id
    }

    insert_user_category = insert_category_db(user_category_data) # Chama função que tá em repositories/category_data.py
    return insert_user_category # Retorna o que foi inserido no banco de dados, que é o que tá em schemas/category.py