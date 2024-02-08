from barcode import Code128
from barcode.writer import ImageWriter

class BarCodeHandler:
    '''
    Handle external libraries
    '''
    def create_barcode(self, product_code: str) -> str:
        bar_code = Code128(product_code, writer=ImageWriter())
        path_from_bar_code = f'{bar_code}'
        bar_code.save(path_from_bar_code)

        return path_from_bar_code
