from pydantic import BaseModel
from datetime import datetime

# Shared properties
class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: datetime.date
    profile_picture_url: str
    age: int

class Customer(UserBase):
    user_id: int

class CustomerCreate(UserBase):
    pass

class CustomerUpdate(UserBase):
    pass

class EmployeeBase(UserBase):
    ssn: int

class Admin(EmployeeBase):
    user_id: int

class AdminCreate(EmployeeBase):
    pass

class AdminUpdate(EmployeeBase):
    pass

class Manager(EmployeeBase):
    user_id: int

class ManagerCreate(EmployeeBase):
    pass

class ManagerUpdate(EmployeeBase):
    pass




