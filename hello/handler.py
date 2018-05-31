import common.response_builder as response


def handle(event={}, context={}):
    query_params = event.get("queryStringParameters")
    query_params = query_params if query_params else {}
    name = query_params.get("name", {})
    name = name if name else "World"
    return response.build("Hello %s" % name)
