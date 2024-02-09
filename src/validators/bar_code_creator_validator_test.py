from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .bar_code_creator_validator import bar_code_creator_validator

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_bar_code_creator_validator():
    request = MockRequest(json={ "product_code": "12345" })
    bar_code_creator_validator(request)

def test_bar_code_creator_validator_with_errors():
    request = MockRequest(json={ "product_code": 12345 })

    try:
        bar_code_creator_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
