(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 48)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  $(".main").hide()

  $(".happy").click(function() {
    $(".check-in").fadeOut();
    $(".main").fadeIn();
  });

  $(".sad").click(function() {
    $(".check-in").fadeOut();
    $(".main").fadeIn();
  });

  $(".angry").click(function() {
    $(".check-in").fadeOut();
    $(".main").fadeIn();
  });

  $(".indifferent").click(function() {
    $(".check-in").fadeOut();
    $(".main").fadeIn();
  });

  $("#remind-me-later").click(function() {
    $(".check-in").fadeOut();
    $(".main").fadeIn();
  });

})(jQuery); // End of use strict

// (function() {
//   // Helper function
//   var update_handle_track_pos;
//
//   update_handle_track_pos = function(slider, ui_handle_pos) {
//     var handle_track_xoffset, slider_range_inverse_width;
//     handle_track_xoffset = -((ui_handle_pos / 100) * slider.clientWidth);
//     $(slider).find(".handle-track").css("left", handle_track_xoffset);
//     slider_range_inverse_width = (100 - ui_handle_pos) + "%";
//     return $(slider).find(".slider-range-inverse").css("width", slider_range_inverse_width);
//   };
//
//   // Init slider
//   $("#js-slider").slider({
//     range: "min",
//     max: 100,
//     value: 50,
//     create: function(event, ui) {
//       var slider;
//       slider = $(event.target);
//
//       // Append the slider handle with a center dot and it's own track
//       slider.find('.ui-slider-handle').append('<span class="dot"><span class="handle-track"></span></span>');
//
//       // Append the slider with an inverse range
//       slider.prepend('<div class="slider-range-inverse"></div>');
//
//       // Set initial dimensions
//       slider.find(".handle-track").css("width", event.target.clientWidth);
//
//       // Set initial position for tracks
//       return update_handle_track_pos(event.target, $(this).slider("value"));
//     },
//     slide: function(event, ui) {
//       // Update position of tracks
//       return update_handle_track_pos(event.target, ui.value);
//     }
//   });
//
// }).call(this);
