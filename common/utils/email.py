import sendgrid
from sendgrid.helpers.mail import Mail

from django.conf import settings


def send_email(to, subject, content, sender='admin@example.com'):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    if (len(str(sg)) > 3):
        print('SG is above 3 chars and starts with: ' , str(sg)[:3])
    else:
        print('SG is not above 3 chars')
    mail = Mail(
        from_email=sender,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    return sg.send(mail)