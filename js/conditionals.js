jQuery(document).ready(function ($) {
  sessionStorage.setItem("exercise", "1");

  $("#x1").droppable({ scope: "cond1" });
  $(".x1Choice").draggable({ scope: "cond1", containment: $("#condExercises") });
  $("#x1").on("drop", function (event, ui) {
    var compareInt = 5,
        droppedVal = parseInt(ui.draggable.text());
    $(".condResult").html("<p>Is " + droppedVal + " > " + compareInt + "?</p><p> " +
      (droppedVal > compareInt).toString() + "</p>").show();
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
      (!(droppedVal < compareInt)).toString() + "</p>").show();
    if (!(droppedVal < compareInt)) {
      $(".nextExercise").show();
    }
  });
  $("#x2").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });

  var droppedX3Val = 1000,
      droppedY3Val = 1000;
  $("#x3, #y3").droppable({ scope: "cond3" });
  $(".x3Choice").draggable({ scope: "cond3", containment: $("#condExercises") });
  $("#x3, #y3").on("drop", function (event, ui) {
    var compareInt = 0;
    if (this.id === "x3") {
      droppedX3Val = parseInt(ui.draggable.text());
    } else if (this.id === "y3") {
      droppedY3Val = parseInt(ui.draggable.text());
    }
    if (droppedX3Val !== 1000 && droppedY3Val !== 1000) {
      $(".condResult").html("<p>Is " + droppedX3Val + " < " + droppedY3Val + " && " +
        droppedY3Val + " < " + compareInt + "?</p>" +
        (droppedX3Val < droppedY3Val && droppedY3Val < compareInt).toString()).show();
      if (droppedX3Val < droppedY3Val && droppedY3Val < compareInt) {
        $(".nextExercise").show();
      }
    }
  });
  $("#x3, #y3").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });

  $("#x4, #y4").droppable({ scope: "cond4" });
  $(".x4Choice").draggable({ scope: "cond4", containment: $("#condExercises") });
  var droppedX4Val = -1000,
      droppedY4Val = 1000;
  $("#x4, #y4").on("drop", function (event, ui) {
    var compareXInt = 50,
        compareYInt = 0;
    if (this.id === "x4") {
      droppedX4Val = parseInt(ui.draggable.text());
    } else if (this.id === "y4") {
      droppedY4Val = parseInt(ui.draggable.text());
    }
    if (droppedX4Val !== -1000 && droppedY4Val !== 1000) {
      $(".condResult").html("<p>Is " + droppedX4Val + " > " + compareXInt + " || " +
        droppedY4Val + " < " + compareYInt + "?</p>" +
        (droppedX4Val > compareXInt || droppedY4Val < compareYInt).toString()).show();
      if (droppedX4Val > compareXInt || droppedY4Val < compareYInt) {
        $(".nextExercise").show();
      }
    }
  });
  $("#x4, #y4").on("dropout", function (event, ui) {
    $(".condResult").html("");
  });

  $(".nextExerciseB").on("click", function (event) {
    var current = parseInt(sessionStorage.getItem("exercise")),
        next = current + 1;
    if (next > 1 && next <= 5) {
      $("#ex" + current.toString()).fadeOut(function () {
        $("#ex" + next.toString()).fadeIn();
      });
      sessionStorage.setItem("exercise", next.toString());
      $(".nextExercise").hide();
      $(".condResult").html("").hide();
    }
  });
});
