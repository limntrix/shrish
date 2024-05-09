from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('index.html',views.home, name='index'),
   path("contacts.html",views.contact,name="contact"),
   path("courses.html",views.courses,name="courses"),
   path("blog.html",views.blog,name="blog"),
   path("about.html",views.about,name="about"),
   path("FaQ.html",views.FaQ,name="FaQ"),
   ]