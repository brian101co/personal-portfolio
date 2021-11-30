from django.template.loader import render_to_string
from django.core.mail import send_mail

class ContactEmail:
    @staticmethod
    def create_email_body(template, **kwargs):
        """ Creates an HTML sting of the email body from a given template. kwargs are passed as template context. """
        return render_to_string(template, context=kwargs)

    @classmethod
    def send_email(cls, template, **kwargs):
        message = cls.create_email_body(template, **kwargs)
        send_mail(kwargs["subject"], message, 'oliverwebdevelopment2020@gmail.com', ['oliverwebdevelopment2020@gmail.com'])