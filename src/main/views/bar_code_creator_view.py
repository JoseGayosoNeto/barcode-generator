from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class BarCodeCreatorView:
    '''
    Responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body['product_code']

        return HttpResponse(status_code=200, body={"product_code": product_code})