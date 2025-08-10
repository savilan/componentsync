from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required
from w3admin import db
from w3admin.gestion.schedules.models import Schedule
from w3admin.gestion.schedules.functions import format_schedule_data
from datetime import datetime, timedelta
from datetime import datetime

schedules_bp = Blueprint('schedules', __name__, url_prefix='/gestion/schedules')

@schedules_bp.route("/")
@login_required
def schedules_list_view():
    context = {"page_title": "Horarios"}
    schedules = Schedule.query.order_by(Schedule.id.desc()).all()
    return render_template("w3admin/gestion/listschedules.html", schedules=schedules, datetime=datetime, **context)


@schedules_bp.route("/add", methods=["POST"])
def add_schedule():
    try:
        data = request.json
        new = Schedule(
            title=data['title'],
            start_day=datetime.strptime(data['start_day'], "%Y-%m-%d").date(),
            start_datetime=datetime.strptime(data['start_datetime'], "%H:%M").time(),
            end_day=datetime.strptime(data['end_day'], "%Y-%m-%d").date(),
            end_datetime=datetime.strptime(data['end_datetime'], "%H:%M").time(),
            status_id=int(data['status_id']),
            condition_id=int(data['condition_id']),
            frecuency_id=int(data['frecuency_id']),
            count=int(data['count']),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new)
        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error en /add:", str(e))
        return jsonify(success=False, error=str(e)), 500

@schedules_bp.route("/update/<int:id>", methods=["POST"])
def update_schedule(id):
    try:
        data = request.json
        schedule = Schedule.query.get(id)
        if not schedule:
            return jsonify(success=False, error="Horario no encontrado"), 404

        schedule.title = data['title']
        schedule.start_day = datetime.strptime(data['start_day'], "%Y-%m-%d").date()
        schedule.start_datetime = datetime.strptime(data['start_datetime'], "%H:%M").time()
        schedule.end_day = datetime.strptime(data['end_day'], "%Y-%m-%d").date()
        schedule.end_datetime = datetime.strptime(data['end_datetime'], "%H:%M").time()
        schedule.status_id = int(data['status_id'])
        schedule.condition_id = int(data['condition_id'])
        schedule.frecuency_id = int(data['frecuency_id'])
        schedule.count = int(data['count'])
        schedule.updated_at = datetime.utcnow()

        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error en /update:", str(e))
        return jsonify(success=False, error=str(e)), 500

@schedules_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_schedule(id):
    try:
        schedule = Schedule.query.get(id)
        if not schedule:
            return jsonify(success=False, error="No se pudo eliminar"), 404
        db.session.delete(schedule)
        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error en /delete:", str(e))
        return jsonify(success=False, error=str(e)), 500

@schedules_bp.route("/clone/<int:id>", methods=["POST"])
def clone_schedule(id):
    try:
        source = Schedule.query.get(id)
        if not source:
            return jsonify(success=False, error="Horario no encontrado")

        data = request.get_json()
        count = int(data.get("count", 1))
        duration = int(data.get("duration", 15))  # en minutos

        base_start = datetime.utcnow()

        for i in range(count):
            start = base_start + timedelta(minutes=i * duration)
            end = start + timedelta(minutes=duration)

            cloned = Schedule(
                title=f"{source.title} (copia {i+1})",
                start_day=start.date(),
                start_datetime=start.time(),
                end_day=end.date(),
                end_datetime=end.time(),
                status_id=source.status_id,
                condition_id=source.condition_id,
                frecuency_id=source.frecuency_id,
                count=source.count,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            db.session.add(cloned)

        db.session.commit()
        return jsonify(success=True)
    except Exception as e:
        print("Error en clonado:", str(e))
        return jsonify(success=False, error=str(e)), 500

