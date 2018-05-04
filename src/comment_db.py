import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('comment.db')
     #to fill the database
    conn.execute('''CREATE TABLE COMMENT
	    (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
	    USER         TEXT     NOT NULL,
            POSTID INTEGER         NOT NULL,
            VALUE        TEXT      NOT NULL);''')
    conn.execute("INSERT INTO COMMENT(USER, POSTID, VALUE) VALUES ('Antoine', 1, 'premier commentaire')");
    conn.commit()
    print("Database successfully created")
    exit();
