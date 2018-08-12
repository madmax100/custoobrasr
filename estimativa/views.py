from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.urls import reverse

from .forms import ProjPadraoForm
from .models import ProjPadrao

def home(request): 
    if request.method == 'POST':
        form=ProjPadraoForm(request.POST)
        if form.is_valid():
            ppadrao = form.save(commit=False)
            ppadrao.save()     
        return render(request, 'estimativa/calculo.html')
    else:
        form=ProjPadraoForm()
    return render(request, 'estimativa/home.html', {'form': form})

def calculo(request):
    return render(request, 'estimativa/calculo.html')