from django.urls import path
from app import views

urlpatterns = [
   path('',views.home,name='home'),
   path('contactus',views.contactus,name='contactus'),
   path('contactus_submited',views.contactus_submited,name='contactus_submited'),
   path('aboutus',views.aboutus,name='aboutus'),
   path('feedback',views.feedback,name='feedback'),
   path('feedback_submit', views.feedback_submit, name='feedback_submit'),
   path('booking', views.booking, name='booking'),
   path('booking_done', views.booking_done, name='booking_done'),
   
]