$(document).ready(function() {
    $.extend(true, $.fn.dataTable.defaults, {
        "language": {
            "url": "/static/w3admin/vendor/datatables/lang/spanish.json"
        },
        "columnDefs": [
            { "type": "num", "targets": 0 }
        ],
        "order": [[0, "asc"]]
    });

    // $('#lista_areas').DataTable();
});



/* old config in /static/w3admin/vendor/datatables/lang/spanish.json
"paginate": {
    "first": "Primero",
    "last": "Último",
    "next": "Siguiente",
    "previous": "Anterior"
},
*/