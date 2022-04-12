function display_movie(movie_data){
    var edit = $("<img class='edit' alt='Edit' src='https://cdn4.iconfinder.com/data/icons/multimedia-collection-15/64/edit-pencil-edit_button-_write-draw-512.png'>");

    var submitform = $("<form id='editor' action='/view/"+ movie_data["id"] + "' method='post'>")

    var titlediv = $("<div>")
    var title = $("<input>").attr({name: 'title'}).val(movie_data["title"])
    titlediv.append("Movie Title: ")
    title.appendTo(titlediv);
    edit.clone().appendTo(titlediv);
    
    var yeardiv = $("<div>")
    var year = $("<input>").attr({name: 'year'}).val(movie_data["year"])
    yeardiv.append("Release Year: ")
    year.appendTo(yeardiv);
    edit.clone().appendTo(yeardiv);

    var scorediv = $("<div>")
    scorediv.append("Score: ")
    var score = $("<input>").attr({name: 'score'}).val(movie_data["score"])
    score.appendTo(scorediv);
    scorediv.append(" / 10 ")
    edit.clone().appendTo(scorediv);

    var imagediv = $("<div>")
    var image = $("<input>").attr({name: 'image'}).val(movie_data["image"])
    image.attr('size', $(image).val().length);
    $(imagediv).append("<span>Image: </span>");
    $(imagediv).append(image);
    var imgpreview = $("<button type='button' class='btn btn-outline-primary'>Preview</button>");
    $(imgpreview).click(function(){
        $(img).attr("src", $(image).val())
    });
    $(imagediv).append(imgpreview);
    edit.clone().appendTo(imagediv);

    var alt = $("<input>").attr({name: 'alt'}).val(movie_data["alt"])
    alt.attr('size', $(alt).val().length);
    $(imagediv).append("<br><span>Image Alt Tag: </span>");
    $(imagediv).append(alt);
    edit.clone().appendTo(imagediv);


    titlediv.appendTo(submitform);
    yeardiv.appendTo(submitform);
    scorediv.appendTo(submitform);
    imagediv.appendTo(submitform);

    var id = $("<input type='hidden' name='id' value='"+movie_data["id"]+"'>")
    id.appendTo($(submitform));

    var row = $("<div class='row bodyfont'>");
    var column1 = $("<div class='col-md-4'>");
    var img = $("<img />", { src: movie_data["image"], class: "img-fluid", alt: movie_data["alt"]});
    $(column1).append(img);
    $(row).append(column1);


    var column2 = $("<div class='col-md-8'>");
    $(column2).append("<b>Synopsis:  ");
    edit.clone().appendTo(column2);
    var synopsis = $("<textarea>").attr({name: 'summary'})
    $(synopsis).val(movie_data["summary"]);
    $(synopsis).css("width", "100%");
    $(synopsis).css("height", "50%");
    $(column2).append(synopsis);
    

    var row2 = $("<div class='row bodyfont'>");
    var starrow = $("<div class='col-md-6'>");
    var starcol = $("<div>")
    starcol.append("<b>Stars:");
    $.each(movie_data["stars"], function(i, star){
        var starlist = $("<li>")
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        starlist.append($("<input>").attr({name: 'stars'}).val(star))
        edit.clone().appendTo(starlist);
        starlist.append(deleter);
        starlist.appendTo(starcol);
    });

    var staradder = $("<button type='button' class='btn btn-outline-primary'>Add a Star</button>");
    $(staradder).click(function(){
        var starlist = $("<li>")
        starin = $("<input>").attr({name: 'stars'})
        starlist.append(starin)
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        edit.clone().appendTo(starlist);
        starlist.append(deleter)
        starlist.appendTo(starcol);
        starin.focus()
    });
    $(starrow).append(starcol);
    $(starrow).append(staradder);
    $(row2).append(starrow);

    var genrerow = $("<div class='col-md-6'>");
    var genrecol = $("<div>")
    genrecol.append("<b>Genres:")
    $.each(movie_data["genres"], function(i, genre){
        var genrelist = $("<li>")
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        genrelist.append($("<input>").attr({name: 'genres'}).val(genre))
        edit.clone().appendTo(genrelist);
        genrelist.append(deleter)
        genrelist.appendTo(genrecol);
    });

    var genreadder = $("<button type='button' class='btn btn-outline-primary'>Add a Genre</button>");
    $(genreadder).click(function(){
        var genrelist = $("<li>")
        geninput = $("<input>").attr({name: 'genres'})
        genrelist.append(geninput)
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        edit.clone().appendTo(genrelist);
        genrelist.append(deleter)
        genrelist.appendTo(genrecol);
        geninput.focus()
    });
    $(genrerow).append(genrecol);
    $(genrerow).append(genreadder);
    $(row2).append(genrerow);
    $(row2).appendTo($(column2));
    $(row).append(column2);
    $(row).appendTo($(submitform));


    

    var row3 = $("<div class='row bodyfont'>");
    var directorrow = $("<div class='col-md-4'>");
    var directorcol = $("<div>")
    directorcol.append("<b>Director(s):")
    $.each(movie_data["director"], function(i, director){
        var directorlist = $("<li>")
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        directorlist.append($("<input>").attr({name: 'director'}).val(director))
        edit.clone().appendTo(directorlist);
        directorlist.append(deleter)
        directorlist.appendTo(directorcol);
    });
    var directoradder = $("<button type='button' class='btn btn-outline-primary'>Add a Director</button>");
    $(directoradder).click(function(){
        var directorlist = $("<li>")
        dirinput = $("<input>").attr({name: 'director'})
        directorlist.append(dirinput)
        var deleter = $("<button class='btn btn-outline-warning'>x</button>");
        $(deleter).click(function(){
            $(this).parent().remove()
        });
        edit.clone().appendTo(directorlist);
        directorlist.append(deleter)
        directorlist.appendTo(directorcol);
        dirinput.focus()
    });
    $(directorrow).append(directorcol);
    $(directorrow).append(directoradder);
    $(row3).append(directorrow);
    $(row3).appendTo(submitform);

    var budgetdiv = $("<div>");
    budgetdiv.append("Budget: ");
    budgetdiv.append($("<input>").attr({name: 'budget'}).val(movie_data["budget"]));
    edit.clone().appendTo(budgetdiv);
    budgetdiv.appendTo(submitform);

    var submitter = $("<input class='btn btn-primary sep' type='submit'>");
    var discarder = $("<button id='discard' class='btn btn-danger sep' type='button'>");
    discarder.append("Discard Changes");
    $(submitter).appendTo(submitform);
    $(discarder).appendTo(submitform);
    $(submitform).appendTo($("#movie_view"));
}

