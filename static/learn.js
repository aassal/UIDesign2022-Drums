
function display_learn(){
    
    var title = $("<h1 class='gold'>")
    title.append(learn["topic"])
    var subheading = $("<h3 class='gold'>")
    subheading.append(learn["subheading"])

    var row = $("<div class='row'>");
    var col1 = $("<div class='col-md-6 contentdiv'>");
    var col2 = $("<div class='col-md-6 contentdiv'>");
    var btngroup = $("<div class='center btn-group'></div>");


    var description = $("<p>")
    description.append(learn["body"])
    title.appendTo($("#welcome_view"));
    subheading.appendTo($("#welcome_view"));
    description.appendTo($(col1));
    
    if (learn["media"].length>0){
        if (learn["media"][0].length>0){
            var leftimg = $(learn["media"][0])
            leftimg.appendTo($(col1));
        }
        if (learn["media"][1].length>0){
            var rightimg = $(learn["media"][1])
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

    $('#yt2').append(learn["audioembed"]);

    $(col2).appendTo($(row));
    $(row).appendTo($("#welcome_view"));

    if (parseInt(learn["id"])>1){
        var prevlearn = $("<a href='/learn/"+(parseInt(learn["id"])-1).toString()+"' class='btn btn-outline gold'> <svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-left-square-fill' viewBox='0 0 16 16'> <path d='M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z'/></svg></a>");
        
        $(prevlearn).appendTo($(btngroup));
        $(btngroup).appendTo($("#final"));
        
    }
    if (parseInt(learn["id"])<6){
        var nextlearn = $("<a href='/learn/"+(parseInt(learn["id"])+1).toString()+"' class='btn btn-outline gold'> <svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-right-square-fill' viewBox='0 0 16 16'> <path d='M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z'/></svg></a>");
        $(nextlearn).appendTo($(btngroup));
        $(btngroup).appendTo($("#final"));
    } else {
        var nextlearn = $("<a href='/quiz/1' class='center btn btn-outline gold'>Start Quiz!</a>");
        $(nextlearn).appendTo($("#final"));
    }
}



$(document).ready(function(){
    display_learn();
})
