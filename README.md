# 📧 Alert Gmail Sender

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?logo=python&logoColor=white)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue)

A simple, robust Python utility for sending automated email alerts via Gmail's SMTP server using SSL encryption.

---

## 🏗 How it Works
This script establishes a secure connection to Google's mail servers to dispatch plain-text emails. It uses a context manager to ensure the connection is safely closed after transmission.



---

## 📋 Prerequisites

To use this script with a Gmail account, you **cannot** use your regular login password. You must:

1.  **Enable 2-Step Verification** in your [Google Account Settings](https://myaccount.google.com/).
2.  **Generate an App Password**:
    * Go to [App Passwords](https://myaccount.google.com/apppasswords).
    * Select `Mail` and `Other (Custom name)`.
    * Copy the generated **16-character code**.

---

## 🚀 Quick Start

### 1. Clone the Repository

git clone [https://github.com/anriabb/alert_gmail.git](https://github.com/anriabb/alert_gmail.git)
cd alert_gmail

---

📄 License
Distributed under the MIT License. See LICENSE for more information.

<p align="center">
<b>Developed by <a href="https://www.google.com/search?q=https://github.com/anriabb">anriabb</a></b>
</p>

```bash
