
function display_quiz(){

    if (quiz["id"]=="end"){
        display_end()
        return
    }
    
    var title = $("<h1 class='gold'>")
    title.append(quiz["question"])

    var row = $("<div class='row'>");
    var col1 = $("<div class='col-md-8 noborder'>");
    var col2 = $("<div class='col-md-4 noborder'>");
    var div1 = $("<div class='contentdiv'>");
    var div2 = $("<div class='contentdiv description'>");
    

 
    title.appendTo($("#welcome_view"));

    $(div1).append(quiz["audioembed"]);

    $(div1).appendTo($(col1));
    $(col1).appendTo($(row));
    
    var quizform = $("<form id='quiz'>")
    var questiondiv = $("<div class='btn-group' role='group'>")
    $.each(quiz["choices"], function(i, question){
        
        var choice = $('<input id="'+i+'" class="btn-check" type="radio" name="choices" value="'+i.toString()+'" autocomplete="off">')
        var label = $('<label for="'+i.toString()+'" class="gold btn btn-outline-light">'+question+'</label>')
        if (quiz["prevans"]==i.toString()){
            $(choice).attr("checked", true)
        }
        choice.appendTo(questiondiv);
        label.appendTo(questiondiv);
        
    });
    questiondiv.appendTo(quizform);
    
    
    var submitbutton = $('<input id="submitbtn" form="quiz" class="center gold btn " type="submit" value="Submit Choice">')
    if (quiz["prevans"]!="-1"){
        $(submitbutton).attr("disabled", true)
        display_answer({"submitted": quiz["prevans"], "correct": quiz["rightchoice"]})
    }
    
    $(quizform).appendTo($(div2));
    $(div2).appendTo($(col2));
    $(col2).appendTo($(row));
    $(row).appendTo($("#welcome_view"));

    var btngroup = $("<div class='center btn-group'></div>");
    if (parseInt(quiz["id"])>1){
        var prevlearn = $("<a href='/quiz/"+(parseInt(quiz["id"])-1).toString()+"' class='btn gold'><svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-left-square-fill' viewBox='0 0 16 16'> <path d='M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z'/></svg></a>");
        $(prevlearn).appendTo($(btngroup));

        $(btngroup).appendTo($("#final"));
    }
    submitbutton.appendTo($("#final"));
    if (parseInt(quiz["id"])<5){
        var nextlearn = $("<a href='/quiz/"+(parseInt(quiz["id"])+1).toString()+"' class='btn gold'><svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-right-square-fill' viewBox='0 0 16 16'> <path d='M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z'/></svg></a>");
        $(nextlearn).appendTo($(btngroup));
        $(btngroup).appendTo($("#final"));
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
