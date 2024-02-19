from unittest.mock import patch
from src.drivers.barcode_handler import BarCodeHandler
from .bar_code_creator_view import BarCodeCreatorView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class MockRequest(HttpRequest):
    def __init__(self, body) -> None:
        super().__init__(body=body)

@patch.object(BarCodeHandler, 'create_barcode')
def test_validate_and_create(mock_create_tag):
    mock_http_request = MockRequest({ "product_code": "12345" })
    assert isinstance(mock_http_request, HttpRequest)

    mock_create_tag.return_value = f'{mock_http_request.body['product_code']}.png'

    barcode_creator_view = BarCodeCreatorView()
    result = barcode_creator_view.validate_and_create(mock_http_request)

    assert isinstance(result, HttpResponse)
    assert hasattr(result, 'status_code')
    assert hasattr(result, 'body')
    assert isinstance(result.status_code, int)
    assert isinstance(result.body, dict)
    assert result.status_code == 200
