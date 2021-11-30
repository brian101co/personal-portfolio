from django.template.loader import render_to_string
from django.core.mail import send_mail

class ContactEmail:

    def __init__(self, template, **kwargs):
        self.template = template
        self.context = kwargs
    
    def create_email_body(self):
        """ Creates email body as HTML and with kwargs as context """
        return render_to_string(self.template, self.context)

    def send(self):
        """ Sends the Contact Email via SMTP """
        message = self.create_email_body()
        send_mail(self.context["subject"], message, 'oliverwebdevelopment2020@gmail.com', ['oliverwebdevelopment2020@gmail.com'])