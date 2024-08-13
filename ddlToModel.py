ddl = """
CREATE TABLE ADDR_CODES(
  c_addr_id INTEGER, 
  c_name CHAR(255), 
  c_name_chn CHAR(255), 
  c_firstyear INTEGER, 
  c_lastyear INTEGER, 
  c_admin_type CHAR(255), 
  x_coord FLOAT, 
  y_coord FLOAT, 
  CHGIS_PT_ID INTEGER, 
  c_notes CHAR, 
  c_alt_names CHAR(255)
);
"""

# 假设我们使用正则表达式来解析字段定义
import re

# 正则表达式匹配字段定义
field_pattern = re.compile(r'(\w+) (\w+)(\(.*?\))?( NOT NULL)?( UNIQUE)?( PRIMARY KEY)?( DEFAULT .+)?')

# 解析字段定义
fields = field_pattern.findall(ddl.replace('\n', ' '))

# 打印转换后的 Pydantic 模型
print("class ADDR_CODES(BaseModel):")
for field in fields:
    field_name, field_type, _, not_null, unique, primary_key, default = field
    field_type = field_type.upper()
    annotation = 'str' if field_type == 'TEXT' else 'int' if field_type == 'INTEGER' else 'bool' if field_type == 'BOOLEAN' else 'Any'
    default_value = 'default=True' if default else ''
    not_null_str = 'required=True' if not_null else ''
    print(f"    {field_name}: {annotation} = Field(..., {not_null_str}, {default_value})")

print("\n    class Config:")
print("        orm_mode = True")
