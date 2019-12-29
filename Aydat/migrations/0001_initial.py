# Generated by Django 3.0.1 on 2019-12-29 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tanim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurum', models.CharField(max_length=50, verbose_name='Kurum')),
                ('kurum_yonetici', models.CharField(max_length=50, verbose_name='Yönetici')),
                ('kayit_tarih', models.DateTimeField(auto_now_add=True, verbose_name='Giris')),
            ],
        ),
        migrations.CreateModel(
            name='Uye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Adı')),
                ('sur_Name', models.CharField(max_length=50, verbose_name='Soyadı Adı')),
                ('Commet', models.CharField(max_length=150, verbose_name='Açıklama')),
                ('Uye_no', models.CharField(max_length=10, verbose_name='No')),
                ('Tarih', models.DateTimeField(auto_now_add=True, verbose_name='Giriş')),
                ('kurum', models.ManyToManyField(to='Aydat.Tanim')),
            ],
        ),
    ]
