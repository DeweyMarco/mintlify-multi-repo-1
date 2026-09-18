"""HTTP API for the merge sort service."""

from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .algorithm import merge_sort

app = FastAPI(
    title="Merge Sort API",
    version="1.0.0",
    description="Sort a list of numbers with a stable merge sort implementation.",
)


class SortRequest(BaseModel):
    values: Annotated[list[float], Field(max_length=10_000)]
    descending: bool = False


class SortResponse(BaseModel):
    values: list[float]
    count: int
    descending: bool


@app.get("/health", tags=["System"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/sort", response_model=SortResponse, tags=["Sorting"])
def sort_values(request: SortRequest) -> SortResponse:
    values = merge_sort(request.values)
    if request.descending:
        values.reverse()
    return SortResponse(
        values=values,
        count=len(values),
        descending=request.descending,
    )
