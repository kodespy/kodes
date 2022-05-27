# Generated by Django 4.0.3 on 2022-05-26 11:51

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(help_text='RUC y/o CI N°', max_length=20, unique=True)),
                ('razonsocial', models.CharField(help_text='Razón Social', max_length=150)),
                ('pais', models.CharField(help_text='País', max_length=50)),
                ('departamento', models.CharField(help_text='Departamento', max_length=50)),
                ('ciudad', models.CharField(help_text='Ciudad', max_length=50)),
                ('direccion', models.CharField(blank=True, help_text='Dirección', max_length=200, null=True)),
                ('correo', models.CharField(blank=True, help_text='Correo', max_length=250, null=True)),
                ('telefono', models.CharField(blank=True, help_text='Teléfono', max_length=30, null=True)),
                ('token', models.CharField(blank=True, default='__@', help_text='Token', max_length=250, null=True)),
                ('estado', models.IntegerField(default=1, help_text='Estado')),
                ('logo', models.ImageField(blank=True, help_text='Logo', null=True, upload_to='fotos/')),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='emails')),
                ('genero', models.CharField(blank=True, default='M', max_length=1)),
                ('avatar', models.ImageField(blank=True, upload_to='fotos/')),
                ('mobile_no', models.CharField(max_length=20)),
                ('profile_picture', models.ImageField(blank=True, help_text='Logo', null=True, upload_to='fotos/')),
                ('admin', models.BooleanField(default=False)),
                ('vendedor', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kodes.empresa')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
