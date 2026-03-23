"""Problem 01: Start with sqlite_web and create the first table.

Task:
1. Install sqlite_web:
       pip install sqlite-web
2. From lectures/06/exercises run:
       python -m sqlite_web school.db
3. Open the local sqlite_web URL in a browser.
4. In the SQL editor, create table `students` with this SQL:

   CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       age INTEGER NOT NULL,
       email TEXT UNIQUE NOT NULL,
       track TEXT NOT NULL
   );

5. Verify the table appears in the UI.

Optional:
- Insert one manual row directly in sqlite_web to verify table is writable.
"""

import sqlite3
def main() -> None:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute (
        """
        CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY,
       name TEXT NOT NULL,
       age INTEGER NOT NULL,
       email TEXT UNIQUE NOT NULL,
       track TEXT NOT NULL
   )
        """
    )
    cursor.executemany("INSERT INTO students (id, name, age, email, track) VALUES (?, ?, ?, ?, ?)", [(1, "ana", 99, "something@gmail.com", 101)])
    conn.commit()
    # TODO: run the steps from the docstring in sqlite_web.
     


if __name__ == "__main__":
    main()
