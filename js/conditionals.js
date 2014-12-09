jQuery(document).ready(function ($) {
  sessionStorage.setItem("exercise", "1");
  $("#x1").droppable({ scope: "cond1" });
  $(".x1Choice").draggable({ scope: "cond1", containment: $("#condExercises") });
  $("#x1").on("drop", function (event, ui) {
    var compareInt = 5,
        droppedVal = parseInt(ui.draggable.text());
    $(".condResult").html("<p>Is " + droppedVal + " > " + compareInt + "?</p><p> " +
      (droppedVal > compareInt).toString() + "</p>");
    if (droppedVal > compareInt) {
      $(".nextExercise").show();
    }
  });
  $("#x1").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });
  $("#x2").droppable({ scope: "cond2" });
  $(".x2Choice").draggable({ scope: "cond2", containment: $("#condExercises") });
  $("#x2").on("drop", function (event, ui) {
    var compareInt = 25,
        droppedVal = parseInt(ui.draggable.text());
    $(".condResult").html("<p>Is !(" + droppedVal + " < " + compareInt + ")?</p><p> " +
      (!(droppedVal < compareInt)).toString() + "</p>");
    if (!(droppedVal < compareInt)) {
      $(".nextExercise").show();
    }
  });
  $("#x2").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });
  $(".nextExerciseB").on("click", function (event) {
    var current = parseInt(sessionStorage.getItem("exercise")),
        next = current + 1;
    if (next > 1 && next < 4) {
      $("#ex" + current.toString()).fadeOut(function () {
        $("#ex" + next.toString()).fadeIn();
      });
      sessionStorage.setItem("exercise", next.toString());
      $(".nextExercise").hide();
      $(".condResult").html("").hide();
    }
  });
});
