# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel). Schema é uma estrutura que organiza e deifine regras para dados
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    category_name: str
    is_anchor: bool = False
    user_id: int

class CategoryResponse(CategoryCreate):
    id: int