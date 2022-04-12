
function display_search(movie_data, search_term){
    
    var title = $("<h1>")
    title.append("Search Results for: '" + search_term + "'")
    title.appendTo($("#search_view"));
    
    if(movie_data.length==0){
        var row = $("<div class='row'>");
        var column1 = $("<div class='col-md-12'>");
        column1.append("No Results")
        column1.appendTo(row)
        $(row).appendTo($("#search_view"));
    } else {
        var row = $("<div class='row'>");
        $.each(movie_data, function(i, movie){
            var column1 = $("<div class='col-md-4 '>");
            var moviediv = $("<div class='welcomediv'>");
            $('<a>',{text: movie["title"], title: movie["title"], href: "/view/" + movie["id"]}).appendTo(moviediv);
            var img = $('<a>',{href: "/view/" + movie["id"]})
            $("<img />", { src: movie["image"], class: "img-fluid", alt: movie["alt"]}).appendTo(img);
            img.appendTo(moviediv)
            moviediv.appendTo(column1)
            column1.appendTo(row)
        })
        $(row).appendTo($("#search_view"));
    }
}


    

$(document).ready(function(){
    display_search(movie_data, search_term);
})