$(document).ready(function () {
    $('#table').DataTable({
        "language": {
            "url": "/static/main/js/mdb_spanish.json"
        },
        "order": [[ 0, "desc" ]]
    });
    $('.dataTables_length').addClass('bs-select');
    
});


function newReader(){
    location.href = '/main/reader/pdf/new/view';
}
function downloadPDF(filename){
    window.open("/"+BASE_POOL_PDF+"/"+filename, '_blank');
}

function downloadWord(filename){
    window.open("/"+BASE_POOL_WORD+"/"+filename, '_blank');
}

