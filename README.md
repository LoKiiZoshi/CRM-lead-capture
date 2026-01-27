ProjectName* CRM-lead-capture


├── accounts/        # User authentication & account logic

├── crm_leads/       # CRM core functionality

├── leads/           # Lead capture & management


├── db.sqlite3       # Database

├── manage.py        # Django management file

├── requirements.txt'

└── README.md

Installation & Setup Guide

Follow these steps to run the project locally.

Clone the Repository
git clone 
cd CRM-lead-capture

Create Virtual Environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py makemigrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser

Run Development Server
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/


Admin panel:

http://127.0.0.1:8000/admin/
