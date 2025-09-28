import pytest
from database import Student


def test_add_student(db_session):
    """Тест добавления студента"""
    test_user_id = 1001
    new_student = Student(
        user_id=test_user_id,
        level="Advanced",
        education_form="personal",
        subject_id=1
    )

    db_session.add(new_student)
    db_session.commit()

    student_from_db = db_session.query(Student).filter(Student.user_id == test_user_id).first()
    assert student_from_db is not None
    assert student_from_db.level == "Advanced"
    assert student_from_db.education_form == "personal"
    assert student_from_db.subject_id == 1

    db_session.query(Student).filter(Student.user_id == test_user_id).delete()
    db_session.commit()


def test_update_student(db_session):
    """Тест изменения данных студента"""
    test_user_id = 1002
    student = Student(
        user_id=test_user_id,
        level="Elementary",
        education_form="group",
        subject_id=1
    )
    db_session.add(student)
    db_session.commit()

    student_to_update = db_session.query(Student).filter(Student.user_id == test_user_id).first()
    student_to_update.level = "Upper-Intermediate"
    student_to_update.education_form = "personal"
    db_session.commit()

    updated_student = db_session.query(Student).filter(Student.user_id == test_user_id).first()
    assert updated_student.level == "Upper-Intermediate"
    assert updated_student.education_form == "personal"
    assert updated_student.subject_id == 1

    db_session.query(Student).filter(Student.user_id == test_user_id).delete()
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления студента"""
    test_user_id = 1003
    student = Student(
        user_id=test_user_id,
        level="Pre-Intermediate",
        education_form="group",
        subject_id=1
    )
    db_session.add(student)
    db_session.commit()

    student_to_delete = db_session.query(Student).filter(Student.user_id == test_user_id).first()
    db_session.delete(student_to_delete)
    db_session.commit()

    deleted_student = db_session.query(Student).filter(Student.user_id == test_user_id).first()
    assert deleted_student is None

    db_session.query(Student).filter(Student.user_id == test_user_id).delete()
    db_session.commit()
