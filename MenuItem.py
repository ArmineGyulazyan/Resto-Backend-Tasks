import pydantic

class Pizza(pydantic.BaseModel):
        name:str
        description:str
        price:float

