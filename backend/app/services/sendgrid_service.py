from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.core.config import get_settings


def send_email(to_email: str, subject: str, html_content: str):
    message = Mail(
        from_email="radakanis321@gmail.com",
        to_emails=to_email,
        subject=subject,
        html_content=html_content,
    )
    try:
        sendgrid_client = SendGridAPIClient(api_key=get_settings().sendgrid_api_key)
        response = sendgrid_client.send(message)
        print(
            f"Email sent successfully to {to_email} with status code {response.status_code}",
            flush=True,
        )
        return True
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}", flush=True)
        return False
