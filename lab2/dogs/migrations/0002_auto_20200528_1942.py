# Generated by Django 3.0.4 on 2020-05-28 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dogs.Club'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='expert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='perform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Perform'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Dog'),
        ),
        migrations.AlterField(
            model_name='perform',
            name='ring',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Ring'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Dog'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Show'),
        ),
        migrations.AlterField(
            model_name='ring',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dogs.Show'),
        ),
    ]
