function assert(cond) {
    if (!cond) {
        alert("Something went wrong.");
        throw new Error("Something went wrong.");
    }
}

jQuery(document).ready(function ($) {
    var loadHome = function() {
        $.ajax({
        url: "main.html",
        type: "GET",
        dataType: "html",
        cache: false,
        success: function(dat) {
          $("#dynamic").html(dat);
        }
      });
    }
  /*
    // Check if the user has taken Quiz 1 yet
    var loadQuiz = function() {
    $.ajax({
    url: "cgi-bin/quiz1-display.py",
    type: "GET",
    dataType: "text",
    cache: false,
    success: function(dat){
      console.log(dat),
      $("#basics1score").append(dat);
      }
    });
  }
  */


    loadHome();
    //$("#userID").text($.cookie("user"));
    $("#userID").text(function () {
     uname = $.cookie("user"); 
     $.ajax({
        url: "cgi-bin/getName.py",
        type: "POST",
        data: { username: uname },
        dataType: "json",
        cache: false,
        success: function(dat) {
          console.dir(dat);
          //$(this).text(dat.firstName); this wasn't working for some reason
          $("#userID").text(dat.firstName);
        },
        error: function (jqXHR, errorStatus, errorString) {
          console.log(errorStatus);
          console.log(errorString);
        }
      });
    });
    $("#themeLink").attr("href", localStorage.getItem("themePath"));
    $("#themeChoice").val(localStorage.getItem("themeName"));
  	//loadQuiz();


    $("#dynamic").on("click", "#basics1", function () {
        $.ajax({
          url: "basics1.html",
          type: "GET",
          dataType: "html",
          cache: false,
          success: function(dat) {
            $("#dynamic").html(dat);
          }
        });
    });

    $("#dynamic").on("click", "#basics1-quiz", function () {
        $.ajax({
          url: "basics1-quiz.html",
          type: "GET",
          dataType: "html",
          cache: false,
          success: function(dat) {
            $("#dynamic").html(dat);
          }
        });
    });

     $("#dynamic").on("click", "#commands", function (event) {
      $.ajax({
        url: "commands.html",
        type: "GET",
        dataType: "html",
        cache: false,
        success: function(dat) {
          $("#dynamic").html(dat);
        }
      });
    });

    $("#dynamic").on("click", "#conditionals", function (event) {
      $.ajax({
        url: "conditionals.html",
        type: "GET",
        dataType: "html",
        cache: false,
        success: function(dat) {
          $("#dynamic").html(dat);
        }
      });
    });

    $("#dynamic").on("click", "#iteration", function (event) {
      $.ajax({
        url: "iteration.html",
        type: "GET",
        dataType: "html",
        cache: false,
        success: function(dat) {
          $("#dynamic").html(dat);
        }
      });
    });

    $("#deleteB").click(function (event) {
      var msg = "This will delete your account.\n\n";
      msg += "This action is permanent and cannot be undone!\n\n";
      msg += "Do you wish to delete your account?";
      return confirm(msg);
    });

    $("#themeChoice").change(function (event) {
      var path = "";
      localStorage.setItem("themeName", $(this).val());
      if ($(this).val() !== "") {
        path = "css/" + $(this).val() + ".css";
      }
      localStorage.setItem("themePath", path);
      $("#themeLink").attr("href", path);
    });

    $("#returnHome").on("click", function (event) {
      loadHome();
    });
});
