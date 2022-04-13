
function display_welcome(){
    
    var title = $("<h1>")
    title.append("Identifying Music Genres from Drum Patterns")
    var description = $("<p>")
    description.append("Greetings! On this site, you will be able to learn about drum patterns, and their importance in identifying musical genres.")
    title.appendTo($("#welcome_view"));
    description.appendTo($("#welcome_view"));

    var row = $("<div class='row'>");
    $(row).appendTo($("#welcome_view"));
    var playbutton = $("<button>Play!</button>");
    $(playbutton).click(finishedLoading);
    $(playbutton).appendTo($("#welcome_view"));
    $("#welcome_view").append("<br>Tempo: ")
    var tempoinput = $("<input id='tempo'>")
    $(tempoinput).val(tempo)
    $(tempoinput).appendTo($("#welcome_view"));

}



function makeGrid(height) {
    for (i=0;i<4;i++) {
        var row1 = $("<div class='row gridfont'>");
        var col1 = $("<div class='col-md-1 labels'>");
        if (i==0){
            $(col1).append("Clap");
        } else if (i==1){
            $(col1).append("OpenHat");
        } else if (i==2){
            $(col1).append("ClosedHat");
        } else {
            $(col1).append("Kick");
        }
        
        var col2 = $("<div class='col-md-11'>");
        for (j = 0; j < height/4; j++) {
            active[i*20+j]=0
            var div = $("<div>");
            $(div).addClass("square");
            $(div).attr("id",i*20+j);
            $(div).click(function() {
                $(this).toggleClass('square-2');
                id=$(this).attr('id')
                if (active[id]==0){
                    active[id]=1
                } else {
                    active[id]=0
                }
            });
            $(col2).append(div);

        }
        $(row1).append(col1);
        $(row1).append(col2);
        $('#info').append(row1);
    }
        
    
};

var active = new Array();
var clapDecode;
var audio = new Array();
var tempo = 60

$(document).ready(function(){
    display_welcome();
    makeGrid(80);
    context = new (window.AudioContext || window.webkitAudioContext)();

    requestAudio(0, '../static/Clap.ogg')
    requestAudio(1, '../static/OpenHat.ogg')
    requestAudio(2, '../static/ClosedHat.ogg')
    requestAudio(3, '../static/Kick.ogg')

    $('#tempo').change(function() {
        tempo=parseInt($('#tempo').val());
    });
    
        
    
})

function requestAudio(location, link) {
    var request = new XMLHttpRequest();
    request.open("GET", link, true);
    request.responseType = "arraybuffer";
    request.onload = function () {
        audio[location]=context.decodeAudioData(request.response)
    }
    request.send()
}

function createbuffer(promise) {
    var source = context.createBufferSource();
    promise.then(function(decodedData) {
        source.buffer = decodedData;
    });
    return source;
}




function finishedLoading() {
  var quartertime = 60/tempo
  time= context.currentTime;
  for (i = 0; i < 20; i++) {
    var tmptime = time + (i)*quartertime;
    for (j=0; j<80; j+=20){
        if (active[i+j]){
            var source = createbuffer(audio[j/20])
            source.connect(context.destination);
            source.start(tmptime);
        }
    }
  }
}