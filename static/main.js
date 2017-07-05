(function() {
    function csrfSafeMethod(method) {
            /* these HTTP methods do not require CSRF protection */
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    $(document).ready(function() {
        fancyboxs();
    });
    $('body').addClass("viewing-page-1");
    $(window).scroll(function() {
        // if ($(this).scrollTop() > 2) {
        //     $('body').removeClass("viewing-page-1");
        //     $('.bar-menu').removeClass("sticky");
        // } else {
        //     $('body').addClass("viewing-page-1");
        //     $('.bar-menu').removeClass("sticky");
        // }
    });


    var window_outerwidth = $(window).outerWidth();
    /**********************************************************************************/
    function fancyboxs() {
        $(".fancybox-products").fancybox({
            openEffect: 'elastic',
            closeEffect: 'elastic',

            helpers: {
                title: {
                    type: 'inside'
                }
            }
        });
        /*$(".fancybox-media").fancybox({
            helpers: {
                media: true
            },
            openEffect  : 'elastic',
            closeEffect : 'elastic',
        });*/

        $(".fancybox-media").fancybox({
            openEffect  : 'none',
            closeEffect : 'none',
            helpers : {
                media : {}
            }
        });
    }
})();

function setEqualHeight(columns) {
        var tallestcolumn = 0;
        columns.each(
            function()
            {
                currentHeight = $(this).height();
                if(currentHeight > tallestcolumn)
                {
                    tallestcolumn = currentHeight;
                }
            }
        );
        columns.height(tallestcolumn);
    };
    $(window).load(function() {
        setEqualHeight($(".col.product.type-product  .title"));
    });

function openDesc(evt, descName) {
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        document.getElementById(descName).style.display = "block";
        evt.currentTarget.className += " active";
    }

$(document).ready(function(){

    /* Time */
    var d = new Date().getFullYear();
    document.getElementById('copyrightTime').innerHTML = d;
    /* !Time */

    /* Get the element with id="defaultOpen" and click on it */
    if (window.location.pathname.match(/\/products\/([0-9]+)\/([a-z]+)|([a-z]+)\-\/([0-9]+)\//)) {
        document.getElementById("defaultOpen").click();
        if ($(".varieble-box").find(".color-description span").text() == '') {
            var wrap = $(".thumb_wrapper .img_wrapper .pr_wr"),
                first = wrap.children()[0],
                title = first.childNodes[1].getAttribute("alt"),
                src = first.childNodes[1].getAttribute("src"),
                price = first.childNodes[1].getAttribute("data-price"),
                pk = first.childNodes[1].getAttribute("data-index");
            // console.log(first.childNodes[1]);
            var big_img_wrap = $(".owl-item"),
                big_img_a = big_img_wrap.children(),
                big_img = big_img_wrap.find("img").attr("src", src);
            big_img_a.attr("href", src);
            // $("input[name='add-to-cart']").attr("data-color", pk);
            $("input[name='add-to-cart']").attr("value", pk);
            $(".line-price .price .woocommerce-Price-amount > .amount").text(price);
            $(".varieble-box").find(".color-description span").text(title);
            $(".box.row div.wm span.prod_color").text(title);
        }
    }

    $('#curr_dropdown').on('click', function () {
        $('#curr_dropdown_container').toggleClass('show');
    });

    $('.tcon1').on('click', function() {
        $(this).toggleClass('tcon-transform');
        $('.menu-scroll').toggleClass('active');
        $('body').toggleClass('active-menu-scroll');
    });

    // $('#cart_button').on('click', function () {
    //     $('#cart_wrapper').fadeToggle();
    // });

    // if (window.location.pathname.match(/\//)) {
    //     document.getElementById("addSubscriber").addEventListener("click", showSnackbar);
    // }


    // function csrfSafeMethod(method) {
    //     /* these HTTP methods do not require CSRF protection */
    //     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    // }
    // $.ajaxSetup({
    //     beforeSend: function(xhr, settings) {
    //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //         }
    //     }
    // });

    $("#addToCart").on('click', function () {
        var pk = $(this).siblings("input[name='add-to-cart']").val(),
            quantity = $(this).siblings("div").find("input[name='quantity']").val(),
            color = $(this).siblings("input[name='add-to-cart']").attr("data-color");
        cart.add(pk, quantity);
    });

    $(".deleter button").on('click', function () {
        var bt = $(this),
            pk = bt.attr('data-product_id');
        cart.removeProd(pk);
    });

    $('#addSubscriber').on('click', function () {
        var emailVal = $("#subscr_email_field").val(),
            nameVal = $("#subscr_name_field").val();
        subscribers.addSubscriber(emailVal, nameVal);
    });

    $("button").on('click', function () {
        if (this.id.match(/comment_reply_([0-9]+)/)) {
            var cForm = $("#comment_form"),
                pos = cForm.position();
            var elem = this,
                parent_id = this.id.match(/([0-9]+)/)[0],
                parent_name = elem.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.childNodes[3].innerText;
            $('body').animate({scrollTop: pos.top}, 600); /* animating of scroll to form */
            cForm.find('input[id="id_parent"]').val(parent_id);
            $('textarea[id="id_comment"]').text("<b>" + parent_name + "</b>, ");
        }
    });

    $("button").on('click', function () {
        if (this.id.match(/question_reply_([0-9]+)/)) {
            var cForm = $("#question_form"),
                pos = cForm.position();
            var elem = this,
                parent_id = this.id.match(/([0-9]+)/)[0],
                parent_name = elem.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.childNodes[3].innerText;
            $('body').animate({scrollTop: pos.top}, 600); /* animating of scroll to form */
            cForm.find('input[id="id_parent"]').val(parent_id);
            $('textarea[id="id_question"]').text("<b>" + parent_name + "</b>, ");
        }
    });

    // $("#slider").slider({
    //     min: 10,
    //     max: 200,
    //     values: [ 60, 100 ],
    //     classes: {
    //         "ui-slider-handle": "advbt-slider-handle",
    //         "ui-slider": "advbt-slider",
    //         "ui-widget": "advbt-widget",
    //         "ui-slider-horizontal": "advbt-slider-horizontal",
    //         "ui-widget-content": "advbt-widget-content",
    //     }
    // });
    // $("#slider").on("change", function () {
    //     var sl = $(this),
    //         val1 = sl.slider("option", "min"),
    //         val2 = sl.slider("option", "max");
    //     console.log("Min: " + val1);
    //     console.log("Max: " + val2);
    // });

});

function showThumb(e) {
    if ($(e)[0].nodeName == 'A') {
        var all_links = $('.varieble-box').find('a');
        for (var i = 0; i < all_links.length; i++) {
            all_links[i].className = 'varieble dot';
        }
        $(e).addClass('active_link_a');
    }
    var wrap = $(".thumb_wrapper .img_wrapper .pr_wr"),
        pk = $(e).attr("data-index"),
        price = $(e).attr("data-price"),
        title = $(e).attr("title"),
        item = wrap.find(".thumb_product").find("img[data-index='"+pk+"']").attr("src");
    var big_img_wrap = $(".owl-item"),
        big_img_a = big_img_wrap.children().attr("href", item),
        big_img = big_img_wrap.find("img").attr("src", item);
    big_img.fadeIn(1000);
    // $("input[name='add-to-cart']").attr("data-color", pk);
    $("input[name='add-to-cart']").attr("value", pk);
    $(".line-price .price .woocommerce-Price-amount > .amount").text(price);
    $(".varieble-box").find(".color-description span").text(title);
    $(".box.row div.wm span.prod_color").text(title);
}

/* using jQuery */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            /* Does this cookie string begin with the name we want? */
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function incr(e) {
    var field = $(e).siblings('input'),
        pk = field.attr('data-product_id'),
        mVal = field.attr("max"),
        vl = field.val(),
        btn = $('.checkout-button');
    btn.addClass('disabled');
    if (+vl >= +mVal) {
        alert("This is the largest quantity of product you can order.");
        btn.removeClass('disabled');
    } else {
        vl++;
    }
    cart.changeQuantity(pk, vl);
}

function decr(e) {
    var field = $(e).siblings('input'),
        pk = field.attr('data-product_id'),
        vl = field.val(),
        btn = $('.checkout-button');
    btn.addClass('disabled');
    if (+vl == 1) {
        alert("This is the least quantity of product you can order.");
        btn.removeClass('disabled');
    } else {
        vl--;
    }
    cart.changeQuantity(pk, vl);
}

function showSnackbar(param) {
    var strName = "snackbar";
    if (param == true) {
        strName = strName;
    } else if (param == false) {
        strName = "error_" + strName;
    }
    var x = document.getElementById(strName);
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}