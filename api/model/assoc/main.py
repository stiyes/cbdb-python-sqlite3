
from pydantic import BaseModel, Field, validator
from typing import Optional, List

class ASSOC_DATA(BaseModel):
  tts_sysno: Optional[int] = Field(None,ge=0)  # 记录的序号
  c_assoc_code: Optional[int] = Field(None,ge=0)  # 社会关系编码
  c_personid: Optional[int] = Field(None,ge=0, printable=True)  # 人物ID
  c_kin_code: Optional[int] = Field(None,ge=0)  # 亲属关系编码
  c_kin_id: Optional[int] = Field(None,ge=0)  # 亲属关系ID
  c_assoc_id: Optional[int] = Field(None,ge=0)  # 社会关系ID
  c_assoc_kin_code: Optional[int] = Field(None,ge=0)  # 
  c_assoc_kin_id: Optional[int] = Field(None,ge=0)  # 
  c_tertiary_personid: Optional[int] = Field(None,ge=0)  # 社会关系ID
  c_tertiary_type_notes: Optional[str] = Field(None)  # 
  c_assoc_count: Optional[int] = Field(None,ge=0)  # 
  c_sequence: Optional[int] = Field(None,ge=0)  # 
  c_assoc_year: Optional[int] = Field(None,ge=0)  # 
  c_source: Optional[int] = Field(None,ge=0)  # 记录的来源，一般是c_textid
  c_pages: str = Field(None)  # 记录来源的具体页面编码
  c_secondary_source_author: str = Field(None)  # 
  c_notes:  str = Field(None) # 记录的文案备注
  c_assoc_nh_code: int = Field(None) # 记录的文案备注
  c_assoc_nh_year: int = Field(None) # 记录的文案备注
  c_assoc_range: int = Field(None) # 记录的文案备注
  c_addr_id: int = Field(None) # 记录的文案备注
  c_litgenre_code: int = Field(None) # 记录的文案备注
  c_occasion_code: int = Field(None) # 记录的文案备注
  c_topic_code: int = Field(None) # 记录的文案备注
  c_inst_code: int = Field(None) # 记录的文案备注
  c_inst_name_code: int = Field(None) # 记录的文案备注
  c_text_title: str = Field(None) # 记录的文案备注
  c_assoc_claimer_id: int = Field(None) # 记录的文案备注
  c_assoc_intercalary: bool = Field(None, description="")
  c_assoc_month: int = Field(None) # 记录的文案备注
  c_assoc_day: int = Field(None) # 记录的文案备注
  c_assoc_day_gz: int = Field(None) # 记录的文案备注
  c_assoc_month: int = Field(None) # 记录的文案备注
  c_created_by: str = Field(None)  # 创建者
  c_created_date: str = Field(None)  # 创建日期
  c_modified_by: str = Field(None)  # 修改者
  c_modified_date: str = Field(None)  # 更新日期

  @validator('c_personid')
  def check_c_personid(cls, v):
    if not isinstance(v, int):
        raise ValueError('c_personid must be an integer')
    return v

  class Config:
    orm_mode = True


