# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel). Schema é uma estrutura que organiza e deifine regras para dados
from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    category_name: str = Field(min_length=2, max_length=25)
    is_anchor: bool = False
    user_id: int = Field(gt=0) # gt significa greater than, ou seja, maior que 0. Isso é pra garantir que o id do usuário seja positivo

class CategoryResponse(CategoryCreate):
    id: int = Field(gt=0) # gt significa greater than, ou seja, maior que 0. Isso é pra garantir que o id da categoria seja positivo