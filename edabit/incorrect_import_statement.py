"""
Given a string of an incorrect import statement, return the fixed string
"""


def fix_import(import_statement_to_fix):
    fixed_import_statement = ["from", "", "import", ""]
    temp_import_statement = import_statement_to_fix.split(" ")
    fixed_import_statement[1] = temp_import_statement[3]
    fixed_import_statement[3] = temp_import_statement[1]
    fixed_import_statement_string = " ".join(fixed_import_statement)

    return fixed_import_statement_string


print(fix_import("import object from module_name"))
print(fix_import("import randint from random"))
print(fix_import("import pi from math"))
