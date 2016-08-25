(function ($) {
 "use strict";

/*----------------------------
 jQuery MeanMenu
------------------------------ */
	jQuery('nav#dropdown').meanmenu({
		meanScreenWidth: "990",
	});	
	
/*----------------------------
 wow js active
------------------------------ */
 new WOW().init();
 
/*----------------------------
 owl active
------------------------------ */  
  $(".total-service-holder").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 1,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:[""],
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });
  $(".total-our-menu").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 3,
	  itemsCustom : [
        [0, 1],
        [450, 1],
        [480, 1],
        [600, 2],
        [700, 2],
        [768, 2],
        [992, 3],
		[1199, 3]
      ],
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:[""],
  });
  
  
  $(".total-testimonial").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });
  $(".total-menu-item").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 1,
	  navigationText:[""],
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });
  $(".reserve-slide").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:true,
	  navigation:false,	  
      items : 1,
	  navigationText:[""],
      itemsDesktop : [1199,1],
	  itemsDesktopSmall : [980,1],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });
  $(".related-blog").owlCarousel({
      autoPlay: false, 
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,	  
      items : 2,
	  navigationText:[""],
      itemsDesktop : [1199,2],
	  itemsDesktopSmall : [980,2],
	  itemsTablet: [768,1],
	  itemsMobile : [479,1],
  });

/*----------------------------
 price-slider active
------------------------------ */  
	  $( "#slider-range" ).slider({
	   range: true,
	   min: 40,
	   max: 600,
	   values: [ 60, 570 ],
	   slide: function( event, ui ) {
		$( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
	   }
	  });
	  $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
	   " - $" + $( "#slider-range" ).slider( "values", 1 ) ); 
	   
/*--------------------------
 scrollUp
---------------------------- */	
	$.scrollUp({
        scrollText: '<i class="fa fa-angle-double-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    }); 
	
	$('.time').timepicker({
		'showDuration': true,
		'timeFormat': 'g:ia'
	});

	$('.date').datepicker({
		'format': 'm/d/yyyy',
		'autoclose': true
	});	
	
    

    
$('.acc-toggle').click(function() {
    if ($('.acc-toggle input').is(':checked')) {
        $('.create-acc-body').slideDown();
    }else{
        $('.create-acc-body').slideUp();
    }
});
    
$('.ship-toggle').click(function() {
    if ($('.ship-toggle input').is(':checked')) {
        $('.ship-acc-body').slideDown();
    }else{
        $('.ship-acc-body').slideUp();
    }
});

    /*----------------------------
     sticky menu 
    ------------------------------ */
    $("#sticker").sticky({
        topSpacing: 0
    });
    
    
    /*----------------------------
     active venobox
    ------------------------------ */
	$('.venobox').venobox();
	

    
    
})(jQuery); 