var jwt;
$("#newpost").hide()

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace('-', '+').replace('_', '/');
    return JSON.parse(window.atob(base64));
};

$("#login").submit(function(event){
    event.preventDefault(); //prevent default action 
    var post_url = $(this).attr("action"); //get form action url
    var form_data = $(this).serialize(); //Encode form elements for submission
    
    $.post( post_url, form_data)
        .done(function(response){
            jwt = response.token;
            $("#jwt").val(jwt); 
            name = parseJwt(jwt).name;
            $("#login_button").html(name);
            $("#closepopup").trigger('click');
            $("#newpost").show()
        })
        .fail(function(response){
            console.log("failed to login");
        });

});

$( document ).ready(function() {
    jwt= $('#my-data').data('token');
    if(jwt){
        $("#newpost").show()
    }
});

$('[name="show_comments"]').click(function(){
    var id = $(this).val();
    $.post( "http://127.0.0.1:5001/comments", {"postId": id})
        .done(function(response){
            if (response.length != 0){
                $('#comments_value_'+id).empty();
                for (var i=0; i<response.length; i++) {
                    $('#comments_value_'+id).append("<li><b>"+response[i][0]+"</b> dit: "+ response[i][1]+"</li>");
                }
            }     
        })
        .fail(function(response){
            console.log("failed to get comments");
        });
    
    if ($('#comments_'+id).css('display') == "none"){
        $('#comments_'+id).show();
    }
    else{
        $('#comments_'+id).hide();
    }    
});

$('[name="add_comment"]').click(function(){
    if (jwt) {
        var id = $(this).val();
        var value = $('#comment_value_'+id).val();
        console.log("adding " + value+ " to comment db");
    
        $.post( "http://127.0.0.1:5001/comment", {"jwt": jwt, "PostId": id, "Value": value})
            .done(function(response){
                console.log(value+ " added to comment db");
            })
            .fail(function(response){
                console.log("failed to get comments");
            });
    } else {
        alert("user not logged in");
    }
    
});
