jQuery(document).ready(function ($) {
  $("#x1").droppable({ scope: "cond1" });
  $(".x1Choice").draggable({ scope: "cond1", containment: $("#condExercises") });
  $("#x1").on("drop", function (event, ui) {
    var compareInt = 5,
        droppedVal = parseInt(ui.draggable.text());
    $(".condResult").html("<p>Is " + droppedVal + " > " + compareInt + "?</p><p> " +
      (droppedVal > compareInt).toString() + "</p>");
  });
  $("#x1").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });
});
