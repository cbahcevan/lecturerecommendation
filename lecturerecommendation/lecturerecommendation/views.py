from django.shortcuts import render
from .models import TrainData
from .forms import DForms
import preparedata
import recommend

"""
This function translates form input into data which we can evaluate
and predict using sklearn
"""
def organizeFormData(req):
	organized = map(lambda x:req[x],req)
	del(organized[4])#csrf token
	return map(lambda x:int(x),organized)


def main(request):
    form = DForms()
    """
    veritaanindaki traindatayi
    """
    if request.method == "POST":
<<<<<<< HEAD
    	userData = organizeFormData(request.POST)
        d = preparedata.fitDataToPandas(TrainData.objects.all())
        print recommend.evaluate(d[0],d[1],userData)

=======
    	evaluationData = organizeFormData(request.POST)
        databaseTrain = TrainData.objects.all()
        trainPrepared = preparedata.fitDataToPandas(databaseTrain)
>>>>>>> origin/master
        return render(request, 'main.html', {})      
    return render(request, 'main.html', {'form':form})
