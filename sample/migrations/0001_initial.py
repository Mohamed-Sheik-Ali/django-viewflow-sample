# Generated by Django 3.2.5 on 2021-12-28 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0008_jsonfield_and_artifact'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorldProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.process')),
                ('text', models.CharField(max_length=150)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
