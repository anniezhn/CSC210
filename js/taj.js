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
    loadHome();
    $("#userID").text($.cookie("user"));
    $("#themeLink").attr("href", localStorage.getItem("themePath"));
    $("#themeChoice").val(localStorage.getItem("themeName"));

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
