from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('ping', __name__)

# sanity check route
@bp.route('/')
def ping_pong(methods=["GET", "POST"]):
    print("pingpong")
    return jsonify('pong!')