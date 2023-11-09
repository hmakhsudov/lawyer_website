from django.shortcuts import render
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Course, Enrollment
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import EnrollmentForm
from .models import Enrollment


from .models import Course

def calendar_view(request):
    current_date = datetime.now()
    start_of_week = datetime.strptime(request.GET.get('start_of_week'), "%Y-%m-%d") if 'start_of_week' in request.GET else current_date - timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    events = Course.objects.filter(date_starting__range=[start_of_week, end_of_week]).order_by('date_starting')
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    week_date_ranges = f"{start_of_week.strftime('%d.%m')} - {end_of_week.strftime('%d.%m')}"

    
    return render(request, 'calendar.html', {'events': events, 'start_of_week': start_of_week_str, 'week_date_ranges': week_date_ranges})


class EnrollmentView(View):
    def post(self, request):
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            # Save to the database
            Enrollment.objects.create(email=email, phone=phone)
            
            # Send email
            send_mail(
                'Subject',
                'Message',
                'schoolbrokerr@gmail.com',
                [email],
                fail_silently=False,
            )
            
            return redirect('success-page')  # Redirect to a success page after submission
            
        return HttpResponse('Не получилось записаться')  # Handle form errors
    
    
    
def success_view(request):
    return render(request, 'success-page.html')