var price = {
    set: function (min_price, max_price) {
        return $.post(PRURL.setPrice, {min_price: min_price, max_price: max_price}, function (xhr) {
            // console.log("min " + min_price);
            // console.log("max " + max_price);
            console.log(xhr);
        }, 'json');
    },
    reset: function () {
        return $.post(PRURL.resetPrice, {}, function (xhr) {
            console.log(xhr);
        }, 'json');
    },
};