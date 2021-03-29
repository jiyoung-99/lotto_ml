from flask import Blueprint, render_template, request, jsonify
import uuid
from app import db
from models import support_model
from models.support_model import Support

bp = Blueprint('support', __name__)

@bp.route('/', methods=['GET', 'POST'])
def all_support():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        set_support = Support(
            id = uuid.uuid4().hex,
            title = post_data.get('title'),
            writer = post_data.get('writer'),
            content = post_data.get('content') 
        )
        print('set_support',set_support, post_data.get('title'))
        db.session.add(set_support)
        db.session.commit()
        response_object['message'] = '문의사항이 등록되었습니다'
    else:
        get_all_support = Support.query.filter_by().all()
        support_list = []
        for support in get_all_support:
            supports = {
                "id":support.id,
                "title":support.title,
                "writer":support.writer,
                "content":support.content
            }
            support_list.append(supports)
        print('support_list',support_list)
        response_object['supports'] = support_list
    return jsonify(response_object)

@bp.route('/<s_ID>', methods=['PUT', 'DELETE'])
def single_support(s_ID):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)
        get_delete_support = Support.query.filter_by(id=s_ID).first()
        db.session.delete(get_delete_support)
        reset_support = Support(
            id = s_ID,
            title = post_data.get('title'),
            writer = post_data.get('writer'),
            content = post_data.get('content')
        )
        db.session.add(reset_support)
        db.session.commit()
        response_object['message'] = '업데이트되었습니다.'
    if request.method == 'DELETE':
        get_delete_support = Support.query.filter_by(id=s_ID).first()
        db.session.delete(get_delete_support)
        db.session.commit()
        response_object['message'] = '삭제되었습니다.'
        
    return jsonify(response_object)
