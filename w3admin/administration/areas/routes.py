from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from w3admin import db
from w3admin.administration.areas.models import Area
from w3admin.administration.areas.functions import format_area_data

areas_bp = Blueprint('areas', __name__, url_prefix='/admin/areas')

@areas_bp.route("/")
@login_required
def list_areas():
    context = {"page_title": "Áreas"}
    areas = Area.query.all()
    return render_template("w3admin/administration/listareas.html", **context, areas=areas)

@areas_bp.route("/add", methods=["POST"])
def add_area():
    data = request.json
    print(data)
    new_area = Area(area=data['area'], description=data['description'], status_id=1)
    db.session.add(new_area)
    db.session.commit()
    return jsonify(success=True)

@areas_bp.route("/update/<int:id>", methods=["POST"])
def update_area(id):
    data = request.json
    area = Area.query.get(id)
    if area:
        area.area = data['area']
        area.description = data['description']
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="Área no encontrada")

@areas_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_area(id):
    area = Area.query.get(id)
    if area:
        db.session.delete(area)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="Área no encontrada")

@areas_bp.route("/update_status/<int:id>", methods=["POST"])
def update_area_status(id):
    data = request.json
    area = Area.query.get(id)
    if area:
        area.status_id = data['status_id']
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="Área no encontrada")