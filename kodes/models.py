from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

import uuid

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey('kodes.Usuario', on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True 

class Empresa(models.Model):
    documento = models.CharField(
        max_length = 20,
        help_text = 'RUC y/o CI N°',
        unique = True 
    )
    razonsocial = models.CharField(
        max_length = 150,
        help_text = 'Razón Social'
    )
    pais = models.CharField(
        max_length = 50,
        help_text = 'País'
    )
    departamento = models.CharField(
        max_length = 50,
        help_text = 'Departamento'
    )
    ciudad = models.CharField(
        max_length = 50,
        help_text = 'Ciudad'
    )
    direccion = models.CharField(
        max_length = 200,
        help_text = 'Dirección',
        null=True, blank=True
    ) 
    correo = models.CharField(
        max_length = 250,
        help_text = 'Correo',
        null=True, blank=True

    )      
    telefono = models.CharField(
        max_length = 30,
        help_text = 'Teléfono',
        null=True, blank=True
    )          
    token = models.CharField(
        max_length = 250,
        help_text = 'Token',
        null=True, blank=True,
        default='__@'
    )       
    estado = models.IntegerField(
        help_text = 'Estado',
        default=1
    )
    logo = models.ImageField(
        help_text = 'Logo',
        upload_to = 'fotos/',
        null = True, blank = True 

    )       
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.razonsocial, self.documento)

    def save(self):
        self.razonsocial = self.razonsocial.upper()
        self.direccion = self.direccion.upper()
        self.pais = self.pais.upper()
        self.ciudad = self.ciudad.upper()
        self.departamento = self.departamento.upper()
        super(Empresa, self).save()

    class Meta:
        verbose_name_plural = "Empresas"    


class Usuario(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(verbose_name='emails', unique=True, max_length=255)
    genero = models.CharField(max_length=1, blank=True, default='M')
    avatar = models.ImageField(upload_to='fotos/', blank=True)
    mobile_no = models.CharField(max_length=20)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)    
    profile_picture =  models.ImageField(
        help_text = 'Logo',
        upload_to = 'fotos/',
        null = True, blank = True )
    admin = models.BooleanField(default=False)
    vendedor = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['empresa_id','genero', 'username']

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'


class UserManager(BaseUserManager):
    def create_superuser(self, *, email, password=None, empresa, genero):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.empresa_id = empresa_id
        user.genero = genero
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user
