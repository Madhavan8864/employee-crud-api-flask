from flask import Blueprint

from controllers.employee_controller import (
    create_employee,
    get_all_employees,
    get_employee,
    update_employee,
    delete_employee
)

employee_bp = Blueprint(
    "employee_bp",
    __name__
)

employee_bp.route(
    "/employees",
    methods=["POST"]
)(create_employee)

employee_bp.route(
    "/employees",
    methods=["GET"]
)(get_all_employees)

employee_bp.route(
    "/employees/<int:emp_id>",
    methods=["GET"]
)(get_employee)

employee_bp.route(
    "/employees/<int:emp_id>",
    methods=["PUT"]
)(update_employee)

employee_bp.route(
    "/employees/<int:emp_id>",
    methods=["DELETE"]
)(delete_employee)