from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 11

movie_data = [
    {
    "id": "1",
    "title": "Red Notice",
    "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2IBsC-V_4yWbxP6E-mZnylYRTYq2G1lp8_s2XMzHPxkWqmKHp",
    "alt": "Red Notice Movie Poster",
    "year": "2021",
    "summary": "Two thousand years ago, Roman general Mark Antony gifts Egyptian queen Cleopatra three bejeweled eggs as a wedding gift symbolizing his devotion. The eggs are lost to time until two are found by a farmer in 1907, but the last one remains lost. Now, an FBI profiler pursuing the world's most wanted art thief becomes his reluctant partner in crime to catch an elusive crook who's always one step ahead.",
    "director": ["Rawson Marshall Thurber"],
    "budget": "$200,000,000",
    "stars": ["Dwayne Johnson", "Ryan Reynolds", "Gal Gadot"],
    "score": "6.3",
    "genres": ["Action", "Comedy", "Thriller"]
    },
    {
    "id": "2",
    "title": "Jungle Cruise",
    "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSqaQW4u1YAq16aNu89SrxPQGABr5bu0ADuRdiN6oBy64Q1pJM1",
    "alt": "Jungle Cruise Movie Poster",
    "year": "2021",
    "summary": "Dr. Lily Houghton enlists the aid of wisecracking skipper Frank Wolff to take her down the Amazon in his ramshackle boat. Together, they search for an ancient tree that holds the power to heal -- a discovery that will change the future of medicine.",
    "director": ["Jaume Collet-Serra"],
    "budget": "$200,000,000",
    "stars": ["Dwayne Johnson", "Emily Blunt", "Edgar Ramirez"],
    "score": "6.6",
    "genres": ["Action", "Adventure", "Comedy"]
    },
    {
    "id": "3",
    "title": "Fast & Furious Presents: Hobbs & Shaw",
    "image": "https://images.moviesanywhere.com/63766f8889b39eef193ba444260d8b1b/94ef792d-94da-4844-b8fb-3feac84b45c2.jpg",
    "alt": "Fast & Furious Presents: Hobbs & Shaw Movie Poster",
    "year": "2019",
    "summary": "Brixton Lorr is a cybernetically enhanced soldier who possesses superhuman strength, a brilliant mind and a lethal pathogen that could wipe out half of the world's population. It's now up to hulking lawman Luke Hobbs and lawless operative Deckard Shaw to put aside their past differences and work together to prevent the seemingly indestructible Lorr from destroying humanity.",
    "director": ["David Leitch"],
    "budget": "$200,000,000",
    "stars": ["Dwayne Johnson", "Jason Statham", "Idris Elba"],
    "score": "6.5",
    "genres": ["Action", "Adventure", "Thriller"]
    },
    {
    "id": "4",
    "title": "The Fate of the Furious",
    "image": "https://m.media-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_.jpg",
    "alt": "The Fate of the Furious Movie Poster",
    "year": "2017",
    "summary": "With Dom and Letty married, Brian and Mia retired and the rest of the crew exonerated, the globe-trotting team has found some semblance of a normal life. They soon face an unexpected challenge when a mysterious woman named Cipher forces Dom to betray them all. Now, they must unite to bring home the man who made them a family and stop Cipher from unleashing chaos.",
    "director": ["David Leitch"],
    "budget": "$250,000,000",
    "stars": ["Dwayne Johnson", "Jason Statham", "Vin Diesel"],
    "score": "6.6",
    "genres": ["Action", "Crime", "Thriller"]
    },
    {
    "id": "5",
    "title": "Jumanji: Welcome to the Jungle",
    "image": "https://m.media-amazon.com/images/M/MV5BODQ0NDhjYWItYTMxZi00NTk2LWIzNDEtOWZiYWYxZjc2MTgxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    "alt": "Jumanji: Welcome to the Jungle Movie Poster",
    "year": "2017",
    "summary": "Four high school kids discover an old video game console and are drawn into the game's jungle setting, literally becoming the adult avatars they chose. What they discover is that you don't just play Jumanji - you must survive it. To beat the game and return to the real world, they'll have to go on the most dangerous adventure of their lives, discover what Alan Parrish left 20 years ago, and change the way they think about themselves - or they'll be stuck in the game forever.",
    "director": ["Jake Kasdan"],
    "budget": "$65,000,000",
    "stars": ["Dwayne Johnson", "Karen Gillian", "Kevin Hart"],
    "score": "6.9",
    "genres": ["Action", "Adventure", "Comedy"]
    },
    {
    "id": "6",
    "title": "Jumanji: The Next Level",
    "image": "https://m.media-amazon.com/images/M/MV5BMGM2NzY4NDUtNmE3ZS00ZTBmLWE4NDYtNTJhNDNhMjQyNDI5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
    "alt": "Jumanji: The Next Level Movie Poster",
    "year": "2019",
    "summary": "When Spencer goes back into the fantastical world of Jumanji, pals Martha, Fridge and Bethany re-enter the game to bring him home. But the game is now broken -- and fighting back. Everything the friends know about Jumanji is about to change, as they soon discover there's more obstacles and more danger to overcome.",
    "director": ["Jake Kasdan"],
    "budget": "$125,000,000",
    "stars": ["Dwayne Johnson", "Jack Black", "Kevin Hart"],
    "score": "6.7",
    "genres": ["Action", "Adventure", "Comedy"]
    },
    {
    "id": "7",
    "title": "Moana",
    "image": "https://lumiere-a.akamaihd.net/v1/images/p_moana_20530_214883e3.jpeg",
    "alt": "Moana Movie Poster",
    "year": "2016",
    "summary": "An adventurous teenager sails out on a daring mission to save her people. During her journey, Moana meets the once-mighty demigod Maui, who guides her in her quest to become a master way-finder. Together they sail across the open ocean on an action-packed voyage, encountering enormous monsters and impossible odds. Along the way, Moana fulfills the ancient quest of her ancestors and discovers the one thing she always sought: her own identity.",
    "director": ["Ron Clements", "John Musker", "Don Hall"],
    "budget": "$150,000,000",
    "stars": ["Dwayne Johnson", "Auli'i Cravalho", "Rachel House"],
    "score": "7.6",
    "genres": ["Animation", "Adventure", "Comedy"]
    },
    {
    "id": "8",
    "title": "Rampage",
    "image": "https://m.media-amazon.com/images/M/MV5BNDA1NjA3ODU3OV5BMl5BanBnXkFtZTgwOTg3MTIwNTM@._V1_FMjpg_UX1000_.jpg",
    "alt": "Rampage Movie Poster",
    "year": "2018",
    "summary": "Primatologist Davis Okoye shares an unshakable bond with George, an extraordinarily intelligent, silverback gorilla that's been in his care since birth. When a rogue genetic experiment goes wrong, it causes George, a wolf and a reptile to grow to a monstrous size. As the mutated beasts embark on a path of destruction, Okoye teams up with a discredited genetic engineer and the military to secure an antidote and prevent a global catastrophe.",
    "director": ["Brad Peyton"],
    "budget": "$120,000,000",
    "stars": ["Dwayne Johnson", "Naomie Harris", "Malin Akerman"],
    "score": "6.1",
    "genres": ["Action", "Adventure", "Sci-Fi"]
    },
    {
    "id": "9",
    "title": "Central Intelligence",
    "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR1xJWK3jVtcCpLAxKsBGwStCFdIV6zy-VoGCGvbRUKJtSyQTDD",
    "alt": "Central Intelligence Movie Poster",
    "year": "2016",
    "summary": "Bullied as a teen for being overweight, Bob Stone (Dwayne Johnson) shows up to his high school reunion looking fit and muscular. While there, he finds Calvin Joyner (Kevin Hart), a fast-talking accountant who misses his glory days as a popular athlete. Stone is now a lethal CIA agent who needs Calvin's number skills to help him save the compromised U.S. spy satellite system. Together, the former classmates encounter shootouts, espionage and double-crosses while trying to prevent worldwide chaos.",
    "director": ["Rawson Marshall Thurber"],
    "budget": "$50,000,000",
    "stars": ["Dwayne Johnson", "Kevin Hart", "Danielle Nicolet"],
    "score": "6.3",
    "genres": ["Action", "Comedy", "Crime"]
    },
    {
    "id": "10",
    "title": "Hercules",
    "image": "https://m.media-amazon.com/images/M/MV5BMTQ4ODA5MTA4OF5BMl5BanBnXkFtZTgwNjMyODM5MTE@._V1_.jpg",
    "alt": "Hercules Movie Poster",
    "year": "2014",
    "summary": "Though he is famous across the ancient world for his larger-than-life exploits, Hercules (Dwayne Johnson), the son of Zeus and a human woman, is haunted by his tragic past. Now, he fights only for gold as a traveling mercenary, accompanied by a band of loyal followers, including Amphiarus (Ian McShane) and Autolycus. However, when the benevolent ruler of Thrace and his daughter seek his help in defeating a savage warlord, Hercules must find the true hero within himself once again.",
    "director": ["Brett Ratner"],
    "budget": "$100,000,000",
    "stars": ["Dwayne Johnson", "John Hurt", "Ian McShane"],
    "score": "6.0",
    "genres": ["Action", "Adventure", "Fantasy"]
    },
]

# ROUTES

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/search_results/<search_term>')
def search_term(search_term):
    search_data=[]
    for i in range(len(movie_data)):
        if movie_data[i]["title"].lower().find(search_term.lower()) != -1:
            search_data.append(movie_data[i])
        for j in movie_data[i]["stars"]:
            if j.lower().find(search_term.lower()) != -1:
                search_data.append(movie_data[i])
        for j in movie_data[i]["genres"]:
            if j.lower().find(search_term.lower()) != -1:
                search_data.append(movie_data[i])
        for j in movie_data[i]["director"]:
            if j.lower().find(search_term.lower()) != -1:
                search_data.append(movie_data[i])
    return render_template('search.html', search_term=search_term, movie_data=search_data)

@app.route('/view/<view_id>', methods=['GET', 'POST'])
def view_term(view_id):
    if request.method == "POST":
        postdata=request.form.to_dict(flat=False)
        postdata["id"]=postdata["id"][0]
        postdata["budget"]=postdata["budget"][0]
        postdata["summary"]=postdata["summary"][0]
        postdata["year"]=postdata["year"][0]
        postdata["score"]=postdata["score"][0]
        postdata["title"]=postdata["title"][0]
        postdata["image"]=postdata["image"][0]
        dictindex=0
        for i in range(len(movie_data)):
            if movie_data[i]["id"] == view_id:
                dictindex=i
                break
        movie_data[dictindex]=postdata
        return render_template('view.html', movie_data=movie_data[dictindex])
    if request.method == "GET": 
        view_data={}
        for i in range(len(movie_data)):
            if movie_data[i]["id"] == view_id:
                view_data=movie_data[i]
                break
        return render_template('view.html', movie_data=view_data)  

@app.route('/edit/<view_id>')
def edit_term(view_id):
    view_data={}
    for i in range(len(movie_data)):
        if movie_data[i]["id"] == view_id:
            view_data=movie_data[i]
            break
    return render_template('edit.html', movie_data=view_data)  

@app.route('/add', methods=['GET', 'POST'])
def add_term():
    global current_id
    if request.method == "POST":
        
        postdata=request.form.to_dict(flat=False)
        postdata["id"]=postdata["id"][0]
        postdata["budget"]=postdata["budget"][0]
        postdata["summary"]=postdata["summary"][0]
        postdata["year"]=postdata["year"][0]
        postdata["score"]=postdata["score"][0]
        postdata["title"]=postdata["title"][0]
        postdata["image"]=postdata["image"][0]
        movie_data.append(postdata)
        current_id+=1
        return render_template('add_complete.html', current_id=(current_id-1))  
    return render_template('add.html', current_id=current_id) 

# AJAX FUNCTIONS

if __name__ == '__main__':
   app.run(debug = True)




