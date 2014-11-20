$(document).ready(function($) {
$("#getStringDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-string.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getCharDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-char.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getIntDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-int.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getFloatDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-float.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getBoolDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-bool.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
$("#getArrayDef").one('click', function() {
    $.ajax({
       url: "cgi-bin/basics1/basics1-array.py",
       type: "GET",
       dataType: "text",
           cache: false,
       success: function(dat) {
         console.log(dat);
         $(".definition").html('<p>' + dat + '</p>');
       },
    });
  });
});
