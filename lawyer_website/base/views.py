from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Testimonial
def index(request):
    return render(request, 'index.html')

def pay_info(request):
    return render(request, 'payment.html')


def pay_by_check(request):
    return render(request, 'payment_schet.html')


def sklad(request):
    return render(request, 'skladirovanie_chekov.html')

def screenshot(request):
    return render(request, 'screenshots.html')

def process_form(request):
    if request.method == 'POST':
        # Get the form data from the request.POST dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        subject = 'Test Email'  # The subject of the email
        message = f'Hello, {name},{phone}, This is a test email from Django.'  # The email body message
        from_email = settings.EMAIL_HOST_USER  # The sender's email address
        recipient_list = [email,]  # A list of recipient email addresses

        send_mail(subject, message, from_email, recipient_list)
        
        # Do something with the form data (e.g., save to the database, send emails, etc.)
        # ...

        # For example, you can print the form data to the console

    return render(request, 'success.html')

def process_form_check(request):
    if request.method == 'POST':
        # Get the form data from the request.POST dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        inn = request.POST.get('inn')
        subject = 'ЗАЯВКА НА ПОЛУЧЕНИЕ СЧЕТА'  # The subject of the email
        message = f'ФИО ОТПРАВИТЕЛЯ: {name}\n ПОЧТА ОТПРАВИТЕЛЯ: {email}\n ТЕЛЕФОН ОТПРАВИТЕЛЯ: {phone}\n ИНН или КПП ОТПРАВИТЕЛЯ: {inn}'  # The email body message
        from_email = settings.EMAIL_HOST_USER  # The sender's email address
        recipient_list = [settings.EMAIL_HOST_USER, 'info@school-broker.ru']  # A list of recipient email addresses

        send_mail(subject, message, from_email, recipient_list)
        
        # Do something with the form data (e.g., save to the database, send emails, etc.)
        # ...

        # For example, you can print the form data to the console

    return render(request, 'success.html')

def process_form_sklad(request):
      if request.method == 'POST':
        # Get the form data from the request.POST dictionary
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = 'БЫЛ СКЛАДИРОВАН ЧЕК'  # The subject of the email
        message = f'ФИО ОТПРАВИТЕЛЯ: {name}\n ПОЧТА ОТПРАВИТЕЛЯ: {email}\n'  # The email body message
        from_email = settings.EMAIL_HOST_USER  # The sender's email address
        recipient_list = [settings.EMAIL_HOST_USER, 'info@school-broker.ru']
        send_mail(subject, message, from_email, recipient_list)
        
        return render(request, 'success.html')




def process_form_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Testimonial.objects.create(name=name, email=email, phone=phone)

    return render(request, 'success.html')




def pay_test(request):
    return render(request, 'test.html')
