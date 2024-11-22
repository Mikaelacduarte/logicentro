from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

CARGO_CHOICES = [
    ('Fiscal', 'Fiscal'),
    ('Supervisor', 'Supervisor'),
    ('Administrador', 'Administrador'),
]

# Defina o UsuarioManager antes do modelo Usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, email, nome, password):
        if not email:
            raise ValueError("O usuário deve ter um email.")
        if not usuario:
            raise ValueError("O usuário deve ter um nome de usuário.")
        if not password:
            raise ValueError("O usuário deve ter uma senha.")
        user = self.model(
            usuario=usuario,
            email=self.normalize_email(email),
            nome=nome,
            is_active=True,  # Garantir que o campo is_active seja True ao criar o usuário
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, nome, password):
        user = self.create_user(
            usuario=usuario,
            email=email,
            nome=nome,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True  # Garantir que o superusuário tenha permissões de staff
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'tb_usuario'

    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    usuario = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(
        max_length=50,
        choices=CARGO_CHOICES,
        default='Fiscal'
    )
    situacao = models.CharField(max_length=1, choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A')
    is_active = models.BooleanField(default=True)  # Defini o campo is_active
    is_staff = models.BooleanField(default=False)  # Adicionado para controlar se o usuário é staff

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario', 'nome']

    objects = UsuarioManager()  # Agora o UsuarioManager está definido antes

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.cargo == 'Administrador' or self.usuario.lower() == 'admin'

    @property
    def is_active_user(self):
        return self.situacao == 'A'  # Verifica se o usuário está ativo com base no campo situacao
