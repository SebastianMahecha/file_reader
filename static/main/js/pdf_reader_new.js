function listDocuments(){
    location.href = '/main/reader/pdf/view';
}

function setNameFile(element) {
    //get the file namea
    
    var fileName = $(element).val();
    //replace the "Choose a file" label
    $(element).next('.custom-file-label').html(fileName);
}