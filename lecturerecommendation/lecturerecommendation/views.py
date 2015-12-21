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
         print form.cleaned_data["math"]
         return render(request, 'main.html', {})      
    return render(request, 'main.html', {'form':form})
