$(function() {
    $('#btnLogin').click(function() {
        console.log("Loggin the muthafuckin in");
        $.ajax({
            url: '/login',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});