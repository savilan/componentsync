def format_ecpu_data(ecpu):
    """Formatea la información de un ECPU antes de enviarlo como JSON."""
    return {
        "id": ecpu.id,
        "code": ecpu.code,
        "node": ecpu.node,
        "name": ecpu.name,
        "descrip": ecpu.descrip,
        "status_id": ecpu.status_id,
        "e_inventory_id": ecpu.e_inventory_id
    }