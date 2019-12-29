# Generated by Django 3.0.1 on 2019-12-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kurum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uye', models.CharField(max_length=50, verbose_name='Kurum Adı')),
                ('tanim', models.TextField(verbose_name='kurum Tanım')),
                ('kayit_tarih', models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')),
            ],
            options={
                'verbose_name': 'Kurumlar',
            },
        ),
    ]
