from flask import Blueprint, render_template, request, jsonify
from app import db
from models import lottohis_model
from models.lottohis_model import Lotto_his

bp = Blueprint('main', __name__)

# sanity check route
@bp.route('/')
def index():
    print("pingpong")
    return jsonify('main!')

@bp.route('/lottoml')
def index():
    # print("pingpong")
    get_lottohis = Lotto_his.query.filterby().order_by(desc(Lotto_his.id)).limit(100).all()
    print('get_lottohis :::::',get_lottohis)
    return jsonify('main!')