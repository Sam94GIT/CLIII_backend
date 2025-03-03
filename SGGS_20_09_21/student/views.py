from django.shortcuts import render
from .models import Country , City
from .forms import studentform ,cityform

# Create your views here.

def create_view(request):
    if request.method == 'POST':
        student_form = studentform(request.POST or None)
        city_form = cityform(request.POST or None)

        if student_form.is_valid() and city_form.is_valid():
            student_form.save()
            city_form.save()
            return redirect('suggest_page')
    else:
        student_form = studentform()
        city_form = cityform()
        return render(request, 'myview.html', {'student_form': student_form, 'city_form': city_form})