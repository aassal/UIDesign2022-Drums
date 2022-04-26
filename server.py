from tokenize import String
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 1

active = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
quiz_responses = [-1,-1,-1,-1,-1]
correct_responses = [1,2,1,0,3]

learn_data = [
    {
    "id": "1",
    "topic": "Song Analysis",
    "media": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "subheading": "Can you tell what genre this song is from just the drums?",
    "body": ["Take a look at a this popular song's drums and analyze its beat. After identifying its characteristics, classification will be simple. At the end of the page, you can find the whole track!"]
    },
    {
    "id": "2",
    "topic": "Around the World - Daft Punk",
    "media": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "subheading": "Did you guess the genre correctly?",
    "body-right": "",
    "body": ["With the full track, is the genre easier to determine? Click on the genres tab to practice."]
    },
    {
    "id": "3",
    "topic": "So What ARE Drum Patterns?",
    "media": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": [],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "And how do we teach them?",
    "body": ["Drum patterns are, simply put, the ordering of different ‘hits’ (when a drum is played) on a grid. Drum patterns are a useful tool for electronic musicians when creating music. Drum patterns can also be simply the order different drums are heard or played. We teach drum patterns through visualizations and the audio accompanying them."]
    },
    {
    "id": "4",
    "topic": "Hip Hop and Trap",
    "media": ['<video width="100%" controls> <source src="../static/Hip Hop 1_Trim.mp4" type="video/mp4"></video>', '<video width="100%" controls> <source src="../static/Trap 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "1",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "subheading": "Let's Differentiate Them!",
    "body": ["Trap, although a subgenre of hip hop, is very different. Trap also utilizes hi hats, but instead features triplets and ‘rolls’ (when hi hats are playing in succession very quickly), but with infrequent kicks. A snare is used in a similar way to all hip hop. Trap music is usually quicker than hip hop, broadly. You can observe the pattern on the right side of the page.", "Hip Hop primarily utilizes the hi hats, with accompanying kicks to formulate their beat. A snare is often added on three, marking the end of a measure. Hip hop has a very distinctive bounce to it. You can observe the pattern on the left side of the page."],
    },
    {
    "id": "5",
    "topic": "Dance and Electric Dance Drums",
    "media": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>','<video width="100%" controls> <source src="../static/EDM 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "1",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/xLLCIEZzroI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "subheading": "Let's Differentiate Them!",
    "body": ["Vital to EDM (electronic dance music) is the kick drum on every beat; it feels like a fast heartbeat. EDM music is usually a little faster than Dance music, but the snare and hi hat are very similar. The most important distinction is the kick drum on every beat rather than every other.", "Dance music is often in a very simple kick-hihat-snare-hihat pattern, making the thump of the kick drum on every other beat. Dance music is quicker than hip hop. It is usually around 125 beat per minute (like a slow heart beat)."]
    },
    {
    "id": "6",
    "topic": "Rock Drums",
    "media": ['<video width="100%" controls> <source src="../static/Rock 1_Trim.mp4" type="video/mp4"></video>'],
    "rows": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/8ceiFrrHlbI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "subheading": "Let's Differentiate Them!",
    "body": ["Rock Drums almost never have two different ‘hits’ (when a drum is played) on the same beat. Rock will be very distinctive in that every drum is loud, instead of just the usual kick and snare. They will often be slower than dance and hip hop as well."],
    },
]

quiz_data = [
    {
    "id": "1",
    "question": "Determine the Genre of this Pattern.",
    "audioembed": ['<video width="100%" controls> <source src="../static/EDM 2_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choices": ["Hip-Hop","EDM","Dance","Country"],
    "prevans": "-1",
    "rightchoice": "1"
    },
    {
    "id": "2",
    "question": "Determine the Genre of this Pattern.",
    "audioembed": ['<video width="100%" controls> <source src="../static/Dance 2_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choices": ["Rock","EDM","Dance","Country"],
    "prevans": "-1",
    "rightchoice": "2"
    },
    {
    "id": "3",
    "question": "Determine the Genre of this Pattern.",
    "audioembed": ['<video width="100%" controls> <source src="../static/Hip Hop 2_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choices": ["Country","Hip-Hop","EDM","Rock"],
    "prevans": "-1",
    "rightchoice": "1"
    },
    {
    "id": "4",
    "question": "Determine the Genre of this Pattern.",
    "audioembed": ['<video width="100%" controls> <source src="../static/Rock 2_Trim.mp4" type="video/mp4"></video>'], 
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choices": ["Rock","Hip-Hop","Dance","Country"],
    "prevans": "-1",
    "rightchoice": "0"
    },
    {
    "id": "5",
    "question": "Determine the Genre of this Pattern.",
    "audioembed": ['<video width="100%" controls> <source src="../static/Trap 2_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choices": ["Rock","Hip-Hop","Country","Trap"],
    "prevans": "-1",
    "rightchoice": "3"
    },
    {
    "id": "end",
    "correct": "0"
    },
]

# ROUTES

@app.route('/')
def welcome():
    return render_template('welcome.html', active=active)


@app.route('/learn/<learn_id>', methods=['GET', 'POST'])
def learn_term(learn_id):
        return render_template('learn.html', learn_id=learn_data[int(learn_id)-1])  

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz_term(quiz_id):
    if request.method == "GET": 
        correct_no=0
        if quiz_id == "end" or quiz_id == "6":
            for i in range(len(correct_responses)):
                if correct_responses[i]==quiz_responses[i]:
                    correct_no+=1
            quiz_data[-1]["correct"]=str(correct_no)
            for i in quiz_data[:-1]:
                i["prevans"]="-1"
            for i in range(len(quiz_responses)):
                quiz_responses[i]=-1
            return render_template('quiz.html', quiz_data=quiz_data[-1]) 
        return render_template('quiz.html', quiz_data=quiz_data[int(quiz_id)-1]) 
    if request.method == "POST": 
        postdata=request.form
        quiz_data[int(quiz_id)-1]["prevans"]=postdata["choices"]
        quiz_responses[int(quiz_id)-1]=int(postdata["choices"])
        return {"submitted": postdata["choices"], "correct": str(correct_responses[int(quiz_id)-1])}


# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True)




