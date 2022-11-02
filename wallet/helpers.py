import json
from typing import Any, Dict

from django.http.response import HttpResponse


def write_json_response(
    status_code: int, data: Any, headers: Dict[str, str] = dict()
) -> HttpResponse:
    data = {'message': data} if type(data) is str else data

    res = HttpResponse(json.dumps(data), content_type='application/json')
    res.status_code = status_code

    for k, v in headers.items():
        res[k] = v

    return res
