from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    category_name: str = Field(min_length=2, max_length=25)
    is_anchor: bool = False
    user_id: int = Field(gt=0)

class CategoryResponse(CategoryCreate):
    id: int = Field(gt=0)
