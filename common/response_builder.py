from typing import Dict, Any


def build(message: str) -> Dict[str, Any]:
    return {"statusCode": 200, "body": message}
