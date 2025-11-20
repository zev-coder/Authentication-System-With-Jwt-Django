## for portofolio and education purpose

# 🔐 Django JWT Authentication API

This project is result of implementation **Authentication using JWT (JSON Web Token)** with **Django REST Framework** and **SimpleJWT**.  
The main purpose of this repo is giving an example how to make login system, registering, endpoint protection, and refresh token as basic of microsevices authentication
---

## 🚀 Main Feature

- User Regsitration
- User Login → Generate **Access Token** & **Refresh Token**
- Refresh Token Endpoint
- endpoint protection using `IsAuthenticated`
- Custom User Serializer
- Logout (blacklist refresh token)
- 
---

## 🛠️ Teknologi yang Digunakan

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- SimpleJWT  
- SQLite (default)

---

## 📁 Struktur Project

```
App/
├── App/              # Main Project
│   ├── settings.py   # Project Configuration
│   ├── urls.py       # Main Routing
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── Auth/             # Spesfic Application For Authentication
│   ├── models.py     # Model Custom Users
│   ├── serializers.py # Serializer For Register & Login
│   ├── views.py      # ViewHandler Auth
│   ├── urls.py       # Routing For Auth
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   └── __init__.py
│
├── manage.py         # Entry point Django
├── db.sqlite3        # Database default
└── requirements.txt  # Dependencies
```

---

## 🛠 instalation & setup

### 1. Clone Repository

```bash
git clone <repo-url>
cd App
```

### 2. Make Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migration

```bash
python manage.py migrate
```

### 5. Run The Server

```bash
python manage.py runserver
```

---

## 🔐 Endpoint Autentikasi (JWT)

Using **SimpleJWT**.

### 1. Register User

```
POST /auth/register/
```

Body JSON:

```json
{
  "username": "testuser",
  "email": "test@mail.com",
  "password": "password123"
}
```

### 2. Login (Get Token)

```
POST /auth/login/
```

Response:

```json
{
  "access": "<ACCESS_TOKEN>",
  "refresh": "<REFRESH_TOKEN>"
}
```

### 3. Refresh Token

```
POST /auth/refresh/
```

Body:

```json
{
  "refresh": "<REFRESH_TOKEN>"
}
```

### 4. Protected Endpoint

Use header:

```
Authorization: Bearer <ACCESS_TOKEN>
```

---

## 🧩 Example Of Serializer

```python
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
```

---

## 📌 Note

* Makesure **AllowAny** used just upon to endpoint public (register & login).
*  Another Endpoint must use pakai **IsAuthenticated**.
*  `REST_FRAMEWORK` and JWT settings in `settings.py`.

---





