from django.contrib import admin
from .models import Service,Project,Post,ContactMessage,NewsletterSubscriber,Appointment
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin): list_display=("name","featured","active","price"); prepopulated_fields={"slug":("name",)}; list_filter=("active","featured")
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): list_display=("title","category","year","featured"); prepopulated_fields={"slug":("title",)}; list_filter=("category","featured")
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): list_display=("title","author","published","created_at"); prepopulated_fields={"slug":("title",)}; list_filter=("published",)
@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin): list_display=("name","email","subject","read","created_at"); list_filter=("read",); search_fields=("name","email","subject")
@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin): list_display=("email","active","created_at"); list_filter=("active",)
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin): list_display=("user","service","date","time","status"); list_filter=("status","service","date"); search_fields=("user__username","user__email")
