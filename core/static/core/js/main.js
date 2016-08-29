var brownfoodsManageCart = {
  urls: {
    updateCart: '/update_cart/',
    deleteMenuItem: '/remove_from_cart/'
  }
};






/**
 * prepare ajax calls
 */
brownfoods.getCookie = function (name) {
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
};
brownfoods.csrfSafeMethod = function (method) {
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};
brownfoods.prepareAjaxCalls = function () {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!brownfoods.csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", brownfoods.getCookie('csrftoken'));
      }
    }
  });
};

$(window).ready( function() {
  brownfoods.prepareAjaxCalls();
});