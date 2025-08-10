import locale

# Intentar setear el locale español, con fallback si no está disponible
try:
    locale.setlocale(locale.LC_TIME, 'es_CL.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')  # Usa el locale por defecto

def format_created_at(visit_log):
    """
    Devuelve 'lun 20:33' usando la fecha de la base (ya en hora local)
    """
    return visit_log.created_at.strftime('%a %H:%M')
