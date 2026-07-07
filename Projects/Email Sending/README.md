# 📧 Email Sending using Python

A simple Python project that sends emails using Gmail's SMTP server. This project demonstrates how to send emails programmatically using Python and the `smtplib` and `email` libraries.

---

## 🚀 Features

- Send emails using Gmail SMTP
- Secure authentication using Gmail App Password
- Simple command-line interface
- Custom email recipient, subject, and body
- Exception handling for common errors

---

## 🛠️ Technologies Used

- Python 3
- smtplib
- email.mime.multipart
- email.mime.text

---

## 📂 Project Structure

```
Email Sending/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
└── email_env/
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project

```bash
cd Email-Sending
```

### 3. Create a virtual environment

```bash
python -m venv email_env
```

### 4. Activate the virtual environment

#### Windows

```bash
email_env\Scripts\activate
```

#### Linux/macOS

```bash
source email_env/bin/activate
```

### 5. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Update the following variables in `app.py`:

```python
smtp_server = "smtp.gmail.com"
smtp_port = 587

sender_email = "your_email@gmail.com"
passkey = "your_16_character_app_password"
```

> **Note:** Do not use your Gmail account password. Use a Gmail App Password.

---

## ▶️ Run the Project

```bash
python app.py
```

Example:

```
Enter Email address: receiver@gmail.com
Enter Email Subject: Greetings
Enter Email Body: Hello! This email was sent using Python.

Successfully email sent to receiver@gmail.com
```

---

## 📋 Requirements

Generate the requirements file using:

```bash
pip freeze > requirements.txt
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔐 Gmail App Password

To use Gmail SMTP:

1. Enable **2-Step Verification** for your Google account.
2. Go to **Google Account → Security → App Passwords**.
3. Generate a new App Password.
4. Copy the generated 16-character password.
5. Use it as the `passkey` in your code.

---

## 📚 Concepts Covered

- SMTP Protocol
- Email Authentication
- Gmail App Password
- MIME Messages
- Python Exception Handling
- Virtual Environments
- Requirements File

---

## 👨‍💻 Author

**Abinay Teja Gaddam**

B.Tech CSE | Python Developer | AI & ML Enthusiast

---