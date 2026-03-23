"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    cur.execute("SELECT COUNT(*) FROM students")
    answer_1 = cur.fetchone()[0]
    print(answer_1)

    # TODO: SELECT AVG(age) FROM students
    cur.execute("SELECT AVG(age) FROM students")
    answer_2 = cur.fetchone()[0]
    print(answer_2)
    # TODO: SELECT MIN(age), MAX(age) FROM students
    cur.execute("SELECT MIN(age), MAX(age) FROM students")
    answer_3, answer_4 = cur.fetchone()
    print(answer_3, answer_4, end = "\n")
    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    cur.execute("SELECT track, COUNT(*) FROM students GROUP BY track")
    answer_5 = cur.fetchall()
    for t, c in answer_5:
        print(f"{t}: {c}")

    conn.close()


if __name__ == "__main__":
    main()
