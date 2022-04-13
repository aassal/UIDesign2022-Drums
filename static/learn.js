
function display_learn(){
    
    var title = $("<h1 class='gold'>")
    title.append(learn["topic"])
    var subheading = $("<h3 class='gold'>")
    subheading.append(learn["subheading"])

    var row = $("<div class='row'>");
    var col1 = $("<div class='col-md-6 contentdiv'>");
    var col2 = $("<div class='col-md-6 contentdiv'>");

    var description = $("<p>")
    description.append(learn["body"])
    title.appendTo($("#welcome_view"));
    subheading.appendTo($("#welcome_view"));
    description.appendTo($(col1));
    
    if (learn["media"].length>0){
        if (learn["media"][0].length>0){
            var leftimg = $("<img class='img100' src='"+learn["media"][0]+"'></img>")
            leftimg.appendTo($(col1));
        }
        if (learn["media"][1].length>0){
            var rightimg = $("<img class='img100' src='"+learn["media"][1]+"'></img>")
            rightimg.appendTo($(col2));
        }
    }
    
    if (learn["body-right"].length>0){
        var rightbody = $("<p>"+learn["body-right"]+"</p>")
        rightbody.appendTo($(col2));
    }
    

    $(col1).appendTo($(row));
    if (learn["ytpos"]=='0'){
        $(col2).append('<h6 class="gold">'+learn["yttitle"]+'</h6>');
        $(col2).append(learn["ytembed"]);
    } else {
        $('#yt2').append('<h6 class="gold">'+learn["yttitle"]+'</h6>');
        $('#yt2').append(learn["ytembed"]);
    }

    $(col2).appendTo($(row));
    $(row).appendTo($("#welcome_view"));

    if (parseInt(learn["id"])>1){
        var prevlearn = $("<a href='/learn/"+(parseInt(learn["id"])-1).toString()+"' class='center btn btn-outline-warning'>Previous Page!</a>");
        $(prevlearn).appendTo($("#final"));
    }
    if (parseInt(learn["id"])<6){
        var nextlearn = $("<a href='/learn/"+(parseInt(learn["id"])+1).toString()+"' class='center btn btn-outline-warning'>Next Page!</a>");
        $(nextlearn).appendTo($("#final"));
    } else {
        var nextlearn = $("<a href='/quiz/1' class='center btn btn-outline-warning'>Start Quiz!</a>");
        $(nextlearn).appendTo($("#final"));
    }
}



$(document).ready(function(){
    display_learn();
})