$(document).ready(function(){
    display_movie(movie_data);
    $("#editor").on("submit", function () {
        var title = $("input[name='title']").val()
        if (title.trim() == "" ){
            alert("Title cannot be Blank.");
            $("input[name='title']").focus();
            return false
        }

        var year = $("input[name='year']").val()
        if (year.trim() == "" ){
            alert("Year cannot be Blank.");
            $("input[name='year']").focus();
            return false
        }
        if (isNaN(year)) {
            alert("Year must be a number.");
            $("input[name='year']").focus();
            return false
        }

        var score = $("input[name='score']").val()
        if (score.trim() == "" ){
            alert("Score cannot be Blank.");
            $("input[name='score']").focus();
            return false
        }

        if (isNaN(score)) {
            alert("Score must be a number.");
            $("input[name='score']").focus();
            return false
        }
        
        var image = $("input[name='image']").val()
        if (image.trim() == "" ){
            alert("Image cannot be Blank.");
            $("input[name='image']").focus();
            return false
        }

        var summary = $("textarea[name='summary']").val()
        if (summary.trim() == "" ){
            alert("Synopsis cannot be Blank.");
            $("textarea[name='summary']").focus();
            return false
        }
        
        

        var budget = $("input[name='budget']").val()
        if (budget.trim() == "" ){
            alert("Budget cannot be Blank.");
            $("input[name='budget']").focus();
            return false
        }
        if (isNaN(budget.replace(/[$,]+/g,""))) {
            alert("Budget must be a number.");
            $("input[name='budget']").focus();
            return false
        }

        var genres = $('input[name="genres"]').map(function () {
                        return $(this).val();
                    }).get()
        if (genres.length == 0){
            alert("A Genre must be added");
            $("input[name='genres']").focus();
            return false
        }
        $.each(genres, function(i, genre){
            if (genre.trim() == "" ){
                alert("A genre cannot be Blank.");
                $("input[name='genre']").focus();
                return false
            }
        })
        var stars = $('input[name="stars"]').map(function () {
            return $(this).val();
        }).get()
        if (stars.length == 0){
            alert("A star must be added");
            $("input[name='stars']").focus();
            return false
        }
        $.each(stars, function(i, star){
            if (star.trim() == "" ){
                alert("A star cannot be Blank.");
                $("input[name='stars']").focus();
                return false
            }
        })
        var director = $('input[name="director"]').map(function () {
            return $(this).val();
        }).get()
        if (director.length == 0){
            alert("A director must be added");
            $("input[name='director']").focus();
            return false
        }
        $.each(director, function(i, directors){
            if (directors.trim() == "" ){
                alert("A director cannot be Blank.");
                $("input[name='director']").focus();
                return false
            }
        })
    });
    $("#discard").on("click", function () {
        var retVal = confirm("Do you want to discard your changes?");
        if( retVal == true ) {
            $.ajax({
                success: function(result){
                    window.location.href = "/view/"+movie_data["id"];
                },
            });
        } else { 
        }
    });
})