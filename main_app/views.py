from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

finches = [
  Finch('Ryland', 'saffron', 'chill, muchos siestas', 3),
  Finch('Mehj', 'blue', 'pretty bird, sips tea', 2),
  Finch('Dave', 'spice', 'spicy-boy, charming cat-collector, flex-box girrrrl', 4),
  Finch('Devlin', 'society', 'HIGH-society', 4),
]

def home(request):
  return HttpResponse('<h1>FINCHCOLLECTIONS</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })
