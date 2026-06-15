def validate_employee(data):

    required_fields = [
        "employee_code",
        "name",
        "email",
        "phone",
        "department",
        "designation",
        "salary"
    ]

    for field in required_fields:
        if field not in data:
            return False, f"{field} is required"

    return True, "Validation Passed"