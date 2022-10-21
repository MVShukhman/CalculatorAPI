from models import ExpressionRequest, EvalResponse


def check_phrase_format(phrase: str) -> bool:
    for sym in phrase:
        if 39 < ord(sym) < 44 or 44 < ord(sym) < 58:
            continue
        else:
            return False
    return True


async def calculate_expression(expression: ExpressionRequest) -> EvalResponse:
    if not check_phrase_format(expression.phrase):
        return EvalResponse(full_response="Wrong syntax!")
    try:
        result = eval(expression.phrase)
    except ZeroDivisionError:
        return EvalResponse(full_response="Zero division error!")
    except SyntaxError:
        return EvalResponse(full_response="Wrong syntax!")

    return EvalResponse(value=result, full_response=f"{expression.phrase} = {result}")
