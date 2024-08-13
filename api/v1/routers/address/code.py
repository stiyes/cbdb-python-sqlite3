from typing import Optional, List

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel
from starlette.responses import JSONResponse

from api.model.generic import GenericMessage, GenericExceptionMessage
from api.model.address.code import ADDRESS_CODES
from api.utils import db
from api.utils.db import DB_FILE
from api.utils.login import validate_access_token

router = APIRouter()
ADDRESS_CODES_TABLE_NAME = 'ADDR_CODES'


@router.get("", responses={status.HTTP_200_OK: {"model": List[ADDRESS_CODES]}})
def list(c_addr_id: Optional[int] = 7061):
    fields = {}
    if c_addr_id:
        fields['c_addr_id'] = c_addr_id
    print(ADDRESS_CODES.__fields__.keys())
    list = db.query_db(db_file=DB_FILE, table=ADDRESS_CODES_TABLE_NAME, fields=fields)
    res = {}
    res['list'] = [dict(zip(ADDRESS_CODES.__fields__.keys(), row)) for row in list]
    res['total'] = len(list)
    return res


@router.put("", responses={status.HTTP_200_OK: {"model": GenericMessage},
                           status.HTTP_400_BAD_REQUEST: {"model": GenericExceptionMessage},
                           status.HTTP_409_CONFLICT: {"model": GenericExceptionMessage}})
def update_address(c_addr_id: int = 7061, c_name_zh: Optional[str] = None, c_notes_zh: Optional[str] = None,
                  c_alt_names_zh: Optional[str] = None):
    if not c_name_zh and not c_notes_zh and not c_alt_names_zh:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"status_code": status.HTTP_400_BAD_REQUEST,
                                     "detail": f"No fields to update in ADDRESS_CODES with code {c_addr_id}, "
                                               f"please provide a new c_name_zh, c_notes_zh or c_alt_names_zh at least."})
    fields = {}
    if c_name_zh:
        fields['c_name_zh'] = c_name_zh
    if c_notes_zh:
        fields['c_notes_zh'] = c_notes_zh
    if c_alt_names_zh:
        fields['c_alt_names_zh'] = c_alt_names_zh

    if not db.update_db(db_file=DB_FILE, table=ADDRESS_CODES_TABLE_NAME, field_id_name='c_addr_id', field_id_value=c_addr_id,
                        fields_to_update=fields):
        return JSONResponse(status_code=status.HTTP_409_CONFLICT,
                            content={"status_code": status.HTTP_409_CONFLICT,
                                     "detail": f"Can't update ADDRESS_CODES with c_addr_id {c_addr_id}"})
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "status_code": status.HTTP_200_OK, 
        "detail": f"ADDRESS_CODES with c_addr_id {c_addr_id} updated"})