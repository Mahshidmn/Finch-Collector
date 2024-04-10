from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy

from django.urls import reverse

from .forms import FeedingForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', {
         'finchs': finchs
    })

def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    current_toy_ids = finch.toys.all().values_list('id')
    available_toys = Toy.objects.exclude(id__in=current_toy_ids)
    return render(request, 'finchs/detail.html', {
        'finch' : finch,
        'feeding_form': feeding_form,
        'available_toys': available_toys,
        
    })

def add_feeding(request, finch_id):
    feeding_form = FeedingForm(request.POST)
    if feeding_form.is_valid():
        new_feeding = feeding_form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'variety', 'description', 'age', 'sex']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['variety', 'description', 'age', 'sex']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs/' #TODO get reverse function work


#############Toy CRUD ###################
class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/' # TODO: Dont Hardcode -- use reverese

def add_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)
