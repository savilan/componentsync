from datetime import datetime
from w3admin.models import VisitLog
from babel.dates import format_datetime

def get_datetime():
    return datetime


def get_recent_visits(limit=5):
    visits = VisitLog.query.order_by(VisitLog.created_at.desc()).limit(limit).all()
    result = []
    for v in visits:
        fecha = format_datetime(v.created_at, "EEEE d", locale="es_CL")  # Ej: "sábado 26"
        hora = format_datetime(v.created_at, "HH:mm", locale="es_CL")     # Ej: "22:27"
        result.append({
            "dia": v.created_at.day,
            "dia_semana": fecha.split()[0].capitalize(),  # "Sábado"
            "route": v.route,
            "ip": v.ip_address,
            "hora": hora,
        })
    return result
