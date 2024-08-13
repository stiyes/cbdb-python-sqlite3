from fastapi import APIRouter

from api.v1.routers import health,cbdb_name_list
from api.v1.routers.biog import main as biog_main
from api.v1.routers.assoc import main as assoc_data
from api.v1.routers.address import code as address_code
# schools, positions, assignments


def get_api():
    api_router = APIRouter()
    api_router.include_router(health.router)
    api_router.include_router(cbdb_name_list.router, prefix="/cbdb_name_list")
    api_router.include_router(biog_main.router, prefix="/biog/main")
    api_router.include_router(assoc_data.router, prefix="/assoc/data")
    api_router.include_router(address_code.router, prefix="/address/code")
    # api_router.include_router(positions.router, prefix="/positions")
    # api_router.include_router(assignments.router, prefix="/assignments")
    return api_router
