$(document).ready(function(){
    $("#id_uif_name").blur(function(){
        var url ="http://localhost/is_user_exist/?q="+($("#id_uif_name").val()); 
        $.get(url,function(data){
            $("#username_error").text(data.error_msg);
        });
    });
});
