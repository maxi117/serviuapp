from django.shortcuts import render
from serviuApp.forms import CreateSubsidioForm
from serviuApp.models import Subsidio

# Create your views here.
def index(request):
    subsidios = Subsidio.objects.all()
    data = {'subsidios': subsidios}
    return render(request, 'serviuApp/index.html', data)

def crear(request):
    form = CreateSubsidioForm()
    if request.method == 'POST' :
        form = CreateSubsidioForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'serviuApp/crear.html', data)

