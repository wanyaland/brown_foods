



$(document).ready(function() {
    $('#datepicker').Zebra_DatePicker();
 });





function cartAction(product_code) {
    quantity = $("#qty_"+product_code).val();
	jQuery.ajax({
	url: "/add_to_cart/",
	data:{'menu_id':product_code,'quantity':quantity},
	type:'post',
	dataType:'json',
	success:function(data){
	    cartHandler(data);
	},
	error:function (){}
	});
}


function remove(product_code) {
	jQuery.ajax({
	url: "/remove_from_cart/",
	data:{'menu_id':product_code},
	type:'post',
	dataType:'json',
	success:function(data){
        alert("Removed from cart!");
	},
	error:function (){}
	});
}

var cartHandler = function(data){
   var wrapper = $('.my-cart');
   var list = wrapper.find('ul');
   var added = wrapper.find('div.single-rate')
   var item = $('<li class="row"></li>');
   $('<span class="quantity">'+data.quantity+'</span>').appendTo(item);
   $('<span class="itemName">'+data.name+'</span>').appendTo(item);
   $('<span class="price">'+data.price+'</span>').appendTo(item);
   $('#sub-total').html(data.total);
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
