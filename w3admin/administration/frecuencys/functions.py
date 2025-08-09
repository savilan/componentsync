def format_frecuency_data(frecuency):
    """Formatea la información de una frecuencia antes de enviarla como JSON."""
    return {
        "id": frecuency.id,
        "name": frecuency.name,
        "value": frecuency.value
    }