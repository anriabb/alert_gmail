Simple Gmail SMTP Email Sender (Python)

This project is a minimal Python script that sends a plain-text email using Gmail SMTP over SSL.

📌 Features

Sends a simple email (subject + body)

Uses Gmail’s SMTP server

Secure SSL connection

Minimal dependencies (standard library only)

📁 File Structure
.
├── send_email.py
└── README.md

🛠 Requirements

Python 3.7+

A Gmail account

Gmail App Password (required if 2FA is enabled)

🔐 Important: Gmail App Password

Google does not allow normal account passwords for SMTP.

Enable 2-Step Verification on your Google account

Go to Google Account → Security → App passwords

Generate an app password for Mail

Use that password in SMTP_PASS

⚙️ Configuration

Edit the following variables in the script:

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "example@gmail.com"
SMTP_PASS = "your_app_password"

SENDER = "example@gmail.com"
RECIPIENT = "example@gmail.com"


⚠️ Do NOT commit real credentials to GitHub.
Use environment variables for production.

▶️ Usage

Run the script:

python send_email.py


If successful, you’ll see:

Email sent

📧 Example Function Call
send_simple_email("Hello", "This is a test email.")

🚨 Common Errors
Error	Cause	Fix
Authentication failed	Wrong password	Use Gmail App Password
TimeoutError	Network / firewall issue	Check internet or SMTP port
SMTPAuthenticationError	Less secure apps disabled	Enable App Passwords
🔒 Security Tips

Never hardcode credentials in public repos

Use environment variables:

export SMTP_USER="example@gmail.com"
export SMTP_PASS="app_password"

📄 License

This project is provided for educational purposes. Use at your own risk.
