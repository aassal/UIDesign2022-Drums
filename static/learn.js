
function display_learn(){
    
    var title = $("<h1 class='gold'>")
    title.append(learn["topic"])
    var subheading = $("<h3 class='gold'>")
    subheading.append(learn["subheading"])

    title.appendTo($("#welcome_view"));
    subheading.appendTo($("#welcome_view"));
    

    for (let i = 0; i <= parseInt(learn["rows"]); i++) {
        var row = $("<div class='row learnrows'>");
        var col1 = $("<div class='col-md-5 noborder'>");
        var col2 = $("<div class='col-md-7 noborder'>");
        var div1 = $("<div class='contentdiv'>");
        var div2 = $("<div class='contentdiv'>");
        
        var description = $("<span class='description'>")
        description.append(learn["body"][i])
        description.appendTo($(div1));
    
        var img = $("");
        
        if (learn["media"].length>0){
            if (learn["media"][i].length>0){
                img = $(learn["media"][i])
            }
        }
        
        if (i%2 == 1) {
            description.appendTo($(div2));
            img.appendTo($(div1));
            $(div2).appendTo($(col1));
            $(div1).appendTo($(col2));
            $(col2).appendTo($(row));
            $(col1).appendTo($(row));
        } else {
            description.appendTo($(div1));
            img.appendTo($(div2));
            $(div1).appendTo($(col1));
            $(div2).appendTo($(col2))
            $(col1).appendTo($(row));
            $(col2).appendTo($(row));
        }
        
        $(row).appendTo($("#welcome_view"));
    
    }

    $('#yt2').append('<h6 class="gold">'+learn["yttitle"]+'</h6>');
    $('#yt2').append(learn["ytembed"]);
    
    var btngroup = $("<div class='center btn-group'></div>");

    if (parseInt(learn["id"])>1){
        var prevlearn = $("<a href='/learn/"+(parseInt(learn["id"])-1).toString()+"' class='btn btn-outline gold'> <svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-left-square-fill' viewBox='0 0 16 16'> <path d='M16 14a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12zm-4.5-6.5H5.707l2.147-2.146a.5.5 0 1 0-.708-.708l-3 3a.5.5 0 0 0 0 .708l3 3a.5.5 0 0 0 .708-.708L5.707 8.5H11.5a.5.5 0 0 0 0-1z'/></svg></a>");
        
        $(prevlearn).appendTo($(btngroup));
        $(btngroup).appendTo($("#final"));
        
    }
    if (parseInt(learn["id"])<4){
        var nextlearn = $("<a href='/learn/"+(parseInt(learn["id"])+1).toString()+"' class='btn btn-outline gold'> <svg xmlns='http://www.w3.org/2000/svg' width='25' height='25' fill='greenyellow' class='bi bi-arrow-right-square-fill' viewBox='0 0 16 16'> <path d='M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z'/></svg></a>");
        $(nextlearn).appendTo($(btngroup));
        $(btngroup).appendTo($("#final"));
    } else {
        var nextlearn = $("<a href='/quiz/1' class='center btn btn-border gold'>Start Quiz!</a>");
        $(nextlearn).appendTo($("#final"));
    }
}



$(document).ready(function(){
    display_learn();
})
