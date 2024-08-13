from pydantic import BaseModel, Field

class ADDRESS_CODES(BaseModel):
    c_addr_id: int = Field(..., ge=0)  # 地址ID
    c_name: str = Field(..., min_length=1)  # 地址拼音名称
    c_name_zh: str = Field(None)  # 地址简体名称
    c_name_chn: str = Field(..., min_length=1)  # 地址繁体名称
    c_firstyear: int = Field(..., ge=0)  # 首次创立时间
    c_lastyear: int = Field(..., ge=0)  # 最近更新时间
    c_admin_type: str = Field(..., min_length=1)  # 至少有一个字符的字符串
    x_coord: float = Field(None)  # 经度
    y_coord: float = Field(None)  # 维度
    CHGIS_PT_ID: int = Field(None, ge=0)  # 可以为 None 的大于 0 的整数
    c_notes: str = Field(None)  # 地址有关记录文献繁体
    c_notes_zh: str = Field(None)  # 地址有关记录文献简体
    c_alt_names: str = Field(None)  # 地址别名繁体
    c_alt_names_zh: str = Field(None)  # 地址别名简体
