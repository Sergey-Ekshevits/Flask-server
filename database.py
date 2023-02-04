import sqlite3
def connect_db(app):
    conn=sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

 
def post_counter(db):
    cursor = db.cursor()
    record_counter = cursor.execute('SELECT count(*) AS total FROM posts').fetchone()['total']
    return record_counter   

def getAllPosts(db, page):
    cursor = db.cursor()
    if(page == None):
        page = 1
    else:
        page = int(page)
    offset = 3
    print(page * offset)
    record = cursor.execute('SELECT * FROM posts LIMIT 3 OFFSET ?', [(page - 1) * offset])
    return record.fetchall()    

def create_new_post(db, header, body):
    cursor = db.cursor()
    sqlite_insert_query = """INSERT INTO posts
                          (header,body)
                          VALUES
                          (?,?);"""

    # Close the connection
    # db.close()

    cursor.execute(sqlite_insert_query, [header, body])
    db.commit()
    # db.close()

def change_post_func(db,new_header, new_body, id):
    cursor = db.cursor()
    query = "UPDATE posts SET header = ?, body = ? WHERE id = ?"
    # id=2
    # Values to update
    values = (new_header, new_body, id)

    # Execute the update query
    cursor.execute(query, values)

    # Commit the changes
    db.commit()
    # db.close()

def delete_post(db,id):
    cursor = db.cursor()
    cursor.execute('DELETE FROM posts WHERE id=?', [id])
    db.commit()
    # cursor.execute('SELECT * FROM posts WHERE id=?', [id])
    # req=cursor.fetchone()['id']
