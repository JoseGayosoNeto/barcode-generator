from flask import Blueprint, request, jsonify, make_response
from src.main.views.http_types.http_request import HttpRequest
from src.main.views.bar_code_creator_view import BarCodeCreatorView

bar_code_blueprints = Blueprint('bar_code_routes', __name__)

@bar_code_blueprints.route('/create_tag', methods=['POST'])
def create_bar_code():
    barcode_creator_view = BarCodeCreatorView()

    http_request = HttpRequest(body=request.json)
    response = barcode_creator_view.validate_and_create(http_request)

    return make_response(jsonify(response.body), response.status_code)
