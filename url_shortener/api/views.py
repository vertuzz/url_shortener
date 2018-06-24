from flask import Blueprint, request, jsonify
from url_shortener.core.url_core import save_url


api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/url', methods=['POST'])
def add_url():
    data = request.get_json(force=True)
    short_url = save_url(data['url'], domain=request.url_root)
    return jsonify({'short_url': short_url})

