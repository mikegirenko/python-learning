def relation_to_luke(name):
    relation = ""
    base_string = "Luke, I am your"
    person_relation_dict = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
    }
    for key, value in person_relation_dict.items():
        if key == name:
            relation = f"{base_string} {value}"
        elif key == name:
            relation = f"{base_string} {value}"
        elif key == name:
            relation = f"{base_string} {value}"
        elif key == name:
            relation = f"{base_string} {value}"
    return relation


print(relation_to_luke("Darth Vader"))
print(relation_to_luke("Leia"))
print(relation_to_luke("Han"))
print(relation_to_luke("R2D2"))
