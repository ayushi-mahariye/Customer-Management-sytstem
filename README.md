# Customer Management System

This repository contains a **Customer Management System** built as a web application using Python, Streamlit, and MySQL. This system allows users to manage customer information efficiently, offering functionalities like adding, updating, deleting, and viewing customer records within a structured database. This lightweight application is ideal for small businesses or developers looking to learn how to integrate web applications with databases.
![Screenshot 2024-10-26 203909](https://github.com/user-attachments/assets/00535249-ea81-4ba2-85c2-6a88842da160)


## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Configuration](#database-configuration)
- [Application Interface](#application-interface)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

## Features

The Customer Management System provides the following core functionalities:
![Screenshot 2024-10-26 203927](https://github.com/user-attachments/assets/862e6c04-33bd-46cd-83a6-08c8d434d7b7)


- **Add Customer**: Insert new customer records, including fields like name, email, phone number, and address.
- **Update Customer**: Modify details of existing customers.
- **Delete Customer**: Remove customer records from the database.
- **View Customers**: Display a comprehensive list of all customers stored in the system.
  ![Screenshot 2024-10-26 204247](https://github.com/user-attachments/assets/d8ef3597-b0d8-4bf0-a310-67afac5a86a4)


## Tech Stack

This project leverages the following technologies:

- **Python**: The primary programming language for application logic.
- **Streamlit**: A Python-based web framework for creating the user interface.
- **MySQL**: The backend database used to store customer records.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.7+**
- **MySQL Server**
- **pip** (Python package installer)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/Customer-Management-System.git
   cd Customer-Management-System
   ```

2. **Install Dependencies**:

   Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:

   - Ensure that your MySQL server is running.
   - Create a new MySQL database (e.g., `customer_db`) and configure a user with privileges.
   - See [Database Configuration](#database-configuration) for detailed setup instructions.

4. **Run the Application**:

   Launch the Streamlit application with:

   ```bash
   streamlit run app.py
   ```

## Usage

After starting the Streamlit application, open the provided local URL in your browser to access the interface. Use the following functionalities:

1. **Add Customer**: Enter the necessary details and save a new customer to the database.
2. **Update Customer**: Modify the information of an existing customer.
3. **Delete Customer**: Select and delete a customer record.
4. **View Customers**: Display all customer data in a tabular view.
   ![Screenshot 2024-10-26 203954](https://github.com/user-attachments/assets/bbd5b24e-8205-4600-b1e6-c022598cfdf3)


## Database Configuration

1. **Create Database**:

   Open your MySQL client and create the database:

   ```sql
   CREATE DATABASE customer_db;
   ```

2. **Create a User** (or use an existing user):

   ```sql
   CREATE USER 'yourusername'@'localhost' IDENTIFIED BY 'yourpassword';
   GRANT ALL PRIVILEGES ON customer_db.* TO 'yourusername'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. **Configure Connection**:

   Update the database connection settings in `app.py`:

   ```python
   connection = mysql.connector.connect(
       host='localhost',
       user='yourusername',
       password='yourpassword',
       database='customer_db'
   )
   ```

## Application Interface

The Streamlit web interface includes intuitive forms for adding, updating, and deleting customers, as well as an interactive table for viewing customer records. Each feature is accessible via easy-to-navigate buttons and input fields.

## Project Structure

```plaintext
├── app.py                  # Main application file
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── db_setup.sql            # Optional script to create tables and sample data
```

## Future Enhancements

Potential improvements for the project:

- **Authentication**: Add user authentication to restrict access.
- **Advanced Search**: Include filters to search customers based on criteria like location or email.
- **Data Export**: Enable data export to CSV or Excel for reporting.
- **Error Handling**: Improve error handling for database connectivity and input validation.

## Contributors

- **Ayushi Mahariye** 

---
