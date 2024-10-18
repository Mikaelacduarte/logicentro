from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
            nome=nome
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, nome, password):
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


class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    usuario = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=50)
    situacao = models.CharField(max_length=1, choices=[('A', 'Ativo'), ('I', 'Inativo')], default='A')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario', 'nome']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    @property
    def is_active(self):
        return self.situacao.lower() == 'A'.lower()

    @property
    def is_staff(self):
        return self.cargo.lower() == 'Administrador'.lower()

    @property
    def is_admin(self):
        return self.cargo.lower() == 'Administrador'.lower() or self.get_username() == 'admin'.lower()