from .models import passwordresetcode
from django.shortcuts import redirect
from django.utils.encoding import force_bytes 
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail



def password_reset_email(user):

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    #Delete any password code attached to the user if there is any
    password_token = passwordresetcode.objects.filter(user = user)
    password_token.delete()

    #Create new password reset token
    stored_token = passwordresetcode.objects.create(code = token, user = user)

    html_message = f"""<div style="margin: 5% 0%;">

            <h2>Reset Your Password</h2>
            Hello {user.first_name}, <br><br>Someone requested for password reset link for an account associated with this email.<br><br>
                Click on the link below to reset your password, Just ignore if you did not request for the link<br><br><strong>Note: The link is only valid for 7 minutes and it can only be used once.</strong><br><br><a href=\"http://marhab-shop.herokuapp.com/reset/{uid}/{token}\" style="color:white; text-decoration: none;border-radius: 25px; background-color: blue; padding: 7px 25px;"> <strong>Reset Password<strong></a>
            </div>"""
    subject = "Password Reset link"
    
    email = ""
    try:
        send_mail(subject, email, 'helpraisemyfund@gmail.com' , [user.email], fail_silently=False,html_message=html_message)
    except BadHeaderError:
        pass
    

