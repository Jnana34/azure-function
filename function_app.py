import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="FunctionJnanaranjan")
def FunctionJnanaranjan(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    if name:
        response = {
            "message": f"Hello, {name}!",
            "success": True
        }
    else:
        response = {
            "message": "Please provide a name in the query string or in the request body.",
            "success": False
        }

    return func.HttpResponse(
        body=json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )
