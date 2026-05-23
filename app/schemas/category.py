# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel).
from pydantic import BaseModel

class CategoryCreate(BaseModel):
    category_name: str
    is_anchor: bool = False
    user_id: int
