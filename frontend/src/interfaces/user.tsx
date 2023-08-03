export interface Address {
    street: string;
    city: string;
    state: string;
    zip_code: number;
    country: string;
}

export interface Email {
    email: string;
}

export interface User {
    user_id?: number;
    first_name: string;
    last_name: string;
    birthday: Date;
    profile_pic_URL: string;
    age: number;
    address: Address[];
    email: Email[];
    phone_number: number;
    cart_id?: number;
}

export enum EmployeeTypes {
    Manager = "Manager",
    Admin = "Admin"
}

export interface Employee extends User {
    ssn?: number;
    salary?: number;
    start_date?: Date;
    employee_type?: EmployeeTypes
}