from django.shortcuts import render
from .models import TrainData
from .forms import DForms
import preparedata

"""
This function translates form input into data which we can evaluate
and predict using sklearn
"""
def organizeFormData(req):
	organized = map(lambda x:req[x],req)
	del(organized[4])#csrf token
	print map(lambda x:int(x),organized)


def main(request):
    form = DForms()
    print preparedata.fitDataToPandas(TrainData.objects.all())
    if request.method == "POST":
    	organizeFormData(request.POST)
        return render(request, 'main.html', {})      
    return render(request, 'main.html', {'form':form})
