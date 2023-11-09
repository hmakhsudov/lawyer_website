"""
URL configuration for lawyer_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import index, pay_info, process_form, process_form_testimonial, pay_test, pay_by_check, process_form_check, sklad, process_form_sklad, screenshot
from my_calendar.views import calendar_view, EnrollmentView, success_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('pay_info/', pay_info, name='pay_info'),
    path('submit/', process_form, name='process_form'),
    path('submit_сheck/', process_form_check, name='process_form_check'),
    path('submit_testi/', process_form_testimonial, name='submit_testi'),
    path('submit_sklad/', process_form_sklad, name='submit_sklad'),
    path('pay_by_check/', pay_by_check, name='pay_by_check'),
    path('sklad/', sklad, name='sklad'),
    path('screenshot/', screenshot, name='screenshot'),
    path('calendar/', calendar_view, name='calendar'),
    path('enroll/', EnrollmentView.as_view(), name='enroll-page'),
    # Define the success page URL for redirection
    path('success/', success_view, name='success-page'),
    
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)