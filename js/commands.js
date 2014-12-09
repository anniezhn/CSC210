jQuery(document).ready(function ($) { 
	// to save what exercise they are on
	sessionStorage.setItem("exercise", "1");
	
	// runs the first exercise, shakes the box
    $( "#run" ).click(function() {
      $( "#effect" ).effect("shake", {times: 5}, 300),
      $(".nextExercise").show();
    });

	/*// runs the second exercise, printing to screen
	$("#runProgram").submit(function() {
		var txt = $("#print").val();
		$("#output").html("<p>" + txt + "</p>");
		$(".nextExercise").show();
		});
		*/
		
	// Show the next exercise
(".nextExerciseB").on("click", function (event) {
    var current = parseInt(sessionStorage.getItem("exercise")),
        next = current + 1;
    if (next > 1 && next <= 3) {
      $("#comm" + current.toString()).fadeOut(function () {
        $("#comm" + next.toString()).fadeIn();
      });
      sessionStorage.setItem("exercise", next.toString());
      $(".nextExercise").hide();
      $(".condResult").html("").hide();
    }
  });
  
});