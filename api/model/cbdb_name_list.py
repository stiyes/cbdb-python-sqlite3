from pydantic import BaseModel, Field, validator
from typing import Optional, List

class CBDB_NAME_LIST(BaseModel):
    index: int
    c_personid: Optional[int] = Field(None, gt=0)  # 可以为 None 或大于 0 的整数
    name: str
    source: Optional[str] = Field(None, min_length=1)  # 可以为 None 或至少有一个字符的字符串

    @validator('c_personid')
    def check_c_personid(cls, v):
        if not isinstance(v, int):
            raise ValueError('c_personid must be an integer')
        return v

    class Config:
        orm_mode = True
    def __init__(self, *, name=str):
        print(self, name)

