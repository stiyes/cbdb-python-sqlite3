import sqlite3
import zhconv
from tqdm import tqdm

# 定义一个函数，将繁体中文转换为简体中文
def converter(str):
    new_str = ''
    if(str is not None):
        new_str = zhconv.convert(str, 'zh-hans')
    return new_str

# 连接到 SQLite 数据库
db_path = './latest.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# 我们要转换的表是 'table_name'，字段列表是 'source_columns'
# 1. ADDR_BELONGS_DATA
# table_name = 'ADDR_BELONGS_DATA'
# c_id = 'c_addr_id'
# source_columns = ['c_notes']

# 2. ADDRESSES
# table_name = 'ADDRESSES'
# c_id = 'c_addr_id'
# source_columns = ['c_name_chn','belongs1_Name', 'belongs2_Name', 'belongs3_Name','belongs4_Name','belongs5_Name']

# 3. ALTNAME_DATA
# table_name = 'ALTNAME_DATA'
# c_id = 'c_personid'
# source_columns = ['c_alt_name_chn','c_notes']


# 5. APPOINTMENT_TYPE_CODES
# table_name = 'APPOINTMENT_TYPE_CODES'
# c_id = 'c_appt_type_code'
# source_columns = ['c_appt_type_desc_chn', 'c_appt_type_desc_chn_alt']

# 6. ASSOC_CODES
table_name = 'ASSOC_CODES'
c_id = 'c_assoc_code'
source_columns = ['c_assoc_desc_chn', 'c_example']

# 6. ASSOC_TYPES
table_name = 'ASSOC_TYPES'
c_id = 'c_assoc_type_id'
source_columns = ['c_assoc_type_desc_chn']

# 7. ASSUME_OFFICE_CODES
table_name = 'ASSUME_OFFICE_CODES'
c_id = 'c_assume_office_code'
source_columns = ['c_assume_office_desc_chn']

# 8. BIOG_ADDR_CODES
table_name = 'BIOG_ADDR_CODES'
c_id = 'c_addr_type'
source_columns = ['c_addr_desc_chn']


# 9. BIOG_INST_CODES
table_name = 'BIOG_INST_CODES'
c_id = 'c_bi_role_code'
source_columns = ['c_bi_role_chn','c_notes']

# 9. BIOG_INST_DATA
table_name = 'BIOG_INST_DATA'
c_id = 'c_personid'
source_columns = ['c_notes']

# 10. BIOG_MAIN
table_name = 'BIOG_MAIN'
c_id = 'c_personid'
source_columns = ['c_name_chn', 'c_notes', 'c_fl_ey_notes', 'c_fl_ly_notes', 'c_surname_chn', 'c_mingzi_chn']

# 11. BIOG_SOURCE_DATA 
table_name = 'BIOG_SOURCE_DATA'
c_id = 'tts_sysno'
source_columns = ['c_notes']

# 9. BIOG_ADDR_DATA
table_name = 'BIOG_ADDR_DATA'
c_id = 'tts_sysno'
source_columns = ['c_notes']

# 12. BIOG_TEXT_DATA
table_name = 'BIOG_TEXT_DATA'
c_id = 'tts_sysno_1'
source_columns = ['c_notes']

# 13. CBDB_NAME_LIST
table_name = 'CBDB_NAME_LIST'
c_id = 'tts_sysno'
source_columns = ['name']

table_name = 'YEAR_RANGE_CODES'
c_id = 'c_range_code'
source_columns = ['c_range_chn','c_approx_chn']

table_name = 'TEXT_INSTANCE_DATA'
c_id = 'tts_sysno1'
source_columns = ['c_counter','c_print','c_publisher']



# 限制条件测试数据
# demo_str = f'WHERE {c_id}=4383'
demo_str = None


# 一. 查询所有需要转换的记录
cursor.execute(f'SELECT {", ".join(source_columns)},{c_id} FROM {table_name} {demo_str}')
rows = cursor.fetchall()


# 二、为每个新列执行 ALTER TABLE 语句
# 2.1 查看表结构
cursor.execute(f"PRAGMA table_info({table_name})")
table_infos = cursor.fetchall()
table_columns = [column[1] for column in table_infos]
for column in source_columns:
    # 检查列是否已存在
    if column+'_zh' not in table_columns:
        alter_table_statement = f"ALTER TABLE {table_name} ADD COLUMN {column}_zh TEXT"
        cursor.execute(alter_table_statement)

# 创建一个tqdm进度条对象
pbar = tqdm(total=len(rows), desc="所有需要转换的记录，正在转换....")

# 三、遍历记录并转换字段
for row in rows:
    # 获取原始值,并转换为简体中文
    data = dict(zip(source_columns, row))
    source_values = [converter(item) if isinstance(item, str) else item for item in row]
    # 更新数据库记录
    set_clause = ', '.join([f"{column}_zh = ?" for column in source_columns])

    update_expressions = []
    for column in source_columns:
        if column in data and data[column]:
            value = data[column]
            if isinstance(value, str):
                value = "'" + value.replace("'", "''") + "'"
            else:
                value = str(value)
            update_expressions.append(f"{column} = {value}")

    update_where= 'AND '.join(update_expressions)
    if(len(update_expressions) > 0):
        update_where = 'AND ' + update_where

    sql = f"UPDATE {table_name} SET {set_clause} WHERE {c_id} = ? " + update_where
    # print('update_where ===> ',update_expressions, sql)
    cursor.execute(sql, tuple(source_values))
    # 更新进度条
    pbar.update(1)

# 提交事务
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
# 关闭进度条
pbar.close()

print('Data converted and updated in the database.')