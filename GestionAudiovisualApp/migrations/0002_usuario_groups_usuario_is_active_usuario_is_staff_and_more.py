# Generated by Django 5.1.1 on 2025-03-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAudiovisualApp', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=123456, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tanda_labor',
            field=models.CharField(choices=[('Matutina', 'Matutina'), ('Vespertina', 'Vespertina'), ('Nocturna', 'Nocturna')], max_length=50),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
