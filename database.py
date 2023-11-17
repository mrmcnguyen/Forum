from app import *

# Create new post
def create_post(title, content):
    conn = connect_db()
    c = conn.cursor()

    # Insert post into database
    c.execute("INSERT INTO posts(title, content) VALUES (?, ?)" ,(title, content))

    conn.commit()
    conn.close()
