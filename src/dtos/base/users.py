from pydantic import BaseModel

class UsersBase(BaseModel):
    fullname: str | None
    age: int | None
    email: str | None
    location: str | None