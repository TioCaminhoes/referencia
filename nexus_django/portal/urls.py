from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
 path("",views.home,name="home"),path("servicos/",views.services,name="services"),path("servicos/<slug:slug>/",views.service_detail,name="service_detail"),
 path("projetos/",views.projects,name="projects"),path("projetos/<slug:slug>/",views.project_detail,name="project_detail"),
 path("blog/",views.blog,name="blog"),path("blog/<slug:slug>/",views.post_detail,name="post_detail"),
 path("contato/",views.contact,name="contact"),path("newsletter/",views.newsletter,name="newsletter"),
 path("cadastro/",views.signup,name="signup"),path("login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),path("logout/",auth_views.LogoutView.as_view(),name="logout"),
 path("dashboard/",views.dashboard,name="dashboard"),path("dashboard/agendamento/",views.book_appointment,name="book_appointment"),path("dashboard/agendamento/<int:pk>/cancelar/",views.cancel_appointment,name="cancel_appointment"),
]
