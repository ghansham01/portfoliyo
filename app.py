from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback

load_dotenv()

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        # Get form data
        name = (request.form.get('name') or '').strip()
        email = (request.form.get('email') or '').strip()
        message = (request.form.get('message') or '').strip()

        if not (name and email and message):
            return jsonify({"status": "error", "message": "All form fields are required."}), 400
        
        # Debug prints
        print(f"Sending email using: {os.getenv('EMAIL_USER')}")

        # Email configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = os.getenv('EMAIL_USER')
        sender_password = os.getenv('EMAIL_PASSWORD')
        receiver_email = os.getenv('RECEIVER_EMAIL', "viomshrotriya45@gmail.com")

        if not sender_email or not sender_password:
            return jsonify({"status": "error", "message": "Missing EMAIL_USER or EMAIL_PASSWORD in .env"}), 500

        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Portfolio Contact from {name}"
        body = f"New message from your portfolio website:\n\nName: {name}\nEmail: {email}\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        # Send email with explicit EHLO/starttls and timeout
        with smtplib.SMTP(smtp_server, smtp_port, timeout=15) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return jsonify({"status": "success", "message": "Message sent successfully!"})

    except Exception:
        traceback.print_exc()
        return jsonify({"status": "error", "message": "Internal server error — check server logs"}), 500

if __name__ == '__main__':
    app.run(debug=True)