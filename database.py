import sqlite3

def insert_data(name,email,message):
    conn = sqlite3.connect('contact_form.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS contact(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL,
              message TEXT NOT NULL
              )""")
    c.execute("INSERT INTO contact (name, emaiL, message) VALUES (?, ?, ?)",(name, email, message))
    conn.commit()
    conn.close()
