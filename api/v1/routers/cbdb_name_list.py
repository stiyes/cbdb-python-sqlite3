from typing import Optional, List

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from api.model.generic import GenericMessage, GenericExceptionMessage
from api.model.cbdb_name_list import CBDB_NAME_LIST
from api.utils import db
from api.utils.db import DB_FILE
from api.utils.login import validate_access_token

router = APIRouter()
CBDB_NAME_TABLE_NAME = 'CBDB_NAME_LIST'


@router.get("", responses={status.HTTP_200_OK: {"model": List[CBDB_NAME_LIST]}})
def list(c_personid: Optional[int] = 1, name: Optional[str] = None,
                 source: Optional[str] = None):
    fields = {}
    if c_personid:
        fields['c_personid'] = c_personid
    if name:
        fields['name'] = name
    if source:
        fields['source'] = source

    return [CBDB_NAME_LIST(*row)
            for row in db.query_db(db_file=DB_FILE, table=CBDB_NAME_TABLE_NAME, fields=fields)]