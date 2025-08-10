from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime
from w3admin.models import VisitLog
from w3admin.gestion.schedules.models import Schedule as ProgressSchedule

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route("/index")
@login_required
def dashboard_index():
    entries = ProgressSchedule.query.order_by(ProgressSchedule.start_day.desc()).all()
    recent_visits = VisitLog.query.order_by(VisitLog.created_at.desc()).limit(5).all()

    return render_template(
        "w3admin/dashboard/index.html",
        page_title="Dashboard",
        datetime=datetime,
        entries=entries,
        recent_visits=recent_visits
    )