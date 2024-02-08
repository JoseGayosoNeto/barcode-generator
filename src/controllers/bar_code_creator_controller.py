from typing import Dict
from src.drivers.barcode_handler import BarCodeHandler

class BarCodeCreatorController:
    '''
    resposability for implementing business rules
    '''
    def create(self, product_code: str) -> Dict:
        path_from_bar_code = self.__create_tag(product_code)
        formatted_response = self.__format_response(path_from_bar_code)
        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarCodeHandler()
        path_from_bar_code = barcode_handler.create_barcode(product_code)
        return path_from_bar_code

    def __format_response(self, path_from_bar_code: str) -> Dict:
        return {
            "data": {
                "type": "Bar Code Image",
                "count": 1,
                "path": f'{path_from_bar_code}.png'
            }
        }
