from tokenize import String
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 1

active = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
quiz_responses = [-1,-1,-1,-1,-1]
correct_responses = [1,2,1,0,3lack]

learn_data = [
    {
    "id": "1",
    "topic": "Song Analysis",
    "media": [],
    "ytpos": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "Can you tell what genre this song is from just the drums?",
    "body-right": "",
    "body": "Take a look at a this popular song's drums and analyze its beat. After identifying its characteristics, classification will be simple. At the end of the page, you can find the whole track!",
    },
    {
    "id": "2",
    "topic": "Around the World - Daft Punk",
    "media": [],
    "ytpos": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "Did you guess the genre correctly?",
    "body-right": "",
    "body": "With the full track, is the genre easier to determine? Click on the genres tab to practice.",
    },
    {
    "id": "3",
    "topic": "So What ARE Drum Patterns?",
    "media": [],
    "ytpos": "0",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "And how do we teach them?",
    "body-right": "",
    "body": "Apart from traditional musical notation, some drum patterns denote the actual note you have to hit in a grid format. This grid format reserves a row for each note on the drum, allowing for an easy way to read timings between notes.",
    },
    {
    "id": "4",
    "topic": "Hip Hop and Trap",
    "media": ["../static/hiphop.png","../static/trap.png"],
    "ytpos": "1",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Hip Hop 1_Trim.mp4" type="video/mp4"></video>', '<video width="100%" controls> <source src="../static/Trap 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "Let's Differentiate Them!",
    "body-right": "Hip Hop primarily utilizes the hi hats, with accompanying kicks to formulate their beat. An occasional snare is added in, marking the beginning of a measure. You can observe the pattern on the left side of the page.",
    "body": "Trap genres also utilize hi hats, but instead feature triplets, but with infrequent kicks. An occasional snare is present in gaps of 2-3 measures. You can observe the pattern on the right side of the page.",
    },
    {
    "id": "5",
    "topic": "Dance and Electric Dance Drums",
    "media": ["../static/dance.png","../static/edm.png"],
    "ytpos": "1",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/xLLCIEZzroI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Dance 1_Trim.mp4" type="video/mp4"></video>', '<video width="100%" controls> <source src="../static/EDM 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "Let's Differentiate Them!",
    "body-right": "Dance primarily utilizes closed hi hats to establish rhythm. The kick drum is used to establish a beat and is constant.",
    "body": "The most important part of edm (electronic dance music) is the kick drum on every beat. It feels like a heartbeat.",
    },
    {
    "id": "6",
    "topic": "Rock Drums",
    "media": ["","../static/rock.png"],
    "ytpos": "1",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/8ceiFrrHlbI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
    "audioembed": ['<video width="100%" controls> <source src="../static/Rock 1_Trim.mp4" type="video/mp4"></video>'],
    "yttitle": "Mystery Song...",
    "alt": "Drum Pattern",
    "audio": [],
    "subheading": "Let's Differentiate Them!",
    "body-right": "",
    "body": "Rock Drums almost never have two different ‘hits’ on the same beat. They will often be slower than dance and hip hop as well.",
    },
]

quiz_data = [
    {
    "id": "1",
    "question": "Determine the Genre of this Pattern.",
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
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
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
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
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
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
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
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
    "ytembed": '<iframe width="100%" height="315" src="https://www.youtube.com/embed/dwDns8x3Jb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
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
        if quiz_id == "end":
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




