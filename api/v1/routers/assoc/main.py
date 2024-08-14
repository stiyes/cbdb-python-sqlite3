from typing import Optional, List

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from api.model.generic import GenericMessage, GenericExceptionMessage
from api.model.assoc.main import ASSOC_DATA
from api.utils import db
from api.utils.db import DB_FILE
from api.utils.login import validate_access_token

router = APIRouter()
ASSCO_TABLE_NAME = 'ASSOC_DATA'


@router.get("", responses={status.HTTP_200_OK: {"model": List[ASSOC_DATA]}})
def list(c_personid: Optional[int] = None, showTotal: Optional[bool] = True):
    fields = {}
    if c_personid:
        fields['c_personid'] = c_personid
    print(ASSOC_DATA.__fields__.keys())
    list = db.query_db(db_file=DB_FILE, table=ASSCO_TABLE_NAME, fields=fields)
    list_dict =  [dict(zip(ASSOC_DATA.__fields__.keys(), row)) for row in list]
    if(showTotal is False):
        return list_dict   
    else:
        res = {}
        res['list'] = list_dict
        res['total'] = len(list)
        return res