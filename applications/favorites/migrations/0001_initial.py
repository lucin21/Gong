# Generated by Django 4.1.3 on 2022-12-05 16:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_favorites', to='job_offers.job')),
            ],
            options={
                'verbose_name': 'Trabajo Favorito',
                'verbose_name_plural': 'Trabajos Favoritos',
            },
        ),
    ]
