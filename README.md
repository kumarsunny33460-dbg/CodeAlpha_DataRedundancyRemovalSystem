# CodeAlpha Data Redundancy Removal System

A cloud-based web application developed during the **CodeAlpha Cloud Computing Internship** to detect, manage, and remove duplicate records efficiently. The system stores verified data in a cloud database and provides an easy-to-use interface for managing records.

## 🚀 Live Demo

**Application URL:**
https://codealpha-dataredundancyremovalsystem-420a.onrender.com

---

## 📌 Project Overview

The **Data Redundancy Removal System** is designed to reduce duplicate data storage by identifying repeated records based on important fields such as email and phone number.

The application provides a web interface where users can:

* Add new records
* Automatically detect duplicate records
* View stored records
* Search records
* Edit existing records
* Delete records
* Export data into CSV format

The project demonstrates the use of cloud deployment, database integration, and web application development.

---

## ✨ Features

### 🔹 Duplicate Detection

* Identifies duplicate records using email and phone number.
* Prevents unnecessary data duplication.

### 🔹 Cloud Database Integration

* Uses MongoDB Atlas as a cloud database.
* Stores and retrieves records securely.

### 🔹 CRUD Operations

* Create new records
* Read stored records
* Update existing records
* Delete unwanted records

### 🔹 Search Functionality

* Search records by:

  * Name
  * Email
  * Phone number

### 🔹 CSV Export

* Export stored records into a downloadable CSV file.

### 🔹 Cloud Deployment

* Deployed using Render Cloud Platform.
* Uses Gunicorn production server.

---

## 🛠️ Technologies Used

### Frontend

* HTML
* CSS
* Bootstrap

### Backend

* Python
* Flask Framework

### Database

* MongoDB Atlas

### Deployment

* Render Cloud Platform
* Gunicorn

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```
CodeAlpha_DataRedundancyRemovalSystem/

│
├── app.py                 # Flask application
├── database.py            # MongoDB database connection
├── redundancy.py          # Duplicate detection logic
├── requirements.txt       # Required Python packages
│
├── templates/
│   ├── index.html         # Main webpage
│   └── edit.html          # Edit record page
│
├── static/
│   └── style.css          # Styling files
│
└── README.md              # Project documentation
```

---

## ⚙️ Installation and Setup

### 1. Clone Repository

```bash
git clone https://github.com/kumarsunny33460-dbg/CodeAlpha_DataRedundancyRemovalSystem.git
```

### 2. Navigate to Project Folder

```bash
cd CodeAlpha_DataRedundancyRemovalSystem
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file:

```
MONGO_URI=mongodb+srv://kumarsunny33460_db_user1:yG3g4HGBGaPV8vdv@cluster0.nsapxbs.mongodb.net/?appName=Cluster0
DATABASE_NAME=CloudStorage
COLLECTION_NAME=Records
```

---

### 6. Run Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## ☁️ Cloud Deployment

The application is deployed on **Render Cloud Platform**.

Deployment configuration:

* Runtime: Python
* Server: Gunicorn
* Start Command:

```
gunicorn app:app
```

Live URL:

https://codealpha-dataredundancyremovalsystem-420a.onrender.com

---

## 📊 Working Flow

```
User Input
     |
     ↓
Flask Application
     |
     ↓
Duplicate Detection Algorithm
     |
     ↓
MongoDB Atlas Cloud Database
     |
     ↓
Verified Records Storage
     |
     ↓
CSV Export
```

---

## 🎯 Project Objectives

* Reduce unnecessary duplicate data storage.
* Improve data management efficiency.
* Demonstrate cloud database integration.
* Build and deploy a real-world cloud-based application.

---

## 🔮 Future Improvements

* User authentication system
* Advanced duplicate detection using AI/ML
* Data visualization dashboard
* Automated backup system
* Role-based access control

---

## 👨‍💻 Developer

**Sunny Kumar**

B.Tech Computer Science & Engineering

Developed as part of the **CodeAlpha Cloud Computing Internship**

---

## 📜 License

This project is developed for educational and internship purposes.
