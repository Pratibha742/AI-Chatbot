# Generated by Django 5.2.3 on 2025-07-10 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_chatsession_chatmessage_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chatbot.chatsession'),
        ),
    ]
