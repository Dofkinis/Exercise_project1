import json
from employee_class import NewEmployee
import database

data_strings_list = []
concatenated_string = ""

with open("company_employees.json") as in_file:
    data_company_employees = json.load(in_file)

with open("feedback_for_employees.json") as in_file:
    data_feedback_for_employees = json.load(in_file)

is_working_for_3_years = lambda x: x >= 3

# Concatenated string = firstName, lastName, annual_salary, years_employed, feedback, role, emailAddress
for emp_dict in data_company_employees["Employees"]:
    if not is_working_for_3_years(emp_dict["years_employed"]):
        continue
    for emp_field in emp_dict:
        if emp_field == "emailAddress":
            for feedback_dict in data_feedback_for_employees["Feedback"]:
                if feedback_dict["emailAddress"] == emp_dict["emailAddress"]:
                    concatenated_string += str(feedback_dict["feedback"]) + ","
                    concatenated_string += feedback_dict["role"] + ","
                    break
        concatenated_string += str(emp_dict[emp_field]) + ","
    data_strings_list.append(concatenated_string[:-1])
    concatenated_string = ""

database.delete_all_employees()

for i in range(len(data_strings_list)):
    emp = NewEmployee.create_employee_from_string(data_strings_list[i])
    database.create_employee(emp.first_name, emp.last_name, emp.role,
                             emp.annual_salary,
                             emp.feedback, emp.year_employed, emp.email)

database.get_employees()
