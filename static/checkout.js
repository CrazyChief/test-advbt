$(document).ready(function () {
    $('input[name="shipping_to_home"]').on('change', function () {
        if( $(this).is( ":checked" )  ){
            $('.last-row-hide').slideDown(300);
            // $('.hidden-part #id_shipping_departament').prop('required',true);
            // $('.hidden-part #id_shipping_city').prop('required',true);
            $('.hidden-part #id_shipping_street').prop('required',true);
            $('.hidden-part #id_shipping_home').prop('required',true);
        } else {
            $('.last-row-hide').slideUp(300);
            // $('.hidden-part #id_shipping_departament').prop('required',false);
            // $('.hidden-part #id_shipping_city').prop('required',false);
            $('.hidden-part #id_shipping_street').prop('required',false);
            $('.hidden-part #id_shipping_home').prop('required',false);
        }
    });

    $('input[name="shipping_type"]').on('change', function () {
        console.log($(this).val());
        if( $(this).val() == 'N_P' ){
            $('.hidden-part').slideDown(300);
            $('.hidden-part .main-row input').prop('required',true);
        } else {
            $('.hidden-part').slideUp(300);
            $('.hidden-part .main-row input').prop('required',false);
            if ( $('#id_pay_type_1').is(":checked") ) {
                $('#id_pay_type_1').removeProp('checked');
                $('#id_pay_type_0').prop('checked', true);

            }
        }
    });
    if($('input[name="shipping_type"]:checked').val() == 'N_P') {
        $('.hidden-part').slideDown(300);
        $('.hidden-part .main-row input').prop('required',true);
    }
    if ($('#id_shipping_to_home:checked').length) {
        $('#id_shipping_street').prop('required',true);
        $('#id_shipping_home').prop('required',true);
    } else {
        $('#id_shipping_street').prop('required',false);
        $('#id_shipping_home').prop('required',false);
    }

    if($('#id_shipping_type_1:checked').length) {
        $('#id_shipping_departament').prop('required', false);
        $('#id_shipping_city').prop('required',false);
        $('#id_pay_type_1').prop('disabled', true);
        $('#id_pay_type_1').parent('label').css('opacity', '0.4');
        $('#id_pay_type_0').prop('checked', true);
    }
    $('input[name="shipping_type"]').on('change', function() {
        if($('#id_shipping_type_1:checked').length) {
            $('#id_pay_type_1').prop('disabled', true);
            $('#id_pay_type_1').parent('label').css('opacity', '0.4');
        } else {
            $('#id_pay_type_1').prop('disabled', false);
            $('#id_pay_type_1').parent('label').css('opacity', '1');
        }
    });
});