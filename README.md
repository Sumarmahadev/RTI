# Student Record Management System

## Project Overview

This project is a **Student Record Management System** built using **React.js**.
It allows users to **add, edit, delete, and view student records** in a table format.
All CRUD operations are handled on the **frontend using React state**, without a backend.

This project was developed as part of a **Full Stack Assignment – Students Table**.

---

## Features

### Student Table

* Displays student records in a table
* Columns include:

  * Name
  * Email
  * Age
  * Actions (Edit / Delete)

### Add Student

* Add new student records
* Form validation includes:
* All fields are mandatory
* Email must be in valid format
* Age must be greater than 0

### Edit Student

* Edit existing student details
* Form is pre-filled with student data
* Same validation rules apply

### Delete Student

* Students can be deleted
* Includes confirmation dialog before deletion

### Excel Export

* Download the student list as an Excel file
* Implemented using **xlsx** and **file-saver**

### Simulated Loading

* Displays a loading state before rendering the student table

---

## Technologies Used

* React.js
* React Router
* Tailwind CSS
* JavaScript (ES6)
* XLSX (Excel export)
* File-Saver

---

## Project Structure

```
src
│
├── assets
│
├── components
│   ├── StudentForm.jsx
│   └── StudentTable.jsx
│
├── pages
│   ├── Home.jsx
│   ├── Login.jsx
|   |-- Logout.jsx
|   |-- Regitser.jsx
│   ├── Dashboard.jsx
│   ├── AddStudent.jsx
│   └── StudentsList.jsx
│
├── App.jsx
└── main.jsx
```

---

## Installation and Setup

1. Clone the repository

```
git clone https://github.com/Sumarmahadev/Student-Record-Management-System/
```

2. Navigate to project folder

```
cd student table 
```

3. Install dependencies

```
npm install
```

4. Start the development server

```
npm run dev
```

---

## Live Project

Frontend Hosted Link:

```
https://recordrapid.netlify.app/
```

---

## GitHub Repository

```
https://github.com/Sumarmahadev/Student-Record-Management-System
```

---

## Optional Backend (Bonus)

Backend implementation using **NestJS and PostgreSQL** can be added to handle CRUD operations via APIs.
This part is optional and not required for the assignment.

---

## Author

Developed by **[SUMAR CHIMACODE]**
