from django.db import models
from django.contrib.auth.models import AbstractUser

#Определение моделей для взаимодействия (создание таблиц в БД)
class Status(models.Model):
    ID_status = models.AutoField(primary_key=True, null=False) #Автоматический первичный ключ
    status_name = models.CharField(null=False, blank=False) #Null - не может быть нулевым значением, blank - обязательно должен быть заполнен
    status_desc = models.TextField(null=True, blank=True)

class Metall(models.Model):
    ID_metallType = models.AutoField(primary_key=True, null=False)
    metall_name = models.CharField(null=False, blank=False)

class Jewellery_Type(models.Model):
    ID_jewType = models.AutoField(primary_key=True)
    jew_name = models.CharField(null=False)

class Role(models.Model):
    ID_role = models.AutoField(primary_key=True, null=False)
    role_name = models.CharField(null=False, blank=False)
    role_desc = models.CharField(null=True)

class User(models.Model):
    ID_user = models.AutoField(primary_key=True, null=False)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=False, blank=False) #Внешний ключ, удаляется при удалении роли
    mail_address = models.EmailField(unique=True, blank=False, null=False) #Тип данных для автоматической проверки на соответствие введенных данных типу почта, unique - каждая почта уникальна (1 пользователь с такой почтой)
    us_password = models.CharField(null=False, blank=False)
    us_surname = models.CharField(null=False, blank=False)
    us_name = models.CharField(null=False, blank=False)
    phone_num = models.CharField(null=False, blank=False)
    in_job = models.IntegerField(null=True, blank=True)
    us_img = models.ImageField(upload_to='img/', null=True, blank=True)
    
class Jewellery(models.Model):
    ID_jewellery = models.AutoField(primary_key=True, null=False)
    jewellery_name = models.CharField(null=False, blank=False)
    jewellery_desc = models.CharField(null=False, blank=False)
    jewellery_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False) #max_digits - максимальное количество знаков до запятой, decimal_places - максимальное количество знаков после запятой
    jew_master = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    jewType_id = models.ForeignKey(Jewellery_Type, on_delete=models.CASCADE, null=False, blank=False)
    metalType_id = models.ForeignKey(Metall, on_delete=models.CASCADE, null=False, blank=False)
    creationDate = models.DateField(help_text="Введите дату в формате ГГГГ-ММ-ДД", null=False, blank=False)
    jewellery_img = models.ImageField(upload_to='img/', null=True, blank=True)

class Order(models.Model):
    ID_order = models.AutoField(primary_key=True, null=False)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, null=False, blank=False)
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    jewellery_id = models.ForeignKey(Jewellery, on_delete=models.CASCADE, null=False, blank=False)
    dateOfPrepare = models.DateField(help_text="Введите дату в формате ГГГГ-ММ-ДД", null=False, blank=False)

class Zapros1(models.Model):
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Изделия мастера'
        verbose_name_plural = 'Изделия мастера'
    def __str__(self):
        return str(self.jewellery)
    
class Zapros2(models.Model):
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Изделия дороже суммы'
        verbose_name_plural = 'Изделия дороже суммы'
    def __str__(self):
        return str(self.jewellery)
    
class Zapros3(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Заказы клиента'
        verbose_name_plural = 'Заказы клиента'
    def __str__(self):
        return str(self.order)

class Zapros4(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Заказы мастера'
        verbose_name_plural = 'Заказы мастера'
    def __str__(self):
        return str(self.order)

class Zapros5(models.Model):
    jewType_id = models.ForeignKey(Jewellery_Type, on_delete=models.CASCADE)
    count = models.IntegerField()
    class Meta:
        verbose_name = 'Заказы по типу изделия'
        verbose_name_plural = 'Заказы по типу изделия'
    def __str__(self):
        return f"{self.jewType_id} — {self.count}"
    
class Zapros6(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Клиенты с суммой заказов выше значения'
        verbose_name_plural = 'Клиенты с суммой заказов выше значения'
    def __str__(self):
        return f"{self.client_id} — {self.total}"
    
class Zapros7(models.Model):
    jewellery = models.ForeignKey(Jewellery, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Изделия после года'
        verbose_name_plural = 'Изделия после года'
    def __str__(self):
        return str(self.jewellery)
    
class Zapros8(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Заказы в интервале дат'
        verbose_name_plural = 'Заказы в интервале дат'
    def __str__(self):
        return str(self.order)
    
class Zapros9(models.Model):
    metalType_id = models.ForeignKey(Metall, on_delete=models.CASCADE)
    count = models.IntegerField()
    class Meta:
        verbose_name = 'Изделия по материалу'
        verbose_name_plural = 'Изделия по материалу'
    def __str__(self):
        return f"{self.metalType_id} — {self.count}"
    
class Zapros10(models.Model):
    jewType_id = models.ForeignKey(Jewellery_Type, on_delete=models.CASCADE)
    master_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Мастера по типу изделия'
        verbose_name_plural = 'Мастера по типу изделия'
    def __str__(self):
        return f"{self.master_id} — {self.jewType_id}"
    