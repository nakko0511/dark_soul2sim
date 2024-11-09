from fastapi import APIRouter, Depends
from schemas import Arguments, Results


router = APIRouter()


@router.get("/")
async def calcrate(
        arguments: Arguments = Depends(),
) -> Results:
    # calcrate
    return Results()
