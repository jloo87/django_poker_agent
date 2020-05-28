# Generated by Django 3.0.6 on 2020-05-28 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_remove_note_agent_player'),
        ('agents', '0022_auto_20200528_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentplayer',
            name='notes',
        ),
        migrations.AddField(
            model_name='agentplayer',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.Note'),
        ),
    ]
