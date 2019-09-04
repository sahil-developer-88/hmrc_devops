jQuery(document).ready(function() {
    // jQuery(".products_details_section").length-1
    jQuery("input[name='products_sections_count']").val(jQuery(".products_details_section").length-1)
    
    jQuery("input[name='payment_status_count']").val(jQuery(".payment_statuses").length-1)

    jQuery("#payment_status_add_btn").click(function() {
        new_payment_status_html = jQuery("#new_payment_status").html();
        jQuery(".payment_status_section").append(new_payment_status_html)
        jQuery("input[name='payment_status_count']").val(jQuery(".payment_statuses").length-1)       // update hidden field
        
        section_count = jQuery(".payment_statuses").length-2    // count for appending.
        jQuery(".payment_status_section .payment_statuses").last().children().find("input[name='payment_status']").attr("name", "payment_status_"+section_count)

        jQuery(".payment_status_section .payment_statuses").last().find("input[name='payment_status_id']").attr("name", "payment_status_id_"+section_count)   // update payment status table id on input hidden field. this field is added by clicking on + button. 
        return false
    });

    jQuery(".payment_status_section").on("click", ".item-remove", function () {
        jQuery(this).parents(".payment_statuses").remove();
        // jQuery("input[name='payment_status_count']").val(jQuery("input[name='payment_status_count']").val()-1)
        return false;
    });

    jQuery(".products_section").on("click", ".item-remove", function () {
        jQuery(this).parents(".products_details_section").remove();
        // jQuery("input[name='products_sections_count']").val(jQuery("input[name='products_sections_count']").val()-1)
        return false;
    });

    
    jQuery("#products_details_add_btn").click(function() {
        new_products_details_html = jQuery("#new_product_details").html();
        jQuery(".products_section").append(new_products_details_html)
        jQuery("input[name='products_sections_count']").val(jQuery(".products_details_section").length-1)       // update hidden field
        section_count = jQuery(".products_details_section").length-2    // count for appending.
        
        jQuery(".products_section .products_details_section").last().children().last().find('input[name="product_hidden_id"]').attr("name", "product_hidden_id_"+section_count)  // update hidden field

        jQuery(".products_section .products_details_section").last().children().last().find('input[name="description"]').attr("name","description_"+section_count)
        jQuery(".products_section .products_details_section").last().children().last().find('input[name="unit_price"]').attr("name", "unit_price_"+section_count)
        jQuery(".products_section .products_details_section").last().children().last().find('input[name="quantity"]').attr("name", "quantity_"+section_count)
        jQuery(".products_section .products_details_section").last().children().last().find('input[name="vat_rate"]').attr("name", "vat_rate_"+section_count)
        return false
    });    
})