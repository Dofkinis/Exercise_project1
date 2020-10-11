import re


class NewEmployee:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 annual_salary: float,
                 years_employed: int,
                 feedback: int,
                 role: str,
                 email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.annual_salary = annual_salary
        self.feedback = feedback
        self.year_employed = years_employed
        self.email = email

    @classmethod
    def create_employee_from_string(cls, emp_string: str):
        first_name, last_name, annual_salary, years_employed, feedback, role, email = emp_string.split(",")
        if NewEmployee.validate_email(email):
            return cls(first_name, last_name, annual_salary, years_employed, feedback, role, email)

    @staticmethod
    def validate_email(email):
        result = False
        if re.fullmatch("^[a-z0-9]+@+[a-z0-9]+[.][a-z]+", email) is not None:
            result = True
        return  result
