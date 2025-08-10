import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_CL.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')  # Fallback

def format_created_at(visit_log):
    return visit_log.created_at.strftime('%a %H:%M')
