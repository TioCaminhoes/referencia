from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Service(models.Model):
    name=models.CharField(max_length=120)
    slug=models.SlugField(unique=True)
    short_description=models.CharField(max_length=220)
    description=models.TextField()
    icon=models.CharField(max_length=30,default="✦")
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    active=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-featured","name"]
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse("service_detail",args=[self.slug])

class Project(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    category=models.CharField(max_length=80)
    summary=models.CharField(max_length=240)
    description=models.TextField()
    client=models.CharField(max_length=120,blank=True)
    year=models.PositiveIntegerField(default=2026)
    featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-featured","-year","-created_at"]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("project_detail",args=[self.slug])

class Post(models.Model):
    title=models.CharField(max_length=180)
    slug=models.SlugField(unique=True)
    excerpt=models.CharField(max_length=300)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    published=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: ordering=["-created_at"]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("post_detail",args=[self.slug])

class ContactMessage(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    subject=models.CharField(max_length=180)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)
    class Meta: ordering=["-created_at"]
    def __str__(self): return f"{self.name} — {self.subject}"

class NewsletterSubscriber(models.Model):
    email=models.EmailField(unique=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email

class Appointment(models.Model):
    STATUS=[("pending","Pendente"),("confirmed","Confirmado"),("cancelled","Cancelado"),("done","Concluído")]
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="appointments")
    service=models.ForeignKey(Service,on_delete=models.PROTECT)
    date=models.DateField()
    time=models.TimeField()
    notes=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=STATUS,default="pending")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-date","-time"]
    def __str__(self): return f"{self.service} — {self.date} {self.time}"
