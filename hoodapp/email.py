from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_register_confirm_email(name,receiver):
    subject = 'Welcome to Hoody application'
    sender = 'danmuv12@gmail.com'
    html_content = render_to_string('emails/RegEmail.html',{"name":name})
    text_content = render_to_string('emails/RegEmail.txt',{"name":name})
    
    send_mail(subject,text_content,sender,[receiver],html_message = html_content,fail_silently=False)