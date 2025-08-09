from flask import Flask, render_template, Blueprint, request, g, jsonify, redirect, url_for, flash, session, current_app as app
from w3admin.administration.areas.routes import areas_bp
from w3admin.administration.ecpus.routes import ecpus_bp
from w3admin.administration.ecomponents.routes import ecomponents_bp
from w3admin.gestion.schedules.routes import schedules_bp
from w3admin.dashboard.routes import dashboard_bp
from flask_login import current_user
from functools import wraps
from datetime import datetime
from w3admin.administration.areas.models import Area
from .models import User, VisitLog
from . import db
import requests


main = Blueprint('main', __name__)

main.register_blueprint(areas_bp, url_prefix='/admin/areas')
main.register_blueprint(ecpus_bp, url_prefix='/admin/ecpus')
main.register_blueprint(ecomponents_bp, url_prefix='/admin/ecomponents')
main.register_blueprint(schedules_bp, url_prefix='/gestion/schedules')
main.register_blueprint(dashboard_bp, url_prefix='/dashboard')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


@main.route("/")
@main.route("/index")
def index():
    return redirect("/dashboard/index")


@main.route("/index-2")
def index_2():
    context = {
        "page_title": "Dashboard Dark"
    }
    return render_template("w3admin/index-2.html", **context)

def extract_ip():
    # Si X-Forwarded-For está presente y IP no es privada, úsala
    x_forwarded = request.headers.get("X-Forwarded-For", "").split(',')[0].strip()

    def is_public(ip):
        return not (
            ip.startswith("127.") or
            ip.startswith("192.168.") or
            ip.startswith("10.") or
            ip.startswith("::1") or
            ip == "localhost"
        )

    if x_forwarded and is_public(x_forwarded):
        return x_forwarded

    return request.remote_addr


def get_country(ip_address):
    # Ignorar IPs privadas
    if ip_address.startswith("127.") or ip_address.startswith("192.168.") or ip_address.startswith("10.") or ip_address == "localhost":
        return "Local"

    try:
        res = requests.get(f"https://ipapi.co/{ip_address}/country_name/", timeout=2)
        if res.ok:
            texto = res.text.strip()
            if texto and texto.lower() != "undefined":
                return texto
    except Exception:
        pass
    return "Desconocido"



DEFAULT_USER_ID = 0

@main.before_request
def log_visit():
    ip_address = extract_ip()
    route = request.path
    user_id = session.get('user_id', DEFAULT_USER_ID)
    country = get_country(ip_address)

    visit_log = VisitLog(
        ip_address=ip_address,
        user_id=user_id,
        route=route,
        country=country
    )
    db.session.add(visit_log)
    db.session.commit()


@main.route("/index-3")
def index_3():
    context={
        "page_title":"Dashboard 3"
    }
    return render_template("w3admin/index-3.html",**context)


@main.route("/index-4")
def index_4():
    context={
        "page_title":"Dashboard 4"
    }
    return render_template("w3admin/index-4.html",**context)

    
@main.route("/crm")
def crm():
    context={
        "page_title":"CRM"
    }
    return render_template("w3admin/crm.html",**context)

@main.route("/analytics")
def analytics():
    context={
        "page_title":"Analytics"
    }
    return render_template("w3admin/analytics.html",**context)


@main.route("/contacts")
def contacts():
    context={
        "page_title":"Contacts"
    }
    return render_template("w3admin/contacts.html",**context)

@main.route("/blog")
def blog():
    context={
        "page_title":"Blog"
    }
    return render_template("w3admin/blog.html",**context)

@main.route("/chat")
def chat():
    context={
        "page_title":"Chat"
    }
    return render_template("w3admin/apps/chat.html",**context)

@main.route("/app-profile-1")
def app_profile_1():
    context={
        "page_title":"App Profile 1"
    }
    return render_template("w3admin/apps/app-profile-1.html",**context)

@main.route("/app-profile-2")
def app_profile_2():
    context={
        "page_title":"App Profile 2"
    }
    return render_template("w3admin/apps/app-profile-2.html",**context)

@main.route("/edit-profile")
def edit_profile():
    context={
        "page_title":"Edit Profile"
    }
    return render_template("w3admin/apps/edit-profile.html",**context)

@main.route("/post-details")
def post_details():
    context={
        "page_title":"Post Details"
    }
    return render_template("w3admin/apps/post-details.html",**context)

@main.route("/email-compose")
def email_compose():
    context={
        "page_title":"Compose"
    }
    return render_template("w3admin/apps/email/email-compose.html",**context)

@main.route("/email-inbox")
def email_inbox():
    context={
        "page_title":"Inbox"
    }
    return render_template("w3admin/apps/email/email-inbox.html",**context)

@main.route("/email-read")
def email_read():
    context={
        "page_title":"Read"
    }
    return render_template("w3admin/apps/email/email-read.html",**context)

@main.route("/app-calendar")
def app_calendar():
    context={
        "page_title":"Calendar"
    }
    return render_template("w3admin/apps/app-calendar.html",**context)

@main.route("/ecom-product-grid")
def ecom_product_grid():
    context={
        "page_title":"Product Grid"
    }
    return render_template("w3admin/apps/shop/ecom-product-grid.html",**context)

@main.route("/ecom-product-list")
def ecom_product_list():
    context={
        "page_title":"Product List"
    }
    return render_template("w3admin/apps/shop/ecom-product-list.html",**context)

@main.route("/ecom-product-detail")
def ecom_product_detail():
    context={
        "page_title":"Product Detail"
    }
    return render_template("w3admin/apps/shop/ecom-product-detail.html",**context)

@main.route("/ecom-product-order")
def ecom_product_order():
    context={
        "page_title":"Product Order"
    }
    return render_template("w3admin/apps/shop/ecom-product-order.html",**context)

@main.route("/ecom-checkout")
def ecom_checkout():
    context={
        "page_title":"Checkout"
    }
    return render_template("w3admin/apps/shop/ecom-checkout.html",**context)

@main.route("/ecom-invoice")
def ecom_invoice():
    context={
        "page_title":"Invoice"
    }
    return render_template("w3admin/apps/shop/ecom-invoice.html",**context)

@main.route("/ecom-customers")
def ecom_customers():
    context={
        "page_title":"Customers"
    }
    return render_template("w3admin/apps/shop/ecom-customers.html",**context)


@main.route("/chart-flot")
def chart_flot():
    context={
        "page_title":"Chart Flot"
    }
    return render_template("w3admin/charts/chart-flot.html",**context)

@main.route("/chart-morris")
def chart_morris():
    context={
        "page_title":"Chart Morris"
    }
    return render_template("w3admin/charts/chart-morris.html",**context)

@main.route("/chart-chartjs")
def chart_chartjs():
    context={
        "page_title":"Chart Chartjs"
    }
    return render_template("w3admin/charts/chart-chartjs.html",**context)

@main.route("/chart-chartist")
def chart_chartist():
    context={
        "page_title":"Chart Chartist"
    }
    return render_template("w3admin/charts/chart-chartist.html",**context)

@main.route("/chart-sparkline")
def chart_sparkline():
    context={
        "page_title":"Chart Sparkline"
    }
    return render_template("w3admin/charts/chart-sparkline.html",**context)

@main.route("/chart-peity")
def chart_peity():
    context={
        "page_title":"Chart Peity"
    }
    return render_template("w3admin/charts/chart-peity.html",**context)


@main.route("/ui-accordion")
def ui_accordion():
    context={
        "page_title":"Accordion"
    }
    return render_template("w3admin/bootstrap/ui-accordion.html",**context)

@main.route("/ui-alert")
def ui_alert():
    context={
        "page_title":"Alert"
    }
    return render_template("w3admin/bootstrap/ui-alert.html",**context)

@main.route("/ui-badge")
def ui_badge():
    context={
        "page_title":"Badge"
    }
    return render_template("w3admin/bootstrap/ui-badge.html",**context)

@main.route("/ui-button")
def ui_button():
    context={
        "page_title":"Button"
    }
    return render_template("w3admin/bootstrap/ui-button.html",**context)

@main.route("/ui-modal")
def ui_modal():
    context={
        "page_title":"Modal"
    }
    return render_template("w3admin/bootstrap/ui-modal.html",**context)

@main.route("/ui-button-group")
def ui_button_group():
    context={
        "page_title":"Button Group"
    }
    return render_template("w3admin/bootstrap/ui-button-group.html",**context)

@main.route("/ui-list-group")
def ui_list_group():
    context={
        "page_title":"List Group"
    }
    return render_template("w3admin/bootstrap/ui-list-group.html",**context)

@main.route("/ui-media-object")
def ui_media_object():
    context={
        "page_title":"Media Object"
    }
    return render_template("w3admin/bootstrap/ui-media-object.html",**context)

@main.route("/ui-card")
def ui_card():
    context={
        "page_title":"Card"
    }
    return render_template("w3admin/bootstrap/ui-card.html",**context)

@main.route("/ui-carousel")
def ui_carousel():
    context={
        "page_title":"Carousel"
    }
    return render_template("w3admin/bootstrap/ui-carousel.html",**context)

@main.route("/ui-dropdown")
def ui_dropdown():
    context={
        "page_title":"Dropdown"
    }
    return render_template("w3admin/bootstrap/ui-dropdown.html",**context)

