jQuery(document).ready(function ($) { 
    // callback function to bring a hidden box back
    function callback() {
      setTimeout(function() {
        $( "#effect" ).removeAttr( "style" ).hide().fadeIn();
      }, 1000 );
    };
 
    $( "#run" ).click(function() {
      $( "#effect" ).effect(bounce, {}, 500, callback());
      return false;
    });
  
  
  
  
});