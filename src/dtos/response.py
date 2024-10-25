from pydantic import BaseModel
from typing import List

class Response[T](BaseModel):
    message: str
    data: List[T]