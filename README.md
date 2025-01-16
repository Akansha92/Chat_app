# Chat App

This is a simple and stylish **Chat Application** built using Django, which includes user authentication (Sign Up, Log In, and Log Out) and real-time messaging functionality. The app supports users chatting with each other through a clean and interactive UI, with a moving bubble background effect for a fun and dynamic user experience.

## Features

- **User Authentication**: 
  - Sign up for new users
  - Log in and log out functionality
  - User session management

- **Chat Functionality**:
  - Real-time messaging between users
  - User can select a recipient from the list and send messages
  - Responsive design suitable for desktops and mobile devices

- **Dynamic UI**:
  - Beautiful design with floating bubbles that follow the cursor
  - Clean, modern layout
  - Bootstrap-based front-end with custom styling for an attractive user interface

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (for floating bubble animation and user interaction)
- **Database**: SQLite (default with Django, can be swapped with other DBs)
- **Authentication**: Django's built-in user authentication system

## Requirements

Before you can run this project locally, make sure you have the following installed:

- Python 3.x
- Django 5.x

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/chat-app.git
   cd chat-app
2. **Set up the virtual environment**:

  If you use venv:
  python -m venv venv
  source venv/bin/activate  # For Windows: venv\Scripts\activate
3. **Install dependencies**:

  pip install -r requirements.txt
4. **Migrate the database**:

  python manage.py migrate
5. **Create a superuser for admin access (optional):**
  python manage.py createsuperuser
6. **Run the development server:**
   python manage.py runserver
7. Open the app in your browser at: http://127.0.0.1:8000/

# File Structure
chat_app/: Main Django app directory containing views, models, and templates.
chat_project/: The main project directory containing settings, URLs, and configurations.
templates/: Contains the HTML files for the login, signup, and chat interfaces.
static/: Contains static files such as CSS, JavaScript, and images.

# Demo
You can access the demo of the app by visiting the live server or by running it locally using the instructions above.
The app allows real-time messaging and a fun floating bubble background effect.

# Screenshots
![image](https://github.com/user-attachments/assets/29447529-4f0d-4bd1-87b5-17bcd2e8bf01)
![image](https://github.com/user-attachments/assets/7a300761-1caa-4a35-a044-0283e7d1be65)
![image](https://github.com/user-attachments/assets/ec82cf27-e40f-49d5-900b-c0f017014842)

# Contributing
Fork this repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature-branch)
Create a new Pull Request

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Inspiration for the floating bubble animation from modern web designs.
Bootstrap for providing a responsive front-end framework.

  
### Key Sections:
1. **Project Overview**: Explains what the project is about, its core features, and how it functions.
2. **Technologies**: Lists the technologies used in the project.
3. **Installation**: Provides detailed steps on setting up the project on a local machine.
4. **File Structure**: Explains the main components of the app’s directory structure.
5. **Contributing**: Instructions for others to contribute to the project.
6. **License**: Basic info on licensing (MIT License in this case, adjust as necessary).



