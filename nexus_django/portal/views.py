from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from django.utils import timezone
from .forms import AppointmentForm,ContactForm,NewsletterForm,SignUpForm
from .models import Appointment,Post,Project,Service

def home(request):
    q=request.GET.get("q","").strip()
    services=Service.objects.filter(active=True)[:6]
    projects=Project.objects.all()[:3]
    posts=Post.objects.filter(published=True)[:3]
    if q:
        services=Service.objects.filter(active=True).filter(Q(name__icontains=q)|Q(description__icontains=q))
        projects=Project.objects.filter(Q(title__icontains=q)|Q(summary__icontains=q))
        posts=Post.objects.filter(published=True).filter(Q(title__icontains=q)|Q(content__icontains=q))
    return render(request,"portal/home.html",{"services":services,"projects":projects,"posts":posts,"query":q})

def services(request): return render(request,"portal/services.html",{"services":Service.objects.filter(active=True)})
def service_detail(request,slug): return render(request,"portal/service_detail.html",{"service":get_object_or_404(Service,slug=slug,active=True)})
def projects(request): return render(request,"portal/projects.html",{"projects":Project.objects.all()})
def project_detail(request,slug): return render(request,"portal/project_detail.html",{"project":get_object_or_404(Project,slug=slug)})
def blog(request): return render(request,"portal/blog.html",{"posts":Post.objects.filter(published=True)})
def post_detail(request,slug): return render(request,"portal/post_detail.html",{"post":get_object_or_404(Post,slug=slug,published=True)})

def contact(request):
    form=ContactForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        obj=form.save();
        try: mail_admins(f"Novo contato: {obj.subject}",f"{obj.name} <{obj.email}>\n\n{obj.message}",fail_silently=True)
        except Exception: pass
        messages.success(request,"Mensagem enviada! Nossa equipe entrará em contato.")
        return redirect("contact")
    return render(request,"portal/contact.html",{"form":form})

def newsletter(request):
    form=NewsletterForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        form.save(); messages.success(request,"Você entrou na nossa lista!"); return redirect(request.META.get("HTTP_REFERER","home"))
    return render(request,"portal/newsletter.html",{"form":form})

def signup(request):
    form=SignUpForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        user=form.save(); login(request,user); messages.success(request,"Conta criada com sucesso!"); return redirect("dashboard")
    return render(request,"registration/signup.html",{"form":form})

@login_required
def dashboard(request):
    appointments=Appointment.objects.filter(user=request.user).select_related("service")
    return render(request,"portal/dashboard.html",{"appointments":appointments,"upcoming":appointments.filter(date__gte=timezone.localdate(),status__in=["pending","confirmed"]).count()})

@login_required
def book_appointment(request):
    form=AppointmentForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        ap=form.save(commit=False); ap.user=request.user
        if ap.date < timezone.localdate(): form.add_error("date","Escolha uma data futura.")
        else: ap.save(); messages.success(request,"Agendamento enviado para confirmação!"); return redirect("dashboard")
    return render(request,"portal/appointment.html",{"form":form})

@login_required
def cancel_appointment(request,pk):
    ap=get_object_or_404(Appointment,pk=pk,user=request.user)
    if ap.status in ("pending","confirmed"): ap.status="cancelled"; ap.save(update_fields=["status"]); messages.info(request,"Agendamento cancelado.")
    return redirect("dashboard")
