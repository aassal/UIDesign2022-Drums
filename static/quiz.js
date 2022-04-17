
function display_quiz(){

    if (quiz["id"]=="end"){
        display_end()
        return
    }
    
    var title = $("<h1 class='gold'>")
    title.append(quiz["question"])

    var row = $("<div class='row'>");
    var col1 = $("<div class='col-md-6 contentdiv'>");
    var col2 = $("<div class='col-md-6 contentdiv'>");

 
    title.appendTo($("#welcome_view"));


    $(col1).append('<h6 class="gold">'+quiz["yttitle"]+'</h6>');
    $(col1).append(quiz["ytembed"]);
    $(col1).append(quiz["audioembed"]);


    $(col1).appendTo($(row));
    
    var quizform = $("<form id='quiz' class='contentdiv'>")
    $.each(quiz["choices"], function(i, question){
        var questiondiv = $("<div>")
        var choice = $('<input type="radio" id="'+i+'" name="choices" value="'+i.toString()+'">')
        var label = $('<label for="'+i.toString()+'">'+question+'</label>')
        if (quiz["prevans"]==i.toString()){
            $(choice).attr("checked", true)
        }
        choice.appendTo(questiondiv);
        label.appendTo(questiondiv);
        questiondiv.appendTo(quizform);
    });
    
    var submitbutton = $('<input id="submitbtn" class="center btn btn-outline-warning" type="submit" value="Submit Choice">')
    if (quiz["prevans"]!="-1"){
        $(submitbutton).attr("disabled", true)
        display_answer({"submitted": quiz["prevans"], "correct": quiz["rightchoice"]})
    }
    submitbutton.appendTo(quizform);
    $(quizform).appendTo($(col2));
    $(col2).appendTo($(row));
    $(row).appendTo($("#welcome_view"));

    if (parseInt(quiz["id"])>1){
        var prevlearn = $("<a href='/quiz/"+(parseInt(quiz["id"])-1).toString()+"' class='center btn btn-outline-warning'>Previous Question!</a>");
        $(prevlearn).appendTo($("#final"));
    }
    if (parseInt(quiz["id"])<5){
        var nextlearn = $("<a href='/quiz/"+(parseInt(quiz["id"])+1).toString()+"' class='center btn btn-outline-warning'>Next Question!</a>");
        $(nextlearn).appendTo($("#final"));
    } else {
        var nextlearn = $("<a href='/quiz/end' class='center btn btn-outline-warning'>Submit Quiz!</a>");
        $(nextlearn).appendTo($("#final"));
    }
}

function display_end(){
    
    var title = $("<h1 class='gold'>")
    title.append("You got "+quiz["correct"]+"/5 questions right!")
    title.appendTo($("#welcome_view"));

    var review = $("<a href='/learn/1' class='center btn btn-outline-warning'>Review Again!</a>");
    $(review).appendTo($("#final"));

}

function display_answer(result){
    $("#answers").empty()
    var decision = $("<h1 class='gold'>")
    if (result["submitted"] == result["correct"]){
        decision.append("Correct Answer!")
        decision.appendTo($("#answers"))
    } else {
        decision.append("Incorrect Answer!")
        var more = $("<h3 class='gold'>")
        more.append("The correct answer was: "+quiz["choices"][parseInt(result["correct"])]+"!")
        decision.appendTo($("#answers"))
        more.appendTo($("#answers"))
    }
}

$(document).ready(function(){
    display_quiz();

    $("#quiz").on("submit", function (e) {
        console.log($(this).serialize())
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: quiz["id"],                
            data : $(this).serialize(),
            success: function(result){
                $("#submitbtn").attr("disabled", true)
                display_answer(result)
            },
            error: function(request, status, error){
            }
        });
    });
})
