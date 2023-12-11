from django.shortcuts import render
from first_app.forms import StudentForm
# second way of importeing
# from first_app.views import home,about
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form':form})