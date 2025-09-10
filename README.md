# Checka - Habit Tracker

Checka is a simple and effective habit tracker web app built with Django.  
It helps you build and maintain healthy habits by letting you record, track, and review your progress over time.

---

## 🚀 Features
- User authentication (login, logout, register, password reset)
- Create, update, and delete habits
- Categorize habits (Health, Fitness, Productivity, etc.)
- Track habit records daily with status and quantity
- Minimalistic UI with responsive design

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/JTCubed/Checka.git
cd checka
```

### 2. Create a virtual environment
```bash
python3 -m venv env
```

### 3. Activate the virtual environment
```bash
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
 ```bash
 python manage.py migrate
 ```

### 6. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```