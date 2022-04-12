function display_movie(movie_data){
    var titlerow = $("<div class='row bodyfont'>");
    var titlecol = $("<div class='col-md-6'>");
    var title = $("<h1>")
    title.append(movie_data["title"] + " ("+movie_data["year"]+")")
    title.appendTo(titlecol);
    var scorecol = $("<div class='col-md-5'>");
    var score = $("<h2>")
    score.append("Score: " + movie_data["score"] + " / 10")
    score.appendTo(scorecol);
    var editcol = $("<div class='col-md-1'>");
    var edit = $("<a href='/edit/"+movie_data['id']+"'>")
    edit.append("<img class='editView' alt='Edit' src='https://cdn4.iconfinder.com/data/icons/multimedia-collection-15/64/edit-pencil-edit_button-_write-draw-512.png'>")
    edit.appendTo(editcol);

    
    
    titlecol.appendTo(titlerow);
    scorecol.appendTo(titlerow);
    editcol.appendTo(titlerow);
    titlerow.appendTo($("#movie_view"));
    
    var row = $("<div class='row bodyfont'>");
    var column1 = $("<div class='col-md-4'>");
    var img = $("<img />", { src: movie_data["image"], class: "img-fluid", alt: movie_data["alt"]});
    $(column1).append(img);
    $(row).append(column1);
    var column2 = $("<div class='col-md-8 contentdiv'>");
    var syndiv = $("<div>").height("50%")
    $(syndiv).append("<h3>Synopsis:</h3>");
    $(syndiv).append(movie_data["summary"]);
    $(column2).append(syndiv);
    $(column2).append("<hr class='gold'>");


    var row2 = $("<div class='row bodyfont'>");

    var starrow = $("<div class='col-md-6'>");
    starrow.append("<b>Stars:");
    $.each(movie_data["stars"], function(i, star){
        var starlist = $("<li>")
        starlist.append("<a href='/search_results/"+star+ "' class='btn btn-outline-info' role='button'>"+star+"</a>")
        starlist.appendTo(starrow);
    });
    $(row2).append(starrow);

    var genrerow = $("<div class='col-md-6'>");
    genrerow.append("<b>Genres:")
    $.each(movie_data["genres"], function(i, genre){
        var genrelist = $("<li>")
        genrelist.append("<a href='/search_results/"+genre+ "' class='btn btn-outline-info' role='button'>"+genre+"</a>")
        genrelist.appendTo(genrerow);
    });
    $(row2).append(genrerow);
    $(row2).appendTo(column2);
    $(row).append(column2);
    $(row).appendTo($("#movie_view"));

    var row3 = $("<div class='row bodyfont'>");

    var directorrow = $("<div class='col-md-4'>");
    directorrow.append("<b>Director(s):")
    $.each(movie_data["director"], function(i, director){
        var directorlist = $("<li>")
        directorlist.append("<a href='/search_results/"+director+ "' class='btn btn-outline-info' role='button'>"+director+"</a>")
        directorlist.appendTo(directorrow);
    });
    $(row3).append(directorrow);
    $(row3).appendTo($("#movie_view"));

    var budget = $("<span>")
    budget.append("Budget: " + movie_data["budget"])
    budget.appendTo($("#movie_view"));

    

    
}

$(document).ready(function(){
    display_movie(movie_data);
})