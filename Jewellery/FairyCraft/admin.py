from django.contrib import admin
from .models import *

class DisplayStatus(admin.ModelAdmin):
    list_display = ('status_name', 'status_desc')
admin.site.register(Status, DisplayStatus)

class DisplayMetall(admin.ModelAdmin):
    list_display = ('ID_metallType', 'metall_name')
admin.site.register(Metall, DisplayMetall)

class DisplayJewType(admin.ModelAdmin):
    list_display = ('ID_jewType', 'jew_name')
admin.site.register(Jewellery_Type, DisplayJewType)

class DisplayRole(admin.ModelAdmin):
    list_display = ('role_name', 'role_desc')
admin.site.register(Role, DisplayRole)

class DisplayUser(admin.ModelAdmin):
    list_display = ('us_surname', 'us_name', 'mail_address', 'us_password', 'phone_num', 'role_id')
admin.site.register(User, DisplayUser)

class DisplayJewellery(admin.ModelAdmin):
    list_display = ('jewellery_name', 'jewellery_desc', 'jewellery_price', 'creationDate', 'jew_master', 'jewType_id', 'metalType_id', 'jewellery_img')
admin.site.register(Jewellery, DisplayJewellery)

class DisplayOrder(admin.ModelAdmin):
    list_display = ('status_id', 'client_id', 'jewellery_id', 'dateOfPrepare')
admin.site.register(Order, DisplayOrder)

@admin.register(Zapros1)
class Zapros1Admin(admin.ModelAdmin):
    list_display = ('jewellery',)

@admin.register(Zapros2)
class Zapros2Admin(admin.ModelAdmin):
    list_display = ('jewellery',)

@admin.register(Zapros3)
class Zapros3Admin(admin.ModelAdmin):
    list_display = ('order',)

@admin.register(Zapros4)
class Zapros4Admin(admin.ModelAdmin):
    list_display = ('order',)

@admin.register(Zapros5)
class Zapros5Admin(admin.ModelAdmin):
    list_display = ('jewType_id', 'count')

@admin.register(Zapros6)
class Zapros6Admin(admin.ModelAdmin):
    list_display = ('client_id', 'total')

@admin.register(Zapros7)
class Zapros7Admin(admin.ModelAdmin):
    list_display = ('jewellery',)

@admin.register(Zapros8)
class Zapros8Admin(admin.ModelAdmin):
    list_display = ('order',)

@admin.register(Zapros9)
class Zapros9Admin(admin.ModelAdmin):
    list_display = ('metalType_id', 'count')

@admin.register(Zapros10)
class Zapros10Admin(admin.ModelAdmin):
    list_display = ('master_id', 'jewType_id')