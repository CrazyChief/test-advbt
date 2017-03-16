(function() {
    $(document).ready(function() {

        fancyboxs();
        transformicons.add('.tcon1');
        owlCarousel();
        form();
        click();
    });
    //$('body').addClass("viewing-page-1");
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

    function click() {
        $('.sector.blog span.btn').click(function() {
            $(this).addClass('active');
        });

        if (window_outerwidth > 992 ) {
            
            $('a').click(function() {
                var target = $(this).attr('target');
                var data_href = $(this).attr('data-href');
                var data_scroll = $(this).attr('scroll');
                var data_fancybox = $(this).attr('fancybox');
                if (target == '_blank') {
                } else if (data_href == 'off') {} else if (data_fancybox == 'on') {} else if (data_scroll == 'on') {
                    url = this.href; // + '#category-box';
                    setTimeout('location.href=url', 200);
                    this.href = 'javascript:void(0)';
                    var $preloader = $('#page-preloader'),
                        $spinner = $preloader.find('.spinner');
                    $spinner.fadeIn();
                    $preloader.delay(50).fadeIn('slow');
                } else {
                    url = this.href;
                    setTimeout('location.href=url', 100);
                    this.href = 'javascript:void(0)';
                    var $preloader = $('#page-preloader'),
                        $spinner = $preloader.find('.spinner');
                    $spinner.fadeIn();
                    $preloader.delay(50).fadeIn('slow');
                }
            });
        }
        $('.tcon1').click(function() {
            $('.menu-scroll').toggleClass('active');
            $('body').toggleClass('active-menu-scroll');
        });
        $('.tcon2').click(function() {
            $('.menu-filter-min.active').removeClass('active');
        });
        $('.cart').click(function() {
            $('.box-cart .box').toggleClass('active');
        });
        $('.rezult').click(function() {
            $('ul.language-chooser').toggleClass('active');
        });
        $('.filter-min span.btn').click(function() {
            $('.menu-filter-min').toggleClass('active');
        });
    }
    function owlCarousel() {
        
        if (window_outerwidth > 992 ) {
            var owl1 = $(".owl1 .products");
            owl1.owlCarousel({
                itemsCustom: [
                    [0, 1],
                    [550, 1],
                    [768, 2],
                    [992, 3],
                    [1200, 3],
                    [1370, 3],
                    [1490, 3]
                ],
                navigation: true
            });

            var owl2 = $(".owl2");
            owl2.owlCarousel({
                itemsCustom: [
                    [0, 1],
                    [550, 1],
                    [768, 1],
                    [992, 2],
                    [1200, 2],
                    [1370, 2],
                    [1490, 2]
                ],
                navigation: true
            });
        }
        
        
        var owl3 = $(".owl3");
        owl3.owlCarousel({
            itemsCustom: [
                [0, 1]
            ],
            navigation: true
        });
    }
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

    function form() {
        $("#form-contacts").validate({
            rules: {
                sendto: {
                    required: true
                },
                textarea: {
                    required: true
                },
                name: {
                    required: true
                },
                email: {
                    required: true
                }
            },
            messages: {
                sendto: '',
                textarea: '',
                name: '',
                email: ''
            },
            errorPlacement: function(error, element) {},
            submitHandler: function(form) {
                var forma = $(form);
                $.ajax({
                    type: 'POST',
                    url: '/wp-content/themes/templebeauty/sendmessage.php',
                    data: forma.serialize(),
                    success: function(data) {
                        $("form").find('input,textarea').val('');
                        if (data == "true") {
                            $.fancybox.close()
                            $.fancybox(
                                '<div class="thenks-fancybox text-center" style="max-width:550px"><p class="img-text-2"><h2>' + title_form + '</h2> <p>' + text_form + '</p></p></div>', {
                                    'autoDimensions': false,
                                    'height': 'auto',
                                    'transitionIn': 'none',
                                    'transitionOut': 'none'
                                }
                            );
                            setTimeout("$.fancybox.close()", 4000);
                        }
                    }
                });
            },
            success: function() {},
            highlight: function(element, errorClass) {
                $(element).addClass('error');
            },
            unhighlight: function(element, errorClass, validClass) {
                $(element).removeClass('error');
            }
        });
        $(function() {
            $("[name='phone']").mask("+38 (999) 999 - 9999");
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


function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";" ;
}

function validate(form, options){
    var setings = {
        errorFunction:null,
        submitFunction:null,
        highlightFunction:null,
        unhighlightFunction:null
    }
    $.extend(setings, options);

    var $form = $(form);

    if ($form.length && $form.attr('novalidate') === undefined) {
        $form.on('submit', function(e) {
            e.preventDefault();
        });

        $form.validate({
            errorClass : 'errorText',
            focusCleanup : true,
            focusInvalid : false,
            invalidHandler: function(event, validator) {
                if(typeof(setings.errorFunction) === 'function'){
                    setings.errorFunction(form);
                }
            },
            errorPlacement: function(error, element) {
                error.appendTo( element.closest('.form_input'));
            },
            highlight: function(element, errorClass, validClass) {
                $(element).addClass('error');
                $(element).closest('.form_row').addClass('error').removeClass('valid');
                if( typeof(setings.highlightFunction) === 'function' ) {
                    setings.highlightFunction(form);
                }
            },
            unhighlight: function(element, errorClass, validClass) {
                $(element).removeClass('error');
                if($(element).closest('.form_row').is('.error')){
                    $(element).closest('.form_row').removeClass('error').addClass('valid');
                }
                if( typeof(setings.unhighlightFunction) === 'function' ) {
                    setings.unhighlightFunction(form);
                }
            },
            submitHandler: function(form) {
                if( typeof(setings.submitFunction) === 'function' ) {
                    setings.submitFunction(form);
                } else {
                    $form[0].submit();
                }
            }
        });

        $('[required]',$form).each(function(){
            $(this).rules( "add", {
                required: true,
                messages: {
                    required: "Вы пропустили"
                }
            });
        });

        if($('[type="email"]',$form).length) {
            $('[type="email"]',$form).rules( "add",
            {
                messages: {
                    email: "Невалидный email"
                 }
            });
        }

        if($('.tel-mask[required]',$form).length){
            $('.tel-mask[required]',$form).rules("add",
            {
                messages:{
                    required:"Введите номер мобильного телефона."
                }
            });
        }

        $('[type="password"]',$form).each(function(){
            if($(this).is("#re_password") == true){
                $(this).rules("add", {
                    minlength:3,
                    equalTo:"#password",
                    messages:{
                        equalTo:"Неверный пароль.",
                        minlength:"Недостаточно символов."
                    }
                });
            }
        })
    }
}

function validationCall(form){

  var thisForm = $(form);
  var formSur = thisForm.serialize();

    $.ajax({
        url : thisForm.attr('action'),
        data: formSur,
        method:'POST',
        error: function(){
          /*  popNext("#error-popup", "fancybox-form-error"); */
        },
        success : function(data){
            if ( data.trim() == 'true') {
                thisForm.trigger("reset");
               /* popNext("#call_success", "fancybox-form-error");*/
            }
            else {
               thisForm.trigger('reset');
            }

        }
    });
}

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

    $('.stars ul li').hover(
        function(){
            var it = $(this).index();
            $(this).closest('ul').find('li').each(function(){
                
                if( $(this).index() <= it ){
                    $(this).addClass('hoverable');
                } else {
                    $(this).addClass('not-hoverable');
                }
            });

        }, function(){
            $('.stars ul li').removeClass('hoverable').removeClass('not-hoverable');
        }
    );

    $('.stars ul li').click(function(){

        var thisName = 'currMark' + $('.headrow').attr('data-postid');

        if ( true ) {
            var mark = $(this).index();
            console.log( mark );

            if (  parseInt( getCookie(thisName) ) != mark ){

                $('.stars ul li').css("pointer-events", 'none');

                var id_posta = $('.headrow').attr('data-postid');
                setCookie( thisName , mark);
                $(this).closest('ul').find('li').each(function(){
                        
                    if( $(this).index() <= mark ){
                        $(this).addClass('plus');
                    } else {
                        $(this).removeClass('plus');
                    }
                });

                $.ajax({
                    url : '/wp-admin/admin-ajax.php',
                    data: {
                        action:  'starsUpdate', 
                        post_id: id_posta, 
                        rate:    mark
                    },
                    method:'POST',
                    success : function(data){

                        $('.stars ul li').css("pointer-events", 'auto');
                    /*  if ( data.trim() == 'true') {
                            thisForm.trigger("reset");
                            popNext("#call_success", "fancybox-form-error");
                        }
                        else {
                            thisForm.trigger('reset');
                        }
                    */

                    }
                });
            }
        }
    });

    var redFlag = false ;

    $('.form-part form input').on('keyup', function(){
        if( $(this).val() != '' ){
            $(this).addClass('error');
        } else {
            $(this).removeClass('error');
        }
    });

    validate('.form-part form', {submitFunction:validationCall});

// Get the element with id="defaultOpen" and click on it
    document.getElementById("defaultOpen").click();
});