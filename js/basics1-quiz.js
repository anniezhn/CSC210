// Much of this code was taken from
// http://code.tutsplus.com/tutorials/build-a-spiffy-quiz-engine--net-20185
// a tutorial to make quizzes
// it was modified to our quiz/lesson

$(function(){
	var progress = $('#progress'),
    progressKeeper = $('#progressKeeper'),
	kroggy = { answers: ['c', 'b', 'd', 'a'] },
    notice = $("#notice"),
    progressWidth = 548,
    answers= kroggy.answers,
    userAnswers = [],
	answerKey = "",
    questionLength= answers.length,
    questionsStatus = $("#questionNumber"),
    questionsList = $(".question");

    function roundReloaded(num, dec) {
    var result = Math.round(num*Math.pow(10,dec))/Math.pow(10,dec);
    return result;
	}

	function judgeSkills(score) {
    var returnString;
        if (score==100) returnString = "You're a genius!"
        else if (score>90) returnString = "Outstanding, noble sir!"
        else if (score>70) returnString = "Exceeds expectations!"
        else if (score>50) returnString = "Acceptable. For a muggle."
        else if (score>35) returnString = "Well, that was poor."
        else if (score>20) returnString = "Dreadful!"
        else returnString = "Maybe you should read over the variable definitions again."
    return returnString;s
	}

	function checkAnswers() {
    var resultArr = [],
                flag = false;
    for (i=0; i<answers.length; i++) {
        if (answers[i] == userAnswers[i]) {
            flag = true;
        }
        else {
            flag = false;
        }
        resultArr.push(flag);
    }
    return resultArr;
	}

	$('.btnStart').click(function(){
   	 $(this).parents('.questionContainer').fadeOut(500, function(){
       	 $(this).next().fadeIn(500, function(){ progressKeeper.show(); });
    	});
      	   return false;
		});

	$('.btnPrev').click(function(){
        notice.hide();
    $(this).parents('.questionContainer').fadeOut(500, function(){
        $(this).prev().fadeIn(500)
    });
    progress.animate({ width: progress.width() - Math.round(progressWidth/questionLength), }, 500 );
         return false;
	});

	$('.btnNext').click(function(){
        var tempCheck = $(this).parents('.questionContainer').find('input[type=radio]:checked');
    if (tempCheck.length == 0) {
         notice.fadeIn(300);return false;
    }
         notice.hide();
    $(this).parents('.questionContainer').fadeOut(500, function(){
        $(this).next().fadeIn(500);
    });
    progress.animate({ width: progress.width() + Math.round(progressWidth/questionLength), }, 500 );
         return false;
});

$('.btnShowResult').click(function(){
	var tempCheck = $(this).parents('.questionContainer').find('input[type=radio]:checked');
	if (tempCheck.length == 0) {
    	 notice.fadeIn(300);return false;
	}
	var tempArr = $('input[type=radio]:checked');
	for (var i = 0, ii = tempArr.length; i < ii; i++) {
    	userAnswers.push(tempArr[i].getAttribute('data-key'));
		}
		progressKeeper.hide();
	var results = checkAnswers(),
              resultSet = '',
              trueCount = 0,
              answerKey = ' Answers <br />',
              score;


		for (var i = 0, ii = results.length; i < ii; i++){
    if (results[i] == true) trueCount++;
    resultSet += '<div class="resultRow"> Question #' + (i + 1) + (results[i]== true ? "<div class='correct'><span>Correct</span></div>": "<div class='wrong'><span>Wrong</span></div>") + "</div>";
    answerKey += (i+1) +" : "+ answers[i] +' &nbsp;  &nbsp;  &nbsp;   ';
}
	score =  roundReloaded(trueCount / questionLength*100, 2);


answerKey = "<div id='answer-key'>" + answerKey + "</div>";
resultSet = '<h2 class="qTitle">' +judgeSkills(score) + ' You scored '+score+'%</h2>' + resultSet + answerKey;
$('#resultKeeper').html(resultSet).show();
     $(this).parents('.questionContainer').fadeOut(500, function(){
    $(this).next().fadeIn(500);
});
return false;

progressKeeper.hide();
notice.hide();
$("#main-quiz-holder input:radio").attr("checked", false);
$('.answers li input').click(function() {
    $(this).parents('.answers').children('li').removeClass("selected");
    $(this).parents('li').addClass('selected');
});

});





});
