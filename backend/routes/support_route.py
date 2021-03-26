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
        Support.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'writer': post_data.get('writer'),
            'content': post_data.get('content') 
        })
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

@bp.route('/<s_id>', methods=['PUT', 'DELETE'])
def single_book(s_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_support(s_id)
        Support.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'writer': post_data.get('writer'),
            'content': post_data.get('content')
        })
        response_object['message'] = '업데이트되었습니다.'
    if request.method == 'DELETE':
        remove_support(s_id)
        response_object['message'] = '삭제되었습니다.'
        
    return jsonify(response_object)

def remove_support(s_id):
    for support in supports:
        if support['s_id'] == s_id:
            supports.remove(support)
            return True
    return False

# Support = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'writer': 'Jack Kerouac',
#         'content': 'gooood'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'writer': 'J. K. Rowling',
#         'content': 'gooood'
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'writer': 'Dr. Seuss',
#         'content': 'gooood'
#     }
# ]
