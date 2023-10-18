"""
Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a
dictionary of objects like { "name": "John", "top_note": 5 }.
"""


def return_student_names(student_info) -> dict:
    top_note = {}
    notes = student_info["notes"]
    max_note = max(notes)
    top_note["name"] = student_info["name"]
    top_note["top_note"] = max_note

    return top_note


def test_return_student_names():
    student_info = {"name": "John", "notes": [3, 5, 4]}
    assert return_student_names(student_info) == {"name": "John", "top_note": 5}

    student_info = {"name": "Max", "notes": [1, 4, 6]}
    assert return_student_names(student_info) == {"name": "Max", "top_note": 6}

    student_info = {"name": "Zygmund", "notes": [1, 2, 3]}
    assert return_student_names(student_info) == {"name": "Zygmund", "top_note": 3}


test_return_student_names()

student_info = {"name": "John", "notes": [3, 5, 4]}
print(return_student_names(student_info))