@main.route("/ui-popover")
def ui_popover():
    context={
        "page_title":"Popover"
    }
    return render_template("w3admin/bootstrap/ui-popover.html",**context)

@main.route("/ui-progressbar")
def ui_progressbar():
    context={
        "page_title":"Progressbar"
    }
    return render_template("w3admin/bootstrap/ui-progressbar.html",**context)

@main.route("/ui-tab")
def ui_tab():
    context={
        "page_title":"Tab"
    }
    return render_template("w3admin/bootstrap/ui-tab.html",**context)

@main.route("/ui-typography")
def ui_typography():
    context={
        "page_title":"Typography"
    }
    return render_template("w3admin/bootstrap/ui-typography.html",**context)

@main.route("/ui-pagination")
def ui_pagination():
    context={
        "page_title":"Pagination"
    }
    return render_template("w3admin/bootstrap/ui-pagination.html",**context)

@main.route("/ui-grid")
def ui_grid():
    context={
        "page_title":"Grid"
    }
    return render_template("w3admin/bootstrap/ui-grid.html",**context)



@main.route("/uc-select2")
def uc_select2():
    context={
        "page_title":"Select"
    }
    return render_template("w3admin/plugins/uc-select2.html",**context)

@main.route("/uc-nestable")
def uc_nestable():
    context={
        "page_title":"Nestable"
    }
    return render_template("w3admin/plugins/uc-nestable.html",**context)

@main.route("/uc-noui-slider")
def uc_noui_slider():
    context={
        "page_title":"UI Slider"
    }
    return render_template("w3admin/plugins/uc-noui-slider.html",**context)

@main.route("/uc-sweetalert")
def uc_sweetalert():
    context={
        "page_title":"Sweet Alert"
    }
    return render_template("w3admin/plugins/uc-sweetalert.html",**context)

@main.route("/uc-toastr")
def uc_toastr():
    context={
        "page_title":"Toastr"
    }
    return render_template("w3admin/plugins/uc-toastr.html",**context)

@main.route("/map-jqvmap")
def map_jqvmap():
    context={
        "page_title":"Jqvmap"
    }
    return render_template("w3admin/plugins/map-jqvmap.html",**context)

@main.route("/uc-lightgallery")
def uc_lightgallery():
    context={
        "page_title":"LightGallery"
    }
    return render_template("w3admin/plugins/uc-lightgallery.html",**context)

@main.route("/widget-basic")
def widget_basic():
    context={
        "page_title":"Widget"
    }
    return render_template("w3admin/widget-basic.html",**context)

@main.route("/form-element")
def form_element():
    context={
        "page_title":"Form Element"
    }
    return render_template("w3admin/forms/form-element.html",**context)

@main.route("/form-wizard")
def form_wizard():
    context={
        "page_title":"Form Wizard"
    }
    return render_template("w3admin/forms/form-wizard.html",**context)

@main.route("/form-editor")
def form_editor():
    context={
        "page_title":"CkEditor"
    }
    return render_template("w3admin/forms/form-editor.html",**context)

@main.route("/form-pickers")
def form_pickers():
    context={
        "page_title":"Pickers"
    }
    return render_template("w3admin/forms/form-pickers.html",**context)

@main.route("/form-validation")
def form_validation():
    context={
        "page_title":"Form Validation"
    }
    return render_template("w3admin/forms/form-validation.html",**context)

@main.route("/table-bootstrap-basic")
def table_bootstrap_basic():
    context={
        "page_title":"Table Bootstrap"
    }
    return render_template("w3admin/table/table-bootstrap-basic.html",**context)

@main.route("/table-datatable-basic")
def table_datatable_basic():
    context={
        "page_title":"Table Datatable"
    }
    return render_template("w3admin/table/table-datatable-basic.html",**context)


@main.route("/page-register")
def page_register():
    return render_template("w3admin/pages/page-register.html")

@main.route("/page-login")
def page_login():
    return render_template("w3admin/pages/page-login.html")

@main.route("/page-forgot-password")
def page_forgot_password():
    return render_template("w3admin/pages/page-forgot-password.html")

@main.route("/page-lock-screen")
def page_lock_screen():
    return render_template("w3admin/pages/page-lock-screen.html")

@main.route("/page-empty")
def page_empty():
    context={
        "page_title":"Empty Page"
    }
    return render_template("w3admin/pages/page-empty.html",**context)

@main.route("/page-error-400")
def page_error_400():
    return render_template("400.html")

@main.route("/page-error-403")    
def page_error_403():
    return render_template("403.html")

@main.errorhandler(404)
@main.route("/page-error-404")
def page_error_404():
    return render_template("404.html"), 404

@main.route("/page-error-500")
def page_error_500():
    return render_template("500.html")

@main.route("/page-error-503")
def page_error_503():
    return render_template("503.html")



