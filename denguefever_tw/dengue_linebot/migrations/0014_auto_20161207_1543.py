# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dengue_linebot', '0013_auto_20161207_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botreplylog',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bot_reply_log', to='dengue_linebot.LineUser'),
        ),
        migrations.AlterField(
            model_name='messagelog',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_log', to='dengue_linebot.LineUser'),
        ),
        migrations.AlterField(
            model_name='responsetounrecogmsg',
            name='unrecognized_msg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proper_response', to='dengue_linebot.UnrecognizedMsg', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='responsetounrecogmsg',
            unique_together=set([]),
        ),
    ]