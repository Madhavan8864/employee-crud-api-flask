from config.database import get_connection


class EmployeeModel:

    @staticmethod
    def create_employee(data):
        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employees
        (
            employee_code,
            name,
            email,
            phone,
            department,
            designation,
            salary,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["employee_code"],
            data["name"],
            data["email"],
            data["phone"],
            data["department"],
            data["designation"],
            data["salary"],
            data["status"]
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_employees():
        conn = get_connection()

        employees = conn.execute(
            "SELECT * FROM employees"
        ).fetchall()

        conn.close()

        return [dict(emp) for emp in employees]

    @staticmethod
    def get_employee_by_id(emp_id):
        conn = get_connection()

        employee = conn.execute(
            "SELECT * FROM employees WHERE id=?",
            (emp_id,)
        ).fetchone()

        conn.close()

        return dict(employee) if employee else None

    @staticmethod
    def update_employee(emp_id, data):
        conn = get_connection()

        conn.execute("""
        UPDATE employees
        SET
            name=?,
            email=?,
            phone=?,
            department=?,
            designation=?,
            salary=?,
            status=?
        WHERE id=?
        """,
        (
            data["name"],
            data["email"],
            data["phone"],
            data["department"],
            data["designation"],
            data["salary"],
            data["status"],
            emp_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_employee(emp_id):
        conn = get_connection()

        conn.execute(
            "DELETE FROM employees WHERE id=?",
            (emp_id,)
        )

        conn.commit()
        conn.close()