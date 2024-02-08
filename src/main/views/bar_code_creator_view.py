from src.controllers.bar_code_creator_controller import BarCodeCreatorController
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class BarCodeCreatorView:
    '''
    Responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        barcode_creator_controller = BarCodeCreatorController()

        body = http_request.body
        product_code = body['product_code']

        formatted_response = barcode_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
