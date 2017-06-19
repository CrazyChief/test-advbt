var cart = {
    add: function (pk, quantity) {
        quantity = quantity || 1;
        return $.post(URLS.addItem, {pk: pk, quantity: quantity}, function (xhr) {
            $("a.cart span").html("");
            $("a.cart span").html(xhr['itemCount']);
            // console.log(xhr);
            $("div.wm").css({display: 'block'}).show(600);
        }, 'json');
    },

    removeProd: function (itemPK) {
        return $.post(URLS.removeItem, {pk: itemPK}, function (xhr) {
            $("a.cart span").html("");
            $("a.cart span").html(xhr['itemCount']);
            if (window.location.pathname.match(/\/cart\/$/)) {
                var bt = $('div.cart_item').find('.deleter button[data-product_id="' + itemPK + '"]'),
                    field = bt.parents('div.cart_item'),
                    totalPrice = $("div.allcost span.woocommerce-Price-amount");
                field.remove();
                totalPrice.text(xhr['totalPrice']);
            }
            if (xhr['itemCount'] == 0) {
                var wrapp = $('section.sector'),
                    blockForDelete = wrapp.find('div.row');
                blockForDelete.remove();
            }
        }, 'json');
    },

    changeQuantity: function (pk, quantity) {
        return $.post(URLS.changeQuantity, {pk: pk, quantity: quantity}, function (xhr) {
            console.log(xhr);
            var tp = +xhr['totalPrice'];
            tp = tp.toFixed(2);
            $('input[data-product_id="'+pk+'"]').val(quantity);
            $('.cart_totals .woocommerce-Price-amount').text(tp);
            $('.checkout-button').removeClass('disabled');
        }, 'json');
    },

    empty: function () {
        $.post(URLS.emptyCart, 'json');
    }
};
