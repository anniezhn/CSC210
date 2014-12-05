jQuery(document).ready(function ($) { 
    $( "#run" ).click(function() {
      $( "#effect" ).effect("shake", {times: 5}, 300);
    });

});