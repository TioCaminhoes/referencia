from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portal.models import Service,Project,Post
from django.utils.text import slugify
class Command(BaseCommand):
    help="Cria conteúdo inicial demonstrativo."
    def handle(self,*args,**kwargs):
        services=[
        ("Desenvolvimento Web","Sites e sistemas rápidos, responsivos e escaláveis.","Construímos experiências digitais sob medida, com arquitetura segura, foco em performance e facilidade de manutenção.","⌘",1490,True),
        ("Design de Interfaces","Interfaces modernas que transformam visitantes em clientes.","Projetamos jornadas intuitivas, sistemas de design e interfaces consistentes para web e mobile.","✦",990,True),
        ("Automação de Processos","Menos tarefas repetitivas. Mais tempo para o que importa.","Integramos ferramentas e automatizamos rotinas para reduzir erros e acelerar sua operação.","⚡",790,False),
        ("Consultoria Digital","Estratégia, tecnologia e produto em uma visão única.","Diagnóstico técnico e estratégico para tirar projetos do papel com clareza e prioridades.","◎",590,False)]
        for name,short,desc,icon,price,feat in services:
            Service.objects.get_or_create(slug=slugify(name),defaults=dict(name=name,short_description=short,description=desc,icon=icon,price=price,featured=feat))
        projects=[("Plataforma Atlas","Produto Digital","Uma plataforma de gestão construída para simplificar operações e dar visão em tempo real.","Atlas Corp",2026,True),("Portal Aurora","Web","Portal institucional com arquitetura orientada a conteúdo e alta conversão.","Aurora",2026,True),("Flow Automations","Automação","Ecossistema de automações que reduziu tarefas manuais e centralizou indicadores.","Flow",2025,False)]
        for title,cat,summary,client,year,feat in projects: Project.objects.get_or_create(slug=slugify(title),defaults=dict(title=title,category=cat,summary=summary,description=summary+"\n\nProjeto desenvolvido com foco em experiência, desempenho e escalabilidade.",client=client,year=year,featured=feat))
        user=User.objects.filter(username="admin").first()
        if not user:
            user=User.objects.create_superuser("admin","admin@example.com","admin12345")
        posts=[("Como transformar uma ideia em produto digital","Da primeira hipótese ao lançamento: um caminho simples para organizar um projeto digital."),("5 decisões que melhoram uma interface","Pequenas decisões de UX podem tornar uma experiência muito mais clara."),("Automação sem complicação","Onde começar quando sua equipe perde tempo com tarefas repetitivas.")]
        for title,excerpt in posts: Post.objects.get_or_create(slug=slugify(title),defaults=dict(title=title,excerpt=excerpt,content=excerpt+"\n\nNeste artigo reunimos princípios práticos, exemplos e um roteiro para colocar a ideia em prática.",author=user,published=True))
        self.stdout.write(self.style.SUCCESS("Conteúdo demo criado. Login: admin / admin12345"))
