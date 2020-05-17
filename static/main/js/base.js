function successAlert(msg){
    $("#success-alert").find("#alert-text").html(msg);
    $("#success-alert").show();
    $("#success-alert").fadeTo(5000, 500).slideUp(200, function(){
        $(this).hide(); 
    });
}

function errorAlert(msg){
    $("#error-alert").find("#alert-text").html(msg);
    $("#error-alert").show();
    $("#error-alert").fadeTo(5000, 500).slideUp(200, function(){
        $(this).hide(); 
    });
}

function infoAlert(msg){
    $("#info-alert").find("#alert-text").html(msg);
    $("#info-alert").show();
    $("#info-alert").fadeTo(5000, 500).slideUp(200, function(){
        $(this).hide(); 
    });
}