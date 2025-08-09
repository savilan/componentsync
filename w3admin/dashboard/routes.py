from flask import Blueprint, render_template
from flask_login import login_required
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route("/index")
@login_required
def dashboard_index():
    return render_template("w3admin/dashboard/index.html", page_title="Dashboard", datetime=datetime)