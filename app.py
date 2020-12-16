from flask import Flask, render_template,request,redirect,flash,jsonify
from flask_debugtoolbar import DebugToolbarExtension
from  random import randint,choice,sample
app=Flask(__name__)
app.config['SECRET_KEY'] = "chickenzarecool2189"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug = DebugToolbarExtension(app)

MOVIES= {'Avengers','Mummy','Spiderman'}


@app.route('/')
def home_page():
    html = """Shows homepage"""
    return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    """Redirects to new home page"""
    flash('That page has moved! This is our new home page!')
    return redirect("/") 

@app.route('/movies')
def show_all_movies():
    """Show all list of movies in fake DB"""
    return render_template('movies.html',movies=MOVIES)

@app.route('/movies/json')
def get_movies_json():
    json_obj = jsonify(list(MOVIES))
    return json_obj

@app.route('/movies/new',methods=["POST"])

def add_movie():
    
    title = request.form['title']
    #Add to pretend DB
    if title in MOVIES:
        flash('Movies Already Exists!','error')
    else:
         MOVIES.add(title)
         flash("Created Your Movie!",'success')
         
           # flash("Good choice!!")
    # return render_template('movies.html',movies=MOVIES)
    return redirect('/movies')
    


@app.route('/form')
def show_form():
    return render_template("form.html")
@app.route('/form-2')
def show_form_2():
    return render_template("form_2.html")

COMPLIMENTS = ["cool","clever","tenacious","awesome","Pythonic"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html",username=username,compliment=nice_thing)


@app.route('/greet-2')
def get_greeting_2():
    username = request.args["username"] 
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)  
    return render_template("greet_2.html",username=username,wants_compliments=wants,compliments=nice_things)

@app.route('/lucky')
def lucky_number():
    num = randint(1,10)
    return render_template('lucky.html',lucky_num=num,msg="You are so lucky!")

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html',word=caps_word)


@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template("hello.html")

@app.route('/goodbye')
def say_bye():
    """Says good bye"""
    return "GOOD BYE!!"

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p>Sorting by:{sort}</p>"
    #in address bar just after search put ? term = cat&sort =top

    #  @app.route("/post",methods=["POST"])
    #  def post_demo():
    #      return "YOU MADE A POST REQUEST"

    # @app.route("/post",methods=["GET"])
    #  def get_demo():
    #      return "YOU MADE A GET REQUEST"
                   
@app.route('/add-comment')
def add_comment_form():
     return """
     <h1>Add Comment </h1>
     <form  method="POST">
     <input type='text' placeholder='comment' name='comment'/>
     <input type='text' placeholder='username' name='username'/>
     <button>Submit</button>
        </form>
     """
@app.route('/add-comment',methods=["POST"])
def save_comment():
    comment=  request.form["comment"]
    username= request.form["username"]
    print(request.form)
    return  f"""
<h1>SAVED YOUR COMMENT</h1>
    <ul>
    <li>Username:{username}</li>
    <li>Comment:{comment}</li>
     </ul>
        """
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
 return f"<h1>Browsing The {subreddit} Subreddit</h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit,post_id):
 return f"<h1>Viewing comments for post with id:{post_id} from the {subreddit} Subreddit</h1>"


POSTS = {
1:"I like chicken tenders",
2:"I hate mayo",
3:"DOuble rainbow all the way",
4:"YOLO OMG(kill me)"

}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id,"Post not found")
    return f"<p>{post}</p>"




