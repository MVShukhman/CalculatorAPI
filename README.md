# CalculatorAPI

Install and run:<br>
<code>docker-compose up</code>
<br>
<br>
## Parameters
<code>
{
    "phrase": "2.5/(2*7)" 
}
</code> <br>

## Usage examples
<code>
curl --location --request POST 'localhost:8000/api/v1/eval/calc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phrase": "2.5/(2*7)"
}'
</code>
<br>
Response:
<br>
<code>
{
    "value": "0.17857142857142858",
    "full_response": "2.5/(2*7) = 0.17857142857142858"
}
</code>
<br>
<code>
"POST /api/v1/eval/calc HTTP/1.1" 201 Created
</code>

<br>
<br>

<code>
curl --location --request GET 'localhost:8000/api/v1/eval/calc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phrase": "2.5/(2*7)"
}'
</code>
<br>
Response:
<br>
<code>
"2.5/(2*7) = 0.17857142857142858"
</code>
<br>
<code>
"GET /api/v1/eval/calc HTTP/1.1" 200 OK
</code>

<br>
<br>


<code>
curl --location --request POST 'localhost:8000/api/v1/eval/calc' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phrase": "7/0"
}'
</code>
<br>
Response:
<br>
<code>
"detail": {
        "value": null,
        "full_response": "Zero division error!"
    }
</code>
<br>
<code>
"POST /api/v1/eval/calc HTTP/1.1" 400 Bad Request
</code>

<br>
<br>
