from flask import Blueprint, render_template, request, jsonify
from app import db
from models import lottohis_model
from models.lottohis_model import Lotto_his
from services import lotto_ml
import random


bp = Blueprint('main', __name__)

# sanity check route
# @bp.route('/')
# def index():
#     print("pingpong")
#     return jsonify('main!')

@bp.route('/lottoml', methods=['GET'])
def index():
    response_object = {'status': 'success'}
    get_lottohis = Lotto_his.query.filter_by().order_by(Lotto_his.id.desc()).limit(100).all()
    lotto_sum_list = []
    lotto_sum = 0
    lotto_result = []
    for lottohis in get_lottohis:
        lotto_sum = lottohis.one
        lotto_sum += lottohis.two
        lotto_sum += lottohis.three
        lotto_sum += lottohis.four
        lotto_sum += lottohis.five
        lotto_sum += lottohis.six
        lotto_sum_list.append(lotto_sum)
    # print('get_lottohis :::::',lotto_sum_list)
    
    y_predict = lotto_ml.lotto_ml(lotto_sum_list)
    print("y_predict 돌아옴", y_predict.astype(int)[0][0])
    y_predict = y_predict.astype(int)[0][0]

    new_lotto_list = []
    lotto_number = set()
    total = 0
    while(len(lotto_number) < 6):
            num = random.randint(1,45)
            lotto_number.add(num)
    for index, value in enumerate(lotto_number):
        total += value
    isdivide = y_predict/total
    for index, value in enumerate(lotto_number):
        new_lotto_list.append(round(value*isdivide))

    print('new_lotto_list : ',new_lotto_list)
    response_object["lotto_result"] = new_lotto_list
    return jsonify(response_object)