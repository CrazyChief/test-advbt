(function() {
    $(document).ready(function() {
        // box_operation();
        fancyboxs();
        // owlCarousel();
        // form();
        // click();
    });
    $('body').addClass("viewing-page-1");
    $(window).scroll(function() {
        if ($(this).scrollTop() > 2) {
            $('body').removeClass("viewing-page-1");
            $('.bar-menu').removeClass("sticky");
        } else {
            $('body').addClass("viewing-page-1");
            $('.bar-menu').removeClass("sticky");
        }
    });


   /* var value_currency_1 = $('.wmcs_currency_switcher_dropdown > *:nth-child(1)').attr('value');
    var value_currency_2 = $('.wmcs_currency_switcher_dropdown > *:nth-child(2)').attr('value');

    var text_currency_1 = $('.wmcs_currency_switcher_dropdown > *:nth-child(1)').text();
    var text_currency_2 = $('.wmcs_currency_switcher_dropdown > *:nth-child(2)').text();

    $('.currency').html('<span>'++'</span><div>'++'</div>')*/


    var window_outerwidth = $(window).outerWidth();
    /**********************************************************************************/
    // function box_operation() {
    //     var main_outerwidth = $(window).outerWidth();
    //     var body_height = $(window).outerHeight();
    //     var footer_outerHeight = $('.footer').outerHeight();
    //     if (main_outerwidth > 991) {
    //         var new_footer = $('body.js .footer').html();
    //         $('body.js #new-footer').html(new_footer).addClass('footer');
    //         var all_corect = body_height - footer_outerHeight;
    //         $('.height-2').attr('style', 'min-height:' + all_corect + 'px');
    //     }
    //     $('ul.filter > li').addClass('item');
    //     var container_outerwidth = $('.sector.product .container').outerWidth();
    //     // var window_outerwidth = $(window).outerWidth();
    //     $('.owl1').outerWidth(container_outerwidth - 30);
    //     var window_outerHeight = $(window).outerHeight();
    //     $('body.js .header, .woocomerce .header').outerHeight(window_outerHeight);
    //     var body_Height = $('body').outerHeight();
    //     var body_offset_left = $('.logo').offset();
    //     body_offset_left = body_offset_left.left;
    //     var calc_right = body_offset_left;
    //     body_offset_left = 'width: calc(' + calc_right + 'px + 225px); height: ' + body_Height + 'px';
    //     $('.block-left-fon').attr('style', body_offset_left);
    //     var body_js_outerHeight = $(window).outerHeight();
    //     var after = 'border-width:' + body_js_outerHeight + 'px' + ' ' + body_js_outerHeight + 'px';
    //     var first_line = body_js_outerHeight / 2;
    //     first_line = first_line - 1;
    //     first_line = 'left: calc(50% + ' + first_line + 'px);';
    //     $('body.js .before-object').attr('style', first_line);
    //     $('body.js .after-object').attr('style', after);
    //     var lank = $(".language-chooser li.active a span").text();
    //     $('.rezult > span').text(lank);
    //
    //
    //     $('a[data-index], .showcoupon, .tabs.wc-tabs a, .woocommerce-remove-coupon').attr('data-href', 'off');
    //
    //     $('.filter a').attr('scroll', 'on');
    //     $('.menu-filter-min a').attr('scroll', 'on');
    //     $('.fancybox-products').attr('fancybox', 'on');
    //
    //
    //
    //     $('.tabs a').addClass('button');
    // }
    // function click() {
    //     $('.sector.blog span.btn').click(function() {
    //         $(this).addClass('active');
    //     });
    //     if (window_outerwidth > 992 ) {
    //         $('a').click(function() {
    //             var target = $(this).attr('target');
    //             var data_href = $(this).attr('data-href');
    //             var data_scroll = $(this).attr('scroll');
    //             var data_fancybox = $(this).attr('fancybox');
    //             if (target == '_blank') {
    //             } else if (data_href == 'off') {} else if (data_fancybox == 'on') {} else if (data_scroll == 'on') {
    //                 url = this.href; // + '#category-box';
    //                 setTimeout('location.href=url', 200);
    //                 this.href = 'javascript:void(0)';
    //                 var $preloader = $('#page-preloader'),
    //                     $spinner = $preloader.find('.spinner');
    //                 $spinner.fadeIn();
    //                 $preloader.delay(50).fadeIn('slow');
    //             } else {
    //                 url = this.href;
    //                 setTimeout('location.href=url', 100);
    //                 this.href = 'javascript:void(0)';
    //                 var $preloader = $('#page-preloader'),
    //                     $spinner = $preloader.find('.spinner');
    //                 $spinner.fadeIn();
    //                 $preloader.delay(50).fadeIn('slow');
    //             }
    //         });
    //     }
    //     $('.tcon1').click(function() {
    //         $('.menu-scroll').toggleClass('active');
    //         $('body').toggleClass('active-menu-scroll');
    //     });
    //     $('.tcon2').click(function() {
    //         $('.menu-filter-min.active').removeClass('active');
    //     });
    //     $('.cart').click(function() {
    //         $('.box-cart .box').toggleClass('active');
    //     });
    //     $('.rezult').click(function() {
    //         $('ul.language-chooser').toggleClass('active');
    //     });
    //     $('.filter-min span.btn').click(function() {
    //         $('.menu-filter-min').toggleClass('active');
    //     });
    // }

    // function owlCarousel() {
    //     if (window_outerwidth > 992 ) {
    //         var owl1 = $(".owl1 .products");
    //         owl1.owlCarousel({
    //             itemsCustom: [
    //                 [0, 1],
    //                 [550, 1],
    //                 [768, 2],
    //                 [992, 3],
    //                 [1200, 3],
    //                 [1370, 3],
    //                 [1490, 3]
    //             ],
    //             navigation: true
    //         });
    //         var owl2 = $(".owl2");
    //         owl2.owlCarousel({
    //             itemsCustom: [
    //                 [0, 1],
    //                 [550, 1],
    //                 [768, 1],
    //                 [992, 2],
    //                 [1200, 2],
    //                 [1370, 2],
    //                 [1490, 2]
    //             ],
    //             navigation: true
    //         });
    //     }
    //     var owl3 = $(".owl3");
    //     owl3.owlCarousel({
    //         itemsCustom: [
    //             [0, 1]
    //         ],
    //         navigation: true
    //     });
    // }
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
    //
    // function form() {
    //     $("#form-contacts").validate({
    //         rules: {
    //             sendto: {
    //                 required: true
    //             },
    //             textarea: {
    //                 required: true
    //             },
    //             name: {
    //                 required: true
    //             },
    //             email: {
    //                 required: true
    //             }
    //         },
    //         messages: {
    //             sendto: '',
    //             textarea: '',
    //             name: '',
    //             email: ''
    //         },
    //         errorPlacement: function(error, element) {},
    //         submitHandler: function(form) {
    //             var forma = $(form);
    //             $.ajax({
    //                 type: 'POST',
    //                 url: '/wp-content/themes/templebeauty/sendmessage.php',
    //                 data: forma.serialize(),
    //                 success: function(data) {
    //                     $("form").find('input,textarea').val('');
    //                     if (data == "true") {
    //                         $.fancybox.close()
    //                         $.fancybox(
    //                             '<div class="thenks-fancybox text-center" style="max-width:550px"><p class="img-text-2"><h2>' + title_form + '</h2> <p>' + text_form + '</p></p></div>', {
    //                                 'autoDimensions': false,
    //                                 'height': 'auto',
    //                                 'transitionIn': 'none',
    //                                 'transitionOut': 'none'
    //                             }
    //                         );
    //                         setTimeout("$.fancybox.close()", 4000);
    //                     }
    //                 }
    //             });
    //         },
    //         success: function() {},
    //         highlight: function(element, errorClass) {
    //             $(element).addClass('error');
    //         },
    //         unhighlight: function(element, errorClass, validClass) {
    //             $(element).removeClass('error');
    //         }
    //     });
    //     $(function() {
    //         $("[name='phone']").mask("+38 (999) 999 - 9999");
    //     });
    // }
    //
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

// function validate(form, options){
//     var setings = {
//         errorFunction:null,
//         submitFunction:null,
//         highlightFunction:null,
//         unhighlightFunction:null
//     };
//     $.extend(setings, options);
//
//     var $form = $(form);
//
//     if ($form.length && $form.attr('novalidate') === undefined) {
//         $form.on('submit', function(e) {
//             e.preventDefault();
//         });
//         $form.validate({
//             errorClass : 'errorText',
//             focusCleanup : true,
//             focusInvalid : false,
//             invalidHandler: function(event, validator) {
//                 if(typeof(setings.errorFunction) === 'function'){
//                     setings.errorFunction(form);
//                 }
//             },
//             errorPlacement: function(error, element) {
//                 error.appendTo( element.closest('.form_input'));
//             },
//             highlight: function(element, errorClass, validClass) {
//                 $(element).addClass('error');
//                 $(element).closest('.form_row').addClass('error').removeClass('valid');
//                 if( typeof(setings.highlightFunction) === 'function' ) {
//                     setings.highlightFunction(form);
//                 }
//             },
//             unhighlight: function(element, errorClass, validClass) {
//                 $(element).removeClass('error');
//                 if($(element).closest('.form_row').is('.error')){
//                     $(element).closest('.form_row').removeClass('error').addClass('valid');
//                 }
//                 if( typeof(setings.unhighlightFunction) === 'function' ) {
//                     setings.unhighlightFunction(form);
//                 }
//             },
//             submitHandler: function(form) {
//                 if( typeof(setings.submitFunction) === 'function' ) {
//                     setings.submitFunction(form);
//                 } else {
//                     $form[0].submit();
//                 }
//             }
//         });
//         $('[required]',$form).each(function(){
//             $(this).rules( "add", {
//                 required: true,
//                 messages: {
//                     required: "Вы пропустили"
//                 }
//             });
//         });
//         if($('[type="email"]',$form).length) {
//             $('[type="email"]',$form).rules( "add",
//             {
//                 messages: {
//                     email: "Невалидный email"
//                  }
//             });
//         }
//         if($('.tel-mask[required]',$form).length){
//             $('.tel-mask[required]',$form).rules("add",
//             {
//                 messages:{
//                     required:"Введите номер мобильного телефона."
//                 }
//             });
//         }
//         $('[type="password"]',$form).each(function(){
//             if($(this).is("#re_password") == true){
//                 $(this).rules("add", {
//                     minlength:3,
//                     equalTo:"#password",
//                     messages:{
//                         equalTo:"Неверный пароль.",
//                         minlength:"Недостаточно символов."
//                     }
//                 });
//             }
//         })
//     }
// }

// function validationCall(form){
//
//   var thisForm = $(form);
//   var formSur = thisForm.serialize();
//
//     $.ajax({
//         url : thisForm.attr('action'),
//         data: formSur,
//         method:'POST',
//         error: function(){
//           /*  popNext("#error-popup", "fancybox-form-error"); */
//         },
//         success : function(data){
//             if ( data.trim() == 'true') {
//                 thisForm.trigger("reset");
//                /* popNext("#call_success", "fancybox-form-error");*/
//             }
//             else {
//                thisForm.trigger('reset');
//             }
//
//         }
//     });
// }

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
    if (window.location.pathname.match(/\/products\/([0-9]+)\/([0-9]+)\//)) {
        document.getElementById("defaultOpen").click();
        if ($(".varieble-box").find(".color-description span").text() == '') {
            var wrap = $(".thumb_wrapper"),
                first = wrap.children()[0],
                title = first.childNodes[1].getAttribute("alt"),
                src = first.childNodes[1].getAttribute("src");
            var big_img_wrap = $(".owl-item"),
                big_img_a = big_img_wrap.children(),
                big_img = big_img_wrap.find("img").attr("src", src);
            big_img_a.attr("href", src);
            $(".varieble-box").find(".color-description span").text(title);
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

    $('#cart_button').on('click', function () {
        $('#cart_wrapper').fadeToggle();
    });

    // if (window.location.pathname.match(/\//)) {
    //     document.getElementById("addSubscriber").addEventListener("click", showSnackbar);
    // }

    // $('.filter-min .btn').on('click', function() {
    //     $('.filter').toggleClass('active');
    // });

    // $('.tcon2').click(function() {
    //     $('.menu-filter-min.active').removeClass('active');
    // });
    // $('.cart').click(function() {
    //     $('.box-cart .box').toggleClass('active');
    // });
    // $('.rezult').click(function() {
    //     $('ul.language-chooser').toggleClass('active');
    // });

  //   // Add smooth scrolling to all links in navbar + footer link
  // $(".navbar a, footer a[href='#myPage']").on('click', function(event) {
  //
  //  // Make sure this.hash has a value before overriding default behavior
  // if (this.hash !== "") {
  //
  //   // Prevent default anchor click behavior
  //   event.preventDefault();
  //
  //   // Store hash
  //   var hash = this.hash;
  //
  //   // Using jQuery's animate() method to add smooth page scroll
  //   // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
  //   $('html, body').animate({
  //     scrollTop: $(hash).offset().top
  //   }, 900, function(){
  //
  //     // Add hash (#) to URL when done scrolling (default click behavior)
  //     window.location.hash = hash;
  //     });
  //   } // End if
  // });
  //   $('#pagepiling').pagepiling({
  //       anchors: ['firstPage', 'secondPage', 'thirdPage', 'fourthPage', 'lastPage'],
  //       menu: '#myMenu'
  //   });



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

    $("#addToCart").on('click', function () {
        var pk = $(this).siblings("input[name='add-to-cart']").val(),
            quantity = $(this).siblings("div").find("input[name='quantity']").val();
        // console.log("PK: " + pk);
        // console.log("quantity: " + quantity);
        cart.add(pk, quantity);
        // console.log("success!");
    });

    $(".deleter button").on('click', function () {
        var bt = $(this),
            pk = bt.attr('data-product_id');
        cart.removeProd(pk);
        // console.log(pk);
    });

    $('#addSubscriber').on('click', function () {
        var emailVal = $("#subscr_email_field").val(),
            nameVal = $("#subscr_name_field").val();
        subscribers.addSubscriber(emailVal, nameVal);
    });

    // $("a[href='#comment_form']").on('click', function () {
    $("button").on('click', function () {
        if (this.id.match(/comment_reply_([0-9]+)/)) {
            var cForm = $("#comment_form"),
                pos = cForm.position();
            // console.log(this.id);
            var elem = this,
                parent_id = this.id.match(/([0-9]+)/)[0],
                parent_name = elem.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.childNodes[3].innerText;
            // console.log(parent_id);
            // console.log(parent_name);
            $('body').animate({scrollTop: pos.top}, 600); /* animating of scroll to form */
            cForm.find('input[id="id_parent"]').val(parent_id);
            $('textarea[id="id_comment"]').text("<b>" + parent_name + "</b>, ");
        }
    });

    $("button").on('click', function () {
        if (this.id.match(/question_reply_([0-9]+)/)) {
            var cForm = $("#question_form"),
                pos = cForm.position();
            // console.log(this.id);
            var elem = this,
                parent_id = this.id.match(/([0-9]+)/)[0],
                parent_name = elem.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.childNodes[3].innerText;
            // console.log(parent_id);
            // console.log(parent_name);
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
    var wrap = $(".thumb_wrapper"),
        index = $(e).attr("data-index"),
        title = $(e).attr("title"),
        item = wrap.find(".thumb_product").find("img[data-index='"+index+"']").attr("src");
    var big_img_wrap = $(".owl-item"),
        big_img_a = big_img_wrap.children().attr("href", item),
        big_img = big_img_wrap.find("img").attr("src", item);
    big_img.fadeIn(1000);
    $(".varieble-box").find(".color-description span").text(title);
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