var cart = {
    add: function (pk, quantity) {
        quantity = quantity || 1;
        return $.post(URLS.addItem, {pk: pk, quantity: quantity}, function (xhr) {
            $("a.cart span").html("");
            $("a.cart span").html(xhr['itemCount']);
        }, 'json');
    },

    remove: function (itemPK) {
        return $.post(URLS.removeItem, {pk: itemPK}, function (xhr) {
            $("a.cart span").html("");
            $("a.cart span").html(xhr['itemCount']);
        }, 'json');
    },

    changeQuantity: function (pk, quantity) {
        return $.post(URLS.changeQuantity, {pk: pk, quantity: quantity}, 'json');
    },

    empty: function () {
        $.post(URLS.emptyCart, 'json');
    }
};
