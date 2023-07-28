from app.schemas.pydantic.user import Employee, EmployeeCreate, EmployeeUpdate
from app.schemas.pydantic.address import Address, AddressCreate, AddressUpdate
from app.schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from app.models.database_manager import DatabaseManager
from app.dao.address_dao import AddressDao
from app.dao.email_dao import EmailDao
from typing import List

class EmployeeDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_employee(self, employee: EmployeeCreate) -> int:
        first_name = employee.first_name
        last_name = employee.last_name
        birthday = employee.birthday
        profile_pic_URL = employee.profile_pic_URL
        age = employee.age
        address_list = employee.address
        email_list = employee.email
        ssn = employee.ssn
        salary = employee.salary
        start_date = employee.start_date
        employee_type = employee.employee_type
        password = employee.password

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `User` (`password`, `first_name`, `last_name`, `birthday`, `profile_pic_URL`, `age`) VALUES (%s, %s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (password, first_name, last_name, birthday, profile_pic_URL, age))
                self.connection.commit()
                user_id = cursor.lastrowid

                for address in address_list:
                    address = AddressCreate(user_id=user_id, street=address.street, city=address.city, zip_code=address.zip_code, state=address.state, country=address.country)
                    print(address)
                    AddressDao().create_address(address)

                for email in email_list:
                    email = EmailCreate(user_id=user_id, email=email.email)
                    print(email)
                    EmailDao().create_email(email)

                sql = "INSERT INTO `Employee` (`user_id`, `ssn`, `salary`, `start_date`, `employee_type`) VALUES (%s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, ssn, salary, start_date, employee_type))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e.message)

    def get_employee_by_id(self, user_id: int) -> Employee:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()

                address_list = AddressDao().get_address_by_id(user_id)

                email_list = EmailDao().get_email_by_id(user_id)

                sql = "SELECT * FROM `Employee` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result_employee = cursor.fetchone()
                user_id, first_name, last_name, birthday, profile_pic_URL, age = result['user_id'], result['first_name'], result['last_name'], result['birthday'], result['profile_pic_URL'], result['age']
                ssn, salary, start_date, employee_type = result_employee['ssn'], result_employee['salary'], result_employee['start_date'], result_employee['employee_type']
                employee = Employee(user_id=user_id, first_name=first_name, last_name=last_name, birthday=birthday, profile_pic_URL=profile_pic_URL, age=age, address=address_list, email=email_list, ssn=ssn, salary=salary, start_date=start_date, employee_type=employee_type)

                return employee
        except Exception as e:
            print(e.message)
    
    def get_all_employees(self) -> List[Employee]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id` IN (SELECT `user_id` FROM `Employee`)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()

                employee_list = []
                for row in result:
                    address_list = AddressDao().get_address_by_id(row['user_id'])

                    email_list = EmailDao().get_email_by_id(row['user_id'])

                    sql = "SELECT * FROM `Employee` WHERE `user_id`=%s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (row['user_id']))
                    result_employee = cursor.fetchone()
                    user_id, first_name, last_name, birthday, profile_pic_URL, age = row['user_id'], row['first_name'], row['last_name'], row['birthday'], row['profile_pic_URL'], row['age']
                    ssn, salary, start_date, employee_type = result_employee['ssn'], result_employee['salary'], result_employee['start_date'], result_employee['employee_type']

                    employee = Employee(user_id=user_id, first_name=first_name, last_name=last_name, birthday=birthday, profile_pic_URL=profile_pic_URL, age=age, address=address_list, email=email_list, ssn=ssn, salary=salary, start_date=start_date, employee_type=employee_type)
                    employee_list.append(employee)
                return employee_list
        except Exception as e:
            print(e.message)