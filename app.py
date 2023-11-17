from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Function to connect to the database
def connect_db():
    return sqlite3.connect('posts.db')

def create_db():
# Create database
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                (postID INTEGER PRIMARY KEY AUTOINCREMENT, 
                 title TEXT, 
                 content TEXT,
              date DATETIME DEFAULT CURRENT_TIMESTAMP )''') # Add userID later
    conn.commit()

    conn.close()

# Home page - Display existing posts
@app.route('/')
def index():
    create_db()
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    print(posts)
    if posts == "None":
        flash()
    connection.close()
    return render_template('index.html', posts=posts)

# Add post form
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Add the new post to the database
        database.create_post(title, content)

        return redirect(url_for('index'))

    return render_template('createPost.html')

@app.route('/delete')
def delete():
    create_db()
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts")

    return render_template('index.html')

if __name__ == '__main__':

    app.run(debug=True)
