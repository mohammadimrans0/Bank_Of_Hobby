from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives


class HomeView(TemplateView):
    template_name = 'index.html'

# sending confirmation email
def send_transaction_email(user, subject, body_content):    
        header = f"<h3>Hello, {user.get_full_name()}</h3>"
        footer = """
            <br/>
            <p>Thanks for banking with us</p>
            <p>Bank Of Hobby</p>
        """
        
        full_message = f"""
            {header}
            {body_content}
            {footer}
        """
        
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(full_message, "text/html")
        send_email.send()
