import uuid
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    password_hash: str = Field(...)

    class ConfigDict:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "username": "foo",
                "password_hash": "foobarbaz_id"
            }
        }

