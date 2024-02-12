from fastapi import APIRouter
from services.domain_geometry import generate_domain_geometry
from models.domain_geometry import DomainGeometry

router = APIRouter()


@router.get(
    "/domain_geometry/",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry",
)
def get_domain_geometry():
    return generate_domain_geometry()
