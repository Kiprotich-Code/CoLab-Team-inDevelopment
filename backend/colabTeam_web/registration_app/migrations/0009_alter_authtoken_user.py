# Generated by Django 4.2.7 on 2023-11-18 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration_app", "0008_alter_authtoken_ip_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authtoken",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="auth_token",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]