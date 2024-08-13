from typing import Optional, List

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from api.model.generic import GenericMessage, GenericExceptionMessage
from api.model.biog.main import BIOG_MAIN, BIOG_MAIN_DETAIL
from api.model.assoc.main import ASSOC_DATA
from api.utils import db
from api.utils.db import DB_FILE
from api.utils.login import validate_access_token

router = APIRouter()
BIOG_TABLE_NAME = 'BIOG_MAIN'
ASSOC_DATA_TABLE_NAME = 'ASSOC_DATA'


@router.get("", responses={status.HTTP_200_OK: {"model": List[BIOG_MAIN]}})
def list_biog(c_personid: Optional[int] = None, c_name_chn: Optional[str] = None):
    fields = {}
    if c_personid:
        fields['c_personid'] = c_personid
    if c_name_chn:
        fields['c_name_chn'] = c_name_chn
    print(BIOG_MAIN.__fields__.keys())
    biog_list = db.query_db_many(db_file=DB_FILE, table=BIOG_TABLE_NAME, fields=fields)
    return [dict(zip(BIOG_MAIN.__fields__.keys(), row)) for row in biog_list]

# Order matters. This method should be at the end of the router for avoiding to override sub-path methods
@router.get("/{c_personid}", responses={status.HTTP_200_OK: {"model": BIOG_MAIN},
                                  status.HTTP_404_NOT_FOUND: {"model": GenericExceptionMessage}})
def get_biog_details(c_personid: int):

    result =  db.query_inner_join(db_file=DB_FILE, table_left=BIOG_TABLE_NAME, table_right=ASSOC_DATA_TABLE_NAME,
                            field_key_left='c_personid', field_key_right='c_personid', field_filters_left={'c_personid': c_personid}, field_filters_right={})
    # 打印结果
    for item in result:
        print(item)
    # result2 = db.query_inner_join(db_file=DB_FILE, table_left==BIOG_TABLE_NAME, table_right= ASSOC_DATA_TABLE_NAME fields={"c_personid": c_personid})
    # result = db.query_db(db_file=DB_FILE, table=BIOG_TABLE_NAME, fields={"c_personid": c_personid})

    # if not result:
    #     return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
    #                         content={"status_code": status.HTTP_404_NOT_FOUND,
    #                                  "detail": f"BIOG_MAIN with c_personid {c_personid} didn't exists in DB."})

    # # 将元组转换为字典
    # result_dict = [dict(zip(BIOG_MAIN.__fields__.keys(), row)) for row in result]

    # # 如果 result_dict 的长度为 1，则返回字典，否则返回列表
    # result_final = result_dict[0] if len(result_dict) == 1 else result_dict
    # print(result,'\n ====> result')
    # print(result_dict,'\n ====> result_dict')
    # print(type(result_final), type(result), type(result_final))

    # return result_final
