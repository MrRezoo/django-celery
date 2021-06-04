from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from home.forms import NumberForm
from home.models import Number
from home.tasks import adding


def home(request):
    numbers = Number.objects.all()
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            num = Number(x=data['x'], y=data['y'])
            num.save()
            result = adding.delay(data['x'], data['y'], num.id)
            num.task_id = result.id
            num.save()
            return redirect('home:home')
    else:
        form = NumberForm()
    return render(request, 'home/home.html', {'form': form, 'numbers': numbers})


def nums(request, num_id):
    num = get_object_or_404(Number, pk=num_id)
    return render(request, 'home/nums.html', {'num': num})
