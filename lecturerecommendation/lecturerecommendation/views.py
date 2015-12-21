from django.shortcuts import render
from .models import TrainData
from .forms import DForms
import preparedata

def main(request):
    form = DForms()
    print preparedata.fitDataToPandas(TrainData.objects.all())
    if request.method == "POST":
    	print request.POST['math']
    	if form.is_valid():
    	 print "valid oluyormu"
         form = DForms(request.POST)
         math= form.cleaned_data["math"]
         lit= form.cleaned_data ["lit"]
         return render(request, 'main.html', {})      
    return render(request, 'main.html', {'form':form})
