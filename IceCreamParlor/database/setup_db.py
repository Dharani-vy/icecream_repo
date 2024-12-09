import sqlite3

def initialize_db():
    conn = sqlite3.connect('C:/Users/DHARANI/Desktop/IceCreamParlor/ice_cream_parlor.db'
)
    cursor = conn.cursor()

    # Create the tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        season TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS allergens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL)''')

    # Prepopulate some sample data
    cursor.execute("INSERT INTO flavors (name, season) VALUES ('Vanilla', 'Summer')")
    cursor.execute("INSERT INTO flavors (name, season) VALUES ('Chocolate', 'All')")
    cursor.execute("INSERT INTO flavors (name, season) VALUES ('Strawberry', 'Spring')")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
