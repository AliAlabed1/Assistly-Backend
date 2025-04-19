# Assistly Backend

Assistly Backend is the server-side component of the Assistly application, designed to handle backend operations, user interactions, and chat session management for AI-based communication.

##  Features

- Manage AI chatbots and their characteristics.
- Create guest users and manage chat sessions.
- Store and retrieve chat messages between AI and users.

##  Data Models Overview

### 1. `Chatbot`
Represents an AI chatbot created by a specific user.

| Field          | Type              | Description                |
|----------------|-------------------|----------------------------|
| clerk_user_id  | CharField(255)    | ID from Clerk authentication |
| name           | CharField(255)    | Name of the chatbot        |
| created_at     | DateTimeField     | Timestamp of creation      |

### 2. `ChatbotCharacteristic`
Defines personality traits or behavior notes associated with a chatbot.

| Field         | Type            | Description                   |
|---------------|-----------------|-------------------------------|
| chatbot       | ForeignKey      | Links to the associated chatbot |
| content       | TextField       | Characteristic content        |
| created_at    | DateTimeField   | Timestamp of creation         |

### 3. `Guest`
Stores information about a guest user initiating a chat session.

| Field      | Type            | Description           |
|------------|-----------------|-----------------------|
| name       | CharField(255)  | Optional guest name   |
| email      | CharField(255)  | Optional guest email  |
| created_at | DateTimeField   | Timestamp of creation |

### 4. `ChatSession`
Represents a chat instance between a chatbot and a guest.

| Field      | Type         | Description                         |
|------------|--------------|-------------------------------------|
| chatbot    | ForeignKey   | Linked chatbot                      |
| guest      | ForeignKey   | Optional guest (nullable)           |
| created_at | DateTimeField| Timestamp of session start          |

### 5. `Message`
Stores each message sent during a chat session.

| Field         | Type            | Description               |
|---------------|-----------------|---------------------------|
| chat_session  | ForeignKey      | Related chat session      |
| content       | TextField       | Message content           |
| sender        | CharField(50)   | 'user' or 'ai'            |
| created_at    | DateTimeField   | Timestamp of the message  |

## 🛠 Technologies Used

- **Python 3**
- **Django**
- **Gunicorn** – Production WSGI server
- **Railway** – For cloud deployment
- **PostgreSQL** – Flexible DB support

## 🚀 Getting Started (Local Setup)

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/AliAlabed1/Assistly-Backend.git
cd Assistly-Backend
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

---

## ☁️ Deployment on Railway

### Step-by-Step

1. Go to [Railway.app](https://railway.app) and sign in.
2. Click on **"New Project"** → **Deploy from GitHub Repo**.
3. Select your `Assistly-Backend` repo.
4. Railway will detect it’s a Python app and install dependencies.
5. In the **"Variables"** section, add the following environment variables:
   - `DJANGO_SECRET_KEY`: Your secret key.
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `*` or your domain
   - `DATABASE_URL`: If using PostgreSQL (Railway auto-generates this if enabled)

6. Add a `start` command in Railway settings:
   ```bash
   gunicorn assistly_backend.wsgi:application
   ```

7. Connect a PostgreSQL plugin (optional) or continue using SQLite for development.

8. Your app is live! 🎉

## 👤 Author

- **Ali Ahmad Alabed**  
  [GitHub Profile](https://github.com/AliAlabed1)
