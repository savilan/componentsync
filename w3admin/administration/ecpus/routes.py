from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from w3admin import db
from w3admin.administration.ecpus.models import ECPU
from w3admin.administration.ecpus.functions import format_ecpu_data
from w3admin.administration.ecpus.functions import format_ecpu_data

ecpus_bp = Blueprint('ecpus', __name__, url_prefix='/admin/ecpus')

@ecpus_bp.route("/")
@login_required
def list_ecpus():
    context = {"page_title": "ECPUs"}
    ecpu_list = ECPU.query.all()
    return render_template("w3admin/administration/listecpus.html", **context, ecpu_list=ecpu_list)

@ecpus_bp.route("/add", methods=["POST"])
def add_ecpu():
    try:
        data = request.get_json(force=True)
        print("Datos recibidos para agregar:", data)

        if not data or 'code' not in data or 'node' not in data or 'name' not in data or 'descrip' not in data:
            return jsonify(success=False, error="Faltan datos"), 400

        new_ecpu = ECPU(
            code=data['code'],
            node=data['node'],
            name=data['name'],
            descrip=data['descrip'],
            status_id=1,
            e_inventory_id=None  # Puedes ajustar si necesitas este valor
        )

        db.session.add(new_ecpu)
        db.session.commit()
        return jsonify(success=True)

    except Exception as e:
        print("Error al agregar ECPU:", str(e))
        return jsonify(success=False, error="Error interno: " + str(e)), 500

@ecpus_bp.route("/update/<int:id>", methods=["POST"])
def update_ecpu(id):
    data = request.get_json(force=True)
    print("Datos recibidos para actualización:", data)

    ecpu = ECPU.query.get(id)
    if ecpu:
        ecpu.code = data.get('code', ecpu.code)
        ecpu.node = data.get('node', ecpu.node)
        ecpu.name = data.get('name', ecpu.name)
        ecpu.descrip = data.get('descrip', ecpu.descrip)
        db.session.commit()
        return jsonify(success=True)
    
    return jsonify(success=False, error="ECPU no encontrado"), 404

@ecpus_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_ecpu(id):
    ecpu = ECPU.query.get(id)
    if ecpu:
        db.session.delete(ecpu)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="ECPU no encontrado"), 404

@ecpus_bp.route("/update_status/<int:id>", methods=["POST"])
def update_ecpu_status(id):
    data = request.get_json(force=True)
    ecpu = ECPU.query.get(id)
    if ecpu:
        ecpu.status_id = data.get('status_id', ecpu.status_id)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="ECPU no encontrado"), 404