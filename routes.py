from fastapi import APIRouter, HTTPException, status
from models import ExpressionRequest, EvalResponse
from services import calculate_expression

eval_router = APIRouter()


@eval_router.get("/eval/calc")
async def get_eval(request: ExpressionRequest) -> str:
    response = await calculate_expression(request)
    if response.value is None:
        raise HTTPException(status_code=400, detail=response.full_response)
    return response.full_response


@eval_router.post(
    "/eval/calc", status_code=status.HTTP_201_CREATED
)
async def post_eval(request: ExpressionRequest):
    response = await calculate_expression(request)
    if response.value is None:
        raise HTTPException(status_code=400, detail=dict(response))
    return response
