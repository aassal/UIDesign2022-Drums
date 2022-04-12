from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 11

learn_data = [
    {
    "id": "1",
    "Topic": "Song Analysis",
    "media": ["https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp"],
    "alt": "Drum Pattern",
    "audio": ["https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp"],
    "subheading": "Can you tell what genre this song is from just the drums?",
    "body": "Take a look at a this popular song’s drums and analyze its beat. After identifying its characteristics, classification will be simple. At the end of the page, you can find the whole track!",
    },
]

quiz_data = [
    {
    "id": "1",
    "question": "Determine the Genre of this Pattern.",
    "media": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choice1": "Hip-Hop",
    "choice2": "Rock",
    "choice3": "Dance",
    "choice4": "Country",
    "rightchoice": "1"
    },
    {
    "id": "2",
    "question": "Determine the Genre of this Pattern.",
    "media": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choice1": "Hip-Hop",
    "choice2": "Rock",
    "choice3": "Dance",
    "choice4": "Country",
    "rightchoice": "1"
    },
    {
    "id": "3",
    "question": "Determine the Genre of this Pattern.",
    "media": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choice1": "Hip-Hop",
    "choice2": "Rock",
    "choice3": "Dance",
    "choice4": "Country",
    "rightchoice": "1"
    },
    {
    "id": "4",
    "question": "Determine the Genre of this Pattern.",
    "media": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choice1": "Hip-Hop",
    "choice2": "Rock",
    "choice3": "Dance",
    "choice4": "Country",
    "rightchoice": "1"
    },
    {
    "id": "5",
    "question": "Determine the Genre of this Pattern.",
    "media": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Drum Pattern",
    "audio": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "choice1": "Hip-Hop",
    "choice2": "Rock",
    "choice3": "Dance",
    "choice4": "Country",
    "rightchoice": "1"
    },
]

# ROUTES

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/learn/<learn_id>', methods=['GET', 'POST'])
def learn_term(learn_id):
        return render_template('learn.html')  

@app.route('/quiz/<view_id>')
def quiz_term(quiz_id):
    return render_template('quiz.html')  

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True)




