
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from api.model.assoc.main import ASSOC_DATA

class BIOG_MAIN(BaseModel):
  tts_sysno: Optional[int] = Field(None,ge=0)  # 可以为 None 或大于 0 的整数
  c_personid: Optional[int] = Field(None,ge=0)  # 可以为 None 或大于 0 的整数
  c_name: Optional[str] = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_name_chn: Optional[str] = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_name_chn_zh: Optional[str] = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_index_year: Optional[int] = Field(None,ge=0)
  c_index_year_type_code: Optional[str] = None  # 可以为 None 或至少有一个字符的字符串
  c_index_year_source_id: Optional[int] = Field(None,ge=0)
  c_female: Optional[bool] = Field(None, description="")
  c_index_addr_id: int = Field(None,ge=0)
  c_index_addr_type_code: int = Field(None,ge=0)
  c_ethnicity_code: int = Field(None,ge=0)
  c_household_status_code: int = Field(None,ge=0)
  c_tribe: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_birthyear: int = Field(None,ge=0)
  c_by_nh_code: int = Field(None,ge=0)
  c_by_nh_year: int = Field(None,ge=0)
  c_by_range: int = Field(None,ge=0)
  c_deathyear: int = Field(None,ge=0)
  c_dy_nh_code: int = Field(None,ge=0)
  c_dy_nh_year: int = Field(None,ge=0)
  c_dy_range: int = Field(None,ge=0)
  c_death_age: int = Field(None,ge=0)
  c_death_age_range: int = Field(None,ge=0)
  c_fl_earliest_year: int = Field(None,ge=0)
  c_fl_ey_nh_code: int = Field(None,ge=0)
  c_fl_ey_nh_year: int = Field(None,ge=0)
  c_fl_ey_notes:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_fl_ey_notes_zh:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_fl_latest_year: int = Field(None,ge=0)
  c_fl_ly_nh_code: int = Field(None,ge=0)
  c_fl_ly_nh_year: int = Field(None,ge=0)
  c_fl_ly_notes:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_fl_ly_notes_zh:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_surname: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_surname_chn: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_surname_chn_zh: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_mingzi: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_mingzi_chn: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_mingzi_chn_zh: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_dy: int = Field(None,ge=0)
  c_choronym_code: int = Field(None,ge=0)
  c_notes:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_notes_zh:str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_by_intercalary: bool = Field(None, description="")
  c_dy_intercalary: bool= Field(None, description="")
  c_by_month: int = Field(None,ge=0)
  c_dy_month: int = Field(None,ge=0)
  c_by_day: int = Field(None,ge=0)
  c_dy_day: int = Field(None,ge=0)
  c_by_day_gz: int = Field(None,ge=0)
  c_dy_day_gz: int = Field(None,ge=0)
  c_surname_proper: str= Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_mingzi_proper: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_name_proper: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_surname_rm: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_mingzi_rm: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_name_rm: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_created_by: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_created_date: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_modified_by: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_modified_date: str = Field(None)  # 可以为 None 或至少有一个字符的字符串
  c_self_bio: bool = Field(None, description="")


  @validator('c_personid')
  def check_c_personid(cls, v):
    if not isinstance(v, int):
        raise ValueError('c_personid must be an integer')
    return v

  # class Config:
  #   orm_mode = True

class BIOG_MAIN_DETAIL (BaseModel):
  person: BIOG_MAIN
  assocList: List[ASSOC_DATA] = []
    

