#O objetivo do documento models é definir tabelas e colunas do banco de dados em termos de classes e atributos.

# Nessa linha, estamos importando o módulo 'django.db' e 'models'. O primeiro contém classes e funções relacionadas à manipulação do banco de dados no Django.
# O 'models' é usado para definir tabelas e colunas do banco de dados em termos de classes Python.
from django.db import models

# Aqui, estamos importando 'AbstractBaseUser' e 'BaseUserManager', ambos da biblioteca 'django.contrib.auth.models'.
# 'AbstractBaseUser' permite que você crie seu próprio modelo de usuário personalizado, enquanto 'BaseUserManager' ajuda a gerenciar a criação de usuários.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Esta classe 'UsuarioManager' é um gerenciador de modelo personalizado que vai controlar como os usuários são criados no banco de dados.
# Ela estende a funcionalidade de 'BaseUserManager'.
class UsuarioManager(BaseUserManager):
     
     # Este método 'create_user' é responsável por criar um usuário comum.
    # Ele recebe como parâmetros o que está nos parênteses.
    def create_user(self, usuario, email, nome, password):
        
        # Os ifs irão verificar se o email, usuário e senha foram passados. Se não, lança um erro.
        if not email:
            raise ValueError("O usuário deve ter um email.")
        if not usuario:
            raise ValueError("O usuário deve ter um nome de usuário.")
        if not password:
            raise ValueError("O usuário deve ter uma senha.")
        
        # Cria um novo objeto de usuário (a instância do modelo 'Usuario'), normalizando o email (padronizando, geralmente em minúsculas).

        user = self.model(
            usuario=usuario,
            email=self.normalize_email(email),
            nome=nome
        )
        
        
        user.set_password(password) #Criptografa a senha
        user.save(using=self._db) # Salva o usuário no banco de dados
        return user

    def create_superuser(self, usuario, email, nome, password):
         # Cria um superusuário (administrador) reutilizando 'create_user'.
        if not email:
            raise ValueError("O usuário deve ter um email.")
        if not usuario:
            raise ValueError("O usuário deve ter um nome de usuário.")
        if not password:
            raise ValueError("O usuário deve ter uma senha.")
        user = self.create_user(
            usuario=usuario,
            email=email,
            nome=nome,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser): # Modelo de usuário personalizado, herda de 'AbstractBaseUser'
    
    id_usuario = models.AutoField(primary_key=True) # Chave primária gerada automaticamente.
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    usuario = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    situacao = models.CharField(max_length=1, choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A')

    USERNAME_FIELD = 'email'  #O campo principal para login será o email.
    REQUIRED_FIELDS = ['usuario', 'nome'] # Campos obrigatórios além do email.

    objects = UsuarioManager() # Define 'UsuarioManager' como o gerenciador do modelo.

    def __str__(self):
        return self.email # Exibe o email como representação do objeto.

    @property
    def is_active(self):
        return self.situacao.lower() == 'A'.lower() # Verifica se o usuário está ativo.

    @property
    def is_staff(self):
        return self.cargo.lower() == 'Administrador'.lower() # Verifica se o usuário faz parte da equipe administrativa

    @property
    def is_admin(self):
        return self.cargo.lower() == 'Administrador'.lower() or self.get_username() == 'admin'.lower()  # Verifica se o usuário é um administrador.