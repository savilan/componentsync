def format_ecomponent_data(ecomponent):
    """Formatea la información de un componente antes de enviarlo como JSON."""
    return {
        "id": ecomponent.id,
        "node": ecomponent.node,
        "code": ecomponent.code,
        "name": ecomponent.name,
        "description": ecomponent.description,
        "status": ecomponent.status_id,
        "is_on": ecomponent.is_on,
        "governed_by": ecomponent.goberned_by,
        "created_at": ecomponent.created_at.strftime("%Y-%m-%d %H:%M:%S") if ecomponent.created_at else None
    }