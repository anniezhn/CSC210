var isLeapYear = function (year) {
  year = parseInt(year) || 1900;
  if (year % 400 === 0) {
    return true;
  } else if (year % 4 === 0 && year % 100 !== 0) {
    return true;
  } else {
    return false;
  }
}

var getNumOfDays = function (month, year) {
  month = parseInt(month) || 1;
  year = parseInt(year) || 1900;
  if (month === 4 || month === 6 || month === 9 || month === 11) {
    return 30;
  }
  if (month === 2) {
    if (isLeapYear(year)) {
      return 29;
    } else {
      return 28;
    }
  }
  return 31;
}

var popYearList = function (yearList) {
  var baseYear = 1900,
      today = new Date(),
      thisYear = today.getFullYear();
  for (var i = thisYear; i >= baseYear; i--) {
    var newOpt = new Option();
    newOpt.value = i;
    newOpt.text = i.toString();
    yearList.options.add(newOpt);
  }
}

var popInitialDayList = function (dayList) {
  var maxDays = 31;
  for (var i = 1; i <= maxDays; i++) {
    var newOpt = new Option();
    newOpt.value = i;
    newOpt.text = i;
    dayList.options.add(newOpt);
  }
}

var addDay = function (dayList, day) {
  var newOpt = new Option();
  newOpt.value = day;
  newOpt.text = day;
  dayList.options.add(newOpt);
}

var updateDayList = function (dayList, month, year) {
  var oldLen = dayList.length,
      newLen = getNumOfDays(month, year) + 1;
  if (newLen < oldLen) {
    dayList.length = newLen;
  } else if (newLen > oldLen) {
    for (var i = oldLen; i < newLen; i++) {
      addDay(dayList, i);
    }
  }
}

jQuery(document).ready(function ($) {
  popInitialDayList($("#day")[0]);
  popYearList($("#year")[0]);

  $("#month").change(function () {
    updateDayList($("#day")[0], $("#month").val(), $("#year").val());
  });
  $("#year").change(function () {
    updateDayList($("#day")[0], $("#month").val(), $("#year").val());
  });
});
