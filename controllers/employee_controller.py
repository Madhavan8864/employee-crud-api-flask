from flask import request, jsonify
from models.employee_model import EmployeeModel
from validators.employee_validator import validate_employee


def create_employee():

    data = request.get_json()

    is_valid, message = validate_employee(data)

    if not is_valid:
        return jsonify({
            "success": False,
            "message": message
        }), 400

    if "status" not in data:
        data["status"] = "Active"

    try:
        EmployeeModel.create_employee(data)

        return jsonify({
            "success": True,
            "message": "Employee created successfully"
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


def get_all_employees():

    employees = EmployeeModel.get_all_employees()

    return jsonify({
        "success": True,
        "count": len(employees),
        "data": employees
    })


def get_employee(emp_id):

    employee = EmployeeModel.get_employee_by_id(emp_id)

    if not employee:
        return jsonify({
            "success": False,
            "message": "Employee not found"
        }), 404

    return jsonify({
        "success": True,
        "data": employee
    })


def update_employee(emp_id):

    employee = EmployeeModel.get_employee_by_id(emp_id)

    if not employee:
        return jsonify({
            "success": False,
            "message": "Employee not found"
        }), 404

    data = request.get_json()

    EmployeeModel.update_employee(emp_id, data)

    return jsonify({
        "success": True,
        "message": "Employee updated successfully"
    })


def delete_employee(emp_id):

    employee = EmployeeModel.get_employee_by_id(emp_id)

    if not employee:
        return jsonify({
            "success": False,
            "message": "Employee not found"
        }), 404

    EmployeeModel.delete_employee(emp_id)

    return jsonify({
        "success": True,
        "message": "Employee deleted successfully"
    })