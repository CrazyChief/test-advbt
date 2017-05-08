var subscribers = {
    addSubscriber: function (email, name) {
        $.ajax({
            type: "POST",
            url: SUBURL.addSubscriber,
            dataType: "json",
            data: {email: email, name: name},
            statusCode: {
                200: function () {
                    showSnackbar(true);
                    $("#subscr_email_field").val('');
                    $("#subscr_name_field").val('');
                },
                400: function () {
                    showSnackbar(false);
                },
                403: function () {
                    alert("You are using incognito profile. Reload your browser to normal profile and try to type your credentials again.");
                    showSnackbar(false);
                },
            },
        });
    },
};