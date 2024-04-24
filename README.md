# ListMind

![Status](https://img.shields.io/badge/STATUS-FINISHED-44CC11)
![Date](https://img.shields.io/badge/RELEASEDATE-DECEMBER-44CC11)
![License](https://img.shields.io/badge/LICENSE-MTI-44CC11)

This Project Was Developed to Manage Your Company's Services Quickly and Conveniently, Accompanied By a Dashboard Containing Information Such as Monthly Revenue, Number of Services Registered, Completed, and Under Warranty.

## Links

- [Project](https://listminder.pythonanywhere.com/)

## Home

![Home Layout](./assets/listmindhome.png)

## DashBoard

![Home Layout](./assets/listminddashboard.png)

## Features

### Authentication

- **Account Login:** Allows users to authenticate in the application.
- **Account Register:** Enables new users to create an account.

### Service

- **Add Service:** Allows users to add new services.
- **Edit Service:** Allows modification of the informations of a service.
- **Remove Service:** Allows the deletion of a service.
- **Check Service:** Allows marking a service as completed or not completed.
- **PDF by Service:** Allows you generate a PDF from a service.
- **Warranty Area:** Allows you view all warranty services
- **Completed Area:** Allows you view all completed services

### Filter

- **Name:** Allows you filter all services by name
- **Date:** Allows you filter all services between two dates
- **Multiple Filters:** Allows you filter all services by name and two dates.

### DashBoard

- **Monthly Revenue:** Allows you view your monthly revenue
- **Quantity of services:** Allows you view the total quantity of services
- **Quantity of completed services:** Allows you view the quantity of completed services
- **Quantity of warranty services:** Allows you view the quantity of warranty services

## Technologies Used

### Back-End
- Python
- Django
- JavaScript

### Front-End
- HTML
- CSS
- JavaScript

### Deploy
- Back-End: PythonAnyWhere
- Front-End: PythonAnyWhere
- Database: MySql/PythonAnyWhere

## Run Project

#### Prerequisite
- Python 3.11

```bash

# Clone Repository
git clone https://github.com/V1KILL/PROJETO-LISTMIND.git

# Activate Virtual Environment
.\venv\Scripts\activate

# Activate Virtual Environment (Linux)
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py migrate
