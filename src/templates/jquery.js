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
            console.log(jwt);
            $("#jwt").val(jwt); 
            name = parseJwt(jwt).name;
            console.log(name);
            $("#login_button").html(name);
            $("#closepopup").trigger('click');
            $("#newpost").show()
        })
        .fail(function(response){
            console.log("failed to login");
        });

});

// $("#createpost").submit(function(event){
//     event.preventDefault(); //prevent default action 
//     var post_url = $(this).attr("action"); //get form action url
//     var form_data = $(this).serialize(); //Encode form elements for submission

//     $.post( post_url, form_data)
//         .done(function(response){
//             console.log("done");
//     })
//     .fail(function(response){
//         console.log("failed toadd");
//     });

// });

