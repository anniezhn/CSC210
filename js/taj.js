jQuery(document).ready(function ($) {
    $("#dynamic").one("click", "#basics1", function () {
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

    $("#dynamic").one("click", "#getStringDef", function() {
      $.ajax({
         url: "cgi-bin/basics1.py",
         type: "GET",
         dataType: "text",
         cache: false,
         success: function(dat) {
           console.log(dat);
           $("#string").append('<ul><li>' + dat + '</li></ul>');
         }
      });
    });

    $("#deleteB").click(function (event) {
      var msg = "This will delete your account.\n\n";
      msg += "This action is permanent and cannot be undone!\n\n";
      msg += "Do you wish to delete your account?";
      return confirm(msg);
    });
});
