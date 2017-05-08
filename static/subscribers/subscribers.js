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
                },
                400: function () {
                    showSnackbar(false);
                },
                403: function () {
                    showSnackbar(false);
                }
            },
        });
    },
};