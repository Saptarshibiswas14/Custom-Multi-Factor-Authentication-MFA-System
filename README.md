# Custom-Multi-Factor-Authentication-MFA-System
This is a repository on custom MFA 

📌 Project Title: Custom Multi-Factor Authentication (MFA) System
Description:

Developed a secure custom Multi-Factor Authentication (MFA) system using Python and Flask to enhance user authentication by incorporating an OTP-based second verification step. The system first validates user credentials and then generates and sends a time-sensitive One-Time Password (OTP) via email to the registered user. Only after successful OTP verification is access granted, ensuring an additional layer of security.

Key Features:

🔐 Two-Step Verification: Combines password-based login with OTP-based second factor for improved access security.

🧮 Secure OTP Generation: Uses Python's secrets module to generate cryptographically secure 6-digit OTPs.

📧 Email OTP Delivery: Sends OTPs to users via SMTP using smtplib (or optional integration with email APIs like SendGrid).

⏳ OTP Expiration Logic: Implements a time-bound OTP (5-minute validity) to prevent misuse.

🧾 User Authentication Flow:

Step 1: User logs in with username and password.

Step 2: OTP is generated and sent to registered email.

Step 3: User verifies the OTP on a secure page to complete login.

🔐 Security Practices: Passwords hashed using bcrypt, session tracking included (optional), and OTPs are never logged or stored permanently.

💾 Database: SQLite used for user credentials and temporary OTP data.

Tools & Technologies:

Python, Flask

HTML/CSS (for UI)

SQLite

bcrypt, smtplib, secrets, datetime

Learning Outcome:

Gained hands-on experience in implementing secure authentication flows, email integration, OTP logic, and best practices in protecting user identities through layered security controls—relevant to Identity and Access Management (IAM) systems in real-world environments.

Let me know if you'd like the code with setup instructions too — I can drop that next!
