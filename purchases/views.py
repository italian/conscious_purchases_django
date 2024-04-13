import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PurchaseForm
from .models import Purchase
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse  # , HttpResponse
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = UserCreationForm()
    return render(request, 'purchases/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Обработка неудачной попытки входа
            messages.error(request, 'Неверное имя пользователя или пароль')
            return render(
                request,
                'purchases/login.html',
                {'error': 'Неверное имя пользователя или пароль'}
                )
    return render(request, 'purchases/login.html')


@login_required(login_url='/login/')
def home(request):
    purchases = Purchase.objects.filter(user=request.user)
    for purchase in purchases:
        # Вычисляем разницу во времени
        # между последним запросом и текущим временем
        time_diff = timezone.now() - purchase.last_purchase_date   # type: ignore # noqa: E501
        # Округляем до ближайшей секунды
        rounded_time_diff = timedelta(seconds=int(time_diff.total_seconds()))
        # Добавляем разницу во времени в объект покупки
        purchase.time_diff = rounded_time_diff   # type: ignore
    context = {
        'purchases': purchases,
        'is_home': True,
        }
    return render(request, 'purchases/home.html', context)


@login_required(login_url='/login/')
def checklist(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user
            purchase.last_purchase_date = timezone.now()

            # Поиск последней покупки этого товара
            # last_purchase = Purchase.objects.filter(
            #     user=request.user,
            #     item=purchase.item).order_by('-last_purchase_date').first()
            # if last_purchase:
            #     purchase.time_since_last_purchase = \
            #         purchase.last_purchase_date \
            #         - last_purchase.last_purchase_date
            # else:
            #     purchase.time_since_last_purchase = 0

            purchase.save()

            return render(
                request,
                'purchases/result.html',
                {'result': purchase.result},
                )

    else:
        form = PurchaseForm()
    return render(request, 'purchases/checklist.html', {'form': form})


@csrf_exempt
def submit_checklist_result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = data.get('item')
        result = data.get('result')
        user = request.user

        # Используем get_or_create для поиска или создания покупки
        purchase, created = Purchase.objects.get_or_create(
            user=user,
            item=item,
            defaults={
                'last_purchase_date': timezone.now(),
                'result': result,
            }
        )

        # Если покупка уже существует, обновляем ее поля
        if not created:
            purchase.last_purchase_date = timezone.now()
            purchase.result = result
            purchase.save()

        # Создаем новую запись в модели Purchase
        # purchase = Purchase(
        #     user=user,
        #     item=item,
        #     # date_added=datetime.now(),
        #     last_purchase_date=timezone.now(),
        #     result=result,
        # )

        # Поиск последней покупки этого товара
        last_purchase = Purchase.objects.filter(
            user=request.user,
            item=purchase.item).order_by('-last_purchase_date').first()

        if last_purchase and last_purchase.last_purchase_date:
            # Вычисляем разницу во времени и округляем до секунды
            time_diff = \
                purchase.last_purchase_date - last_purchase.last_purchase_date  # type: ignore # noqa: E501
            # Округляем до ближайшей секунды
            rounded_time_diff = timedelta(
                seconds=int(time_diff.total_seconds()))
            purchase.time_since_last_purchase = rounded_time_diff
        else:
            purchase.time_since_last_purchase = None

        purchase.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def about(request):
    return render(request, 'purchases/about.html')
