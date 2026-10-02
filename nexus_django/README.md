# NEXUS — Django Professional Starter

Projeto web completo em Django, em português do Brasil, com interface responsiva e área pública + área autenticada.

## O que já vem pronto

- Página inicial profissional e responsiva
- Serviços e páginas individuais
- Portfólio/projetos
- Blog/conteúdos
- Formulário de contato
- Newsletter
- Cadastro e login de usuários
- Painel do cliente
- Agendamento de serviços
- Cancelamento de agendamento
- Django Admin para gerenciar serviços, projetos, posts, contatos, newsletter e agendamentos
- Busca na página inicial
- Mensagens de feedback
- SQLite configurado para começar sem configuração de banco
- Conteúdo demo criado automaticamente
- Configuração por variáveis de ambiente
- Segurança básica ativada
- CSS/JS próprios, sem framework externo obrigatório
- Scripts de inicialização para Windows e Linux/macOS

## Requisitos

Python 3.12+ (Django 6.1 suporta Python 3.12, 3.13 e 3.14).

## Windows

Dê duplo clique em `run.bat` ou execute:

```bat
run.bat
```

O script cria o ambiente virtual, instala as dependências, executa as migrations, cria o conteúdo demonstrativo e inicia o servidor.

## Linux/macOS

```bash
chmod +x run.sh
./run.sh
```

Depois abra `http://127.0.0.1:8000/`.

## Acesso administrativo demo

- Usuário: `admin`
- Senha: `admin12345`
- Admin: `http://127.0.0.1:8000/admin/`

**Troque a senha imediatamente em um ambiente real.**

## Configuração de produção

Copie `.env.example` para `.env` e defina pelo menos uma `SECRET_KEY` forte, `DEBUG=False` e os hosts permitidos. O arquivo `.env` não deve ser versionado.

Para produção real, configure também HTTPS, banco PostgreSQL, e-mail SMTP, armazenamento de mídia e um servidor WSGI/ASGI/reverse proxy.
