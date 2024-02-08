from flask import Flask, request, jsonify, make_response
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)


@app.route('/create_tag', methods=['POST'])
def create_tag():
    body = request.json
    product_code = body.get('product_code')
    bar_code = Code128(product_code, writer=ImageWriter())
    path_from_bar_code = f'{bar_code}'
    bar_code.save(path_from_bar_code)

    return make_response(jsonify({"bar_code path": path_from_bar_code}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)