
function display_welcome(){
    
    var title = $("<h1 class='gold'>")
    title.append(learn["Topic"])
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

    $(col1).appendTo($(row));
    $(col2).appendTo($(row));
    $(row).appendTo($("#welcome_view"));

}



$(document).ready(function(){
    display_welcome();
    console.log(learn)
    
        
    
})
