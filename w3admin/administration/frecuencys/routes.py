from flask import Blueprint, request, jsonify, render_template
from w3admin import db
from w3admin.administration.frecuencys.models import Frecuency
from w3admin.administration.frecuencys.functions import format_frecuency_data

frecuencys_bp = Blueprint('frecuencys', __name__, url_prefix='/admin/frecuencys')

@frecuencys_bp.route("/")
def list_frecuencys():
    context = {"page_title": "Frecuencias"}
    frecuency_list = Frecuency.query.all()
    return render_template("w3admin/administration/listfrecuencys.html", **context, frecuency_list=frecuency_list)