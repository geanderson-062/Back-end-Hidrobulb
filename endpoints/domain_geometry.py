from fastapi import APIRouter
from services.domain_geometry import (
    generate_domain_geometry_sul,
    generate_domain_geometry_sudeste,
    generate_domain_geometry_centro_oeste,
    generate_domain_geometry_nordeste,
    generate_domain_geometry_norte,
)
from models.domain_geometry import DomainGeometry

router = APIRouter()


@router.get(
    "/domain_geometry/norte",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry Norte",
)
def get_domain_geometry():
    return generate_domain_geometry_norte()


@router.get(
    "/domain_geometry/nordeste",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry",
)
def get_domain_geometry():
    return generate_domain_geometry_nordeste()


@router.get(
    "/domain_geometry/centro_oeste",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry Centro Oeste",
)
def get_domain_geometry():
    return generate_domain_geometry_centro_oeste()


@router.get(
    "/domain_geometry/sudeste",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry Sudeste",
)
def get_domain_geometry():
    return generate_domain_geometry_sudeste()


@router.get(
    "/domain_geometry/sul",
    response_model=DomainGeometry,
    tags=["Domain Geometry"],
    summary="Get Domain Geometry Sul",
)
def get_domain_geometry():
    return generate_domain_geometry_sul()
