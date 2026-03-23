"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        # TODO 1: add an assignment for an existing student
        first_student = session.scalars(select(Student)).first()
 
        if first_student:
            new_assignment = Assignment(
                student_id=first_student.id,
                title="Homework 1",
                score=60,
            )
            session.add(new_assignment)
            session.flush()
            print(f"Created: {new_assignment!r} for {first_student.name!r}")
        else:
            print("No students found — add a student first.")

        # TODO 2: read all students
        all_students = session.scalars(select(Student)).all()
        print("\n── All students ──")
        for s in all_students:
            print(f"  {s.id}: {s.name} <{s.email}>")

        # TODO 3: read filtered + sorted students
        older_students = session.scalars(
            select(Student).where(Student.age >= 22).order_by(desc(Student.age))
        ).all()
        print("\n── Students age >= 22, sorted by age desc ──")
        for s in older_students:
            print(f"  {s.name} — age {s.age}")

        # TODO 4: read assignments with student data
        stmt = (
            select(Assignment, Student)
            .join(Student, Assignment.student_id == Student.id)
        )
        rows = session.execute(stmt).all()
        print("\n── Assignments with student names ──")
        for assignment, student in rows:
            print(f"  [{student.name}] {assignment.title!r} — score: {assignment.score}")

        session.commit()


if __name__ == "__main__":
    main()
