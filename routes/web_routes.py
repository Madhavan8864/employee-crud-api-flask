from flask import Blueprint, render_template

from models.employee_model import EmployeeModel

web_bp = Blueprint(
    "web_bp",
    __name__
)


@web_bp.route("/")
def dashboard():

    employees = EmployeeModel.get_all_employees()

    total_employees = len(employees)

    active_employees = len(
        [e for e in employees if e["status"] == "Active"]
    )

    inactive_employees = len(
        [e for e in employees if e["status"] == "Inactive"]
    )

    departments = len(
        set(
            e["department"]
            for e in employees
        )
    )

    return render_template(
        "dashboard.html",
        employees=employees[:5],
        total_employees=total_employees,
        active_employees=active_employees,
        inactive_employees=inactive_employees,
        departments=departments
    )


@web_bp.route("/employees-page")
def employees_page():

    employees = EmployeeModel.get_all_employees()

    return render_template(
        "employees.html",
        employees=employees
    )


@web_bp.route("/add-employee")
def add_employee_page():

    return render_template(
        "add_employee.html"
    )


@web_bp.route("/employee/<int:id>")
def employee_details(id):

    employee = EmployeeModel.get_employee_by_id(id)

    if not employee:
        return render_template(
            "404.html"
        )

    return render_template(
        "view_employee.html",
        employee=employee
    )


@web_bp.route("/edit-employee/<int:id>")
def edit_employee(id):

    employee = EmployeeModel.get_employee_by_id(id)

    if not employee:
        return render_template(
            "404.html"
        )

    return render_template(
        "edit_employee.html",
        employee=employee
    )