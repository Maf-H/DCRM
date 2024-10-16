# Customer Relation Managment using Django Framewok
Introduction

This is a Django project about customer rrelation managment(CRM)
Features

    Create Account
    Login
    Register Customer
    Read Customers
    Update Customer
    Deleting Customer

Requirements

    Python 3.x
    Django

Getting Started

    Clone this repository to your local machine.
    Change directory to Django CRM
    Make sure you have Python 3.x and installed.
    It is recommended to use virtual environment to protect package conflict
       to create: python3 -m venv crm_env
       to acticate: source crm_env/bin/activate
       
    install django: pip install django
    
    Open a terminal or command prompt and navigate to the project directory.
    Run the python3 manage.py runserver using the following command:
How to Use

      1. Customers can register themself.
         .During Registeration there are pre requisite to filfill what characters to use in username
         .Password can't be common and must not look like username
         .Username must not be registered before (unique username for each user)
      2. After Registering them self, they can login using username and password
         .127.0.0.1:8000/register/
      3. If you are registered and login you can do the following:
      You can do CRUD (create, read, update, and delete/destroy) operation.
        1. Create: Insert new customer data
           .127.0.0.1:8000/add_record/
        3. Read: Read registered customer data
           .127.0.0.1:8000/record/
        5. Update: Modify registered customer data
           .127.0.0.1:8000/update_record/
        7. Delete: You can delete customer data
Contributing

      If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request. We appreciate your contributions!
