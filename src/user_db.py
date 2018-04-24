import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('user.db')
     #to fill the database
    conn.execute('''CREATE TABLE USERS
	    (NAME TEXT PRIMARY KEY    NOT NULL,
	    PASSWORD         TEXT     NOT NULL);''')
    conn.execute("INSERT INTO USERS(NAME, PASSWORD) VALUES ('Antoine', 'ordinateur')");
    conn.execute("INSERT INTO USERS(NAME, PASSWORD) VALUES ('Gaetano', 'ordinateur')");
    conn.execute("INSERT INTO USERS(NAME, PASSWORD) VALUES ('Sylvain', 'ordinateur')");
    conn.commit()
    print("Database successfully created")
    exit();
