from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from w3admin import db
from w3admin.administration.ecomponents.models import EComponent
from w3admin.administration.ecomponents.functions import format_ecomponent_data
from w3admin.administration.ecpus.models import ECPU
from w3admin.administration.frecuencys.models import Frecuency

ecomponents_bp = Blueprint('ecomponents', __name__, url_prefix='/admin/ecomponents')

@ecomponents_bp.route("/")
# @login_required
def list_ecomponents():
    context = {"page_title": "EComponents"}
    ecomponents = EComponent.query.all()
    ecpu_list = ECPU.query.all()
    frecuency_list = Frecuency.query.all()  # 🔥 Ahora también obtenemos la lista de frecuencias
    return render_template("w3admin/administration/listecomponents.html", 
                           **context, ecomponents=ecomponents, ecpu_list=ecpu_list, frecuency_list=frecuency_list)

@ecomponents_bp.route("/add", methods=["POST"])
def add_ecomponent():
    data = request.get_json(force=True)
    print("Datos recibidos para agregar:", data)  # 🔥 Verifica qué datos llegan en Flask

    if not data or 'node' not in data or 'code' not in data or 'name' not in data or 'description' not in data or 'ecpu_id' not in data or 'frecuency_id' not in data:
        return jsonify(success=False, error="Faltan datos"), 400

    new_ecomponent = EComponent(
        node=data['node'],
        code=data['code'],
        name=data['name'],
        description=data['description'],
        status_id=1,
        ecpu_id=data['ecpu_id'],
        frecuency_id=data['frecuency_id']
    )

    db.session.add(new_ecomponent)
    db.session.commit()
    return jsonify(success=True)

@ecomponents_bp.route("/update/<int:id>", methods=["POST"])
def update_ecomponent(id):
    data = request.get_json(force=True)
    print("Datos recibidos para actualización:", data)

    ecomponent = EComponent.query.get(id)
    if ecomponent:
        ecomponent.node = data.get('node', ecomponent.node)
        ecomponent.code = data.get('code', ecomponent.code)
        ecomponent.name = data.get('name', ecomponent.name)
        ecomponent.description = data.get('description', ecomponent.description)
        db.session.commit()
        return jsonify(success=True)
    
    return jsonify(success=False, error="Componente no encontrado"), 404


@ecomponents_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_ecomponent(id):
    ecomponent = EComponent.query.get(id)
    if ecomponent:
        db.session.delete(ecomponent)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False, error="Componente no encontrado"), 404

@ecomponents_bp.route("/update_status/<int:id>", methods=["POST"])
def update_ecomponent_status(id):
    data = request.get_json(force=True)
    print("Datos recibidos para actualización de estado:", data)

    ecomponent = EComponent.query.get(id)
    if ecomponent:
        ecomponent.status_id = data.get('status_id', ecomponent.status_id)
        db.session.commit()
        return jsonify(success=True)

    return jsonify(success=False, error="Componente no encontrado"), 404