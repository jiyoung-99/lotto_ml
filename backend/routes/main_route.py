from flask import Blueprint, render_template, request, jsonify
bp = Blueprint('main', __name__)

# sanity check route
@bp.route('/')
def index():
    print("pingpong")
    return jsonify('main!')