def handle(event={}, context={}):
    query_params = event.get("queryStringParameters")
    query_params = query_params if query_params else {}
    name = query_params.get("name", {})
    name = name if name else "World"
    return {"statusCode": 200, "body": "Hello %s" % name}
