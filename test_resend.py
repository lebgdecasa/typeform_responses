import resend
from dotenv import load_dotenv
import os

load_dotenv()

resend.api_key = os.getenv('RESEND_API_KEY')

try:
    # Send test email to yourself
    response = resend.Emails.send({
        "from": "redabennani@epinnovators.org",
        "to": "jad.lahrichi@gmail.com",  # <- Replace with YOUR email
        "subject": "Test from Typeform Automation",
        "html": """
        <h1>🎉 Email sending works!</h1>
        <p>Your Resend integration is set up correctly.</p>
        <div style="margin: 20px 0;">
            <a href="#" style="font-size: 24px; text-decoration: none; margin: 0 10px;">😊</a>
            <a href="#" style="font-size: 24px; text-decoration: none; margin: 0 10px;">😐</a>
            <a href="#" style="font-size: 24px; text-decoration: none; margin: 0 10px;">☹️</a>
        </div>
        """
    })
    print("✅ Email sent successfully!")
    print(f"Email ID: {response['id']}")
except Exception as e:
    print(f"❌ Error: {e}")
