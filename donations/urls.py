from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('signup1/',views.signup1,name="signup1"),
    path('login1/',views.login1,name="login1"),
    path('signup2/',views.signup2,name="signup2"),
    path('login2/',views.login2,name="login2"),
    path('home1/',views.home1,name="home1"),
    path('home2/',views.home2,name="home2"),
    path('home3/',views.home3,name="home3"),
    path('event/',views.event,name="event"),
    path('gathering/',views.gathering,name="gathering"),
    path('logout1/',views.logout1,name="logout1"),
    path('event1/',views.event1,name="event1"),
    path('upcoming/',views.upcoming,name="upcoming"),
   



]