from unittest.mock import patch
from src.drivers.barcode_handler import BarCodeHandler
from .bar_code_creator_controller import BarCodeCreatorController

@patch.object(BarCodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = "product_code"
    mock_create_barcode.return_value = mock_value
    barcode_creator_controller = BarCodeCreatorController()

    result = barcode_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert 'type' in result['data']
    assert "count" in result['data']
    assert "path" in result['data']

    assert result['data']['type'] == "Bar Code Image"
    assert result['data']['count'] == 1
    assert result['data']['path'] == f"{mock_value}.png"
