from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Tanim(models.Model):

    kurum = models.CharField(verbose_name=("Kurum"), max_length=50)
    kurum_yonetici = models.ForeignKey(settings.AUTH_USER_MODEL, default=True, on_delete=models.SET(get_sentinel_user))

    kayit_tarih =models.DateTimeField(verbose_name=("Giris"), auto_now_add = True)

    def kayit_time(self):
        return self.kayit_tarih >= timezone.now() - datetime.timedelta(days=1)




class Uye(models.Model):
    kurum = models.ForeignKey('Aydat.Tanim', on_delete=models.CASCADE, related_name='Kurum', default=True)
    Name=models.CharField(verbose_name=("Adı"), max_length=50)
    sur_Name = models.CharField(verbose_name = ("Soyadı Adı"), max_length = 50)
    Commet = models.CharField(verbose_name = ("Açıklama"), max_length = 150)
    Uye_no =models.CharField(verbose_name=("No"), max_length = 10)
    Tarih =models.DateTimeField(verbose_name=("Giriş"), auto_now_add = True)


    def kayit_t(self):
        return self.Tarih >= timezone.now() - datetime.timedelta(days=1)

class Odeme(models.Model):
    uye = models.ForeignKey('Aydat.Uye', on_delete=models.CASCADE)
    alinan =models.CharField(verbose_name="Ödenen", max_length=10)
    Tarih_odeme = models.DateTimeField(verbose_name="Tarih", auto_now_add=True)

    def ode_tarih(self):
        return self.Tarih_odeme >= timezone.now() - datetime.timedelta(days=1)


# Create your models here.
