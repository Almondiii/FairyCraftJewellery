from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *

#Функции перехода на другие страницы
def mainpage(request):
    return render(request, 'FairyCraft/main.html')

def katalog(request):
    return render(request, 'FairyCraft/katalog.html')

def account(request):
    return render(request, 'FairyCraft/account.html')

def chek(request):
    return render(request, 'FairyCraft/chek.html')

def mastera(request):
    return render(request, 'FairyCraft/mastera.html')

#Функции для CRUD операций над данными БД
    #Jewellery:

def katalog_view(request):
    jewellery_list = Jewellery.objects.order_by('ID_jewellery')
    context = {'jewellery_list':jewellery_list}
    return render(request, 'FairyCraft/katalog.html', context)

def new_jewellery(request):
    jewellery_list = Jewellery.objects.order_by('-creationDate')[:6]
    context = {'jewellery_list':jewellery_list}
    return render(request, 'FairyCraft/main.html', context)

def master_products_api(request, master_id):
    products = Jewellery.objects.filter(jew_master=master_id).values('jewellery_name', 'jewellery_img', 'jewellery_price', 'jew_master__us_name')
    return JsonResponse({'products': list(products)})

    #Mastera:

def mastera_view(request):
    master_role = Role.objects.get(role_name='Мастер')
    mastera_list = User.objects.filter(role_id=master_role)
    context = {'mastera_list':mastera_list}
    return render(request, 'FairyCraft/mastera.html', context)

def master_katalog(request, ID_user):
    jewellery_list = Jewellery.objects.filter(jew_master=ID_user)
    context = {'jewellery_list':jewellery_list}
    return render(request, 'FairyCraft/katalog.html', context)


    #User: Auth/Reg
def account_view(request):
    # Пример: получаем пользователя по ID из сессии или запроса
    user_id = request.session.get('user_id')  # или другой способ идентификации
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(user=user).order_by('-created_at')
    return render(request, 'account.html', {
        'user': user,
        'orders': orders,
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail_address']
            password = form.cleaned_data['us_password']
            try:
                user = User.objects.get(mail_address=mail, us_password=password)
                request.session['logged_user'] = {
                    'us_name': user.us_name,
                    'us_surname': user.us_surname,
                    'mail_address': user.mail_address,
                    'phone_num': user.phone_num,
                    'us_img': user.us_img.url if user.us_img else None,
                }
                return redirect('account')
            except User.DoesNotExist:
                messages.error(request, 'Неверный email или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем пользователя
            user = User(
                mail_address=form.cleaned_data['mail_address'],
                us_password=form.cleaned_data['us_password'],
                us_surname=form.cleaned_data['us_surname'],
                us_name=form.cleaned_data['us_name'],
                phone_num=form.cleaned_data['phone_num'],
                us_img=form.cleaned_data['us_img'],
                role_id_id=2
            )
            user.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь войдите в систему.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    if 'logged_user' in request.session:
        del request.session['logged_user']
    return redirect('login')