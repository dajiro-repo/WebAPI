from pydantic import BaseModel

class TanukiIn(BaseModel):
    id: int
    name: str
    age: int
    type: str
