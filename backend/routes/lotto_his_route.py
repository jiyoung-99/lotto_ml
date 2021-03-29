from flask import Blueprint, render_template, request, jsonify
from app import db
from models import lottohis_model
from models.lottohis_model import Lotto_his


bp = Blueprint('lotto_his', __name__)

# sanity check route
@bp.route('/')
def index():
    response_object = {'status': 'success'}
    get_lottohises = Lotto_his.query.filter_by().all()
    lottohis_id_list = []
    for lottohis in get_lottohises:
        lottohis_id = lottohis.id
        lottohis_id_list.append(lottohis_id)
    response_object["lottohis_id"] = lottohis_id_list

    return jsonify(response_object)

@bp.route('/one/<int:id>', methods=['GET'])
def lottoSelectOne(id):
    response_object = {'status': 'success'}
    lotto_id = id
    print("lotto id : ", lotto_id)
    getlotto = Lotto_his.query.filter_by(id=lotto_id).first()
    lotto = {
        "id":getlotto.id,
        "date_l":getlotto.date_l,
        "first_num":getlotto.first_num,
        "first_cnt":getlotto.first_cnt,
        "sec_num":getlotto.sec_num,
        "sec_cnt":getlotto.sec_cnt,
        "thd_num":getlotto.thd_num,
        "thd_cnt":getlotto.thd_cnt,
        "one":getlotto.one,
        "two":getlotto.two,
        "three":getlotto.three,
        "four":getlotto.four,
        "five":getlotto.five,
        "six":getlotto.six,
        "bonus":getlotto.bonus

    }
    response_object["selectLottoOne"] = lotto
    print(response_object)
    return jsonify(response_object)

