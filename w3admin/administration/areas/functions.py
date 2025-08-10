def format_area_data(area):
    """Formatea la información de un área antes de enviarla como JSON."""
    return {
        "id": area.id,
        "name": area.area,
        "description": area.description,
        "status": area.status_id,
        "created_at": area.created_at.strftime("%Y-%m-%d %H:%M:%S")
    }