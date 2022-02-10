from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, House
from .forms import WatchingForm
# from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.houses.all().values_list('id')
  houses_finch_doesnt_have = House.objects.exclude(id__in=id_list)
  watching_form = WatchingForm()
  return render(request, 'finches/detail.html', {'finch': finch,
  'watching_form': watching_form, 
  'houses': houses_finch_doesnt_have,
  })

def add_watching(request, finch_id):
  form = WatchingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_watching = form.save(commit=False)
    new_watching.finch_id = finch_id
    new_watching.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = "__all__"

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['type', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def houses_index(request):
  houses = House.objects.all()
  return render(request, 'houses/index.html', {'houses': houses})

def house_detail(request, house_id):
  house = House.objects.get(id=house_id)
  return render(request, 'houses/detail.html', {'house': house})

class HouseCreate(CreateView):
  model = House
  fields = "__all__"

class HouseUpdate(UpdateView):
  model = House
  fields = ['name', 'color']

class HouseDelete(DeleteView):
  model = House
  success_url = '/houses/'

def assoc_house(request, finch_id, house_id):
  finch = Finch.objects.get(id=finch_id)
  finch.houses.add(house_id)
  return redirect ('detail', finch_id=finch_id)

def un_assoc_house(request, finch_id, house_id):
  finch = Finch.objects.get(id=finch_id)
  finch.houses.remove(house_id)
  return redirect ('detail', finch_id=finch_id)

