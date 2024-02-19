from src.errors.error_handler import handle_errors
from src.main.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class MockError422(HttpUnprocessableEntityError):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message

class MockError(Exception):
    def __init__(self,message) -> None:
        super().__init__(message)
        self.message = message

def test_handle_errors_with_error_422():
    mock_error_422 = MockError422(message="Test Error Message")
    assert isinstance(mock_error_422, Exception)
    assert isinstance(mock_error_422, HttpUnprocessableEntityError)

    result = handle_errors(mock_error_422)
    assert isinstance(result, HttpResponse)

    assert hasattr(result, "status_code")
    assert hasattr(result, "body")

    assert "errors" in result.body
    assert "title" in result.body['errors'][0]
    assert "details" in result.body['errors'][0]

    assert result.status_code == mock_error_422.status_code
    assert result.body['errors'][0]['title'] == mock_error_422.name

def test_handle_general_errors():
    mock_error = MockError(message="Test Error Message")
    assert isinstance(mock_error, Exception)

    result = handle_errors(mock_error)
    assert isinstance(result, HttpResponse)

    assert hasattr(result, "status_code")
    assert hasattr(result, "body")

    assert "errors" in result.body
    assert "title" in result.body['errors'][0]
    assert "details" in result.body['errors'][0]

    assert result.status_code == 500
    assert result.body['errors'][0]['title'] == "Server Error"
