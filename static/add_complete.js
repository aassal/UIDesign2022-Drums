function display_movie(){
    var header = $("<h1>")
    header.append("You have successfully added an item.")
    header.appendTo($("#movie_view"))
    var viewitem = $("<a class='btn btn-outline-primary sep' href='/view/"+current_id+"'>View Added Item</button>")
    viewitem.appendTo($("#movie_view"))
    var newitem = $("<a class='btn btn-outline-primary sep' href='/add'>Add a New Item</button>")
    newitem.appendTo($("#movie_view"))
}

$(document).ready(function(){
    display_movie();
})
