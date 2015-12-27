from django.shortcuts import render
from .models import TrainData,Lectures
from .forms import DForms
import preparedata
import recommend

"""
This function translates form input into data which we can evaluate
and predict using sklearn
"""

def getFromLectures(lecid):
    L = Lectures.objects.get(lecid=lecid)
    return L.lecexp


def loadLectureDetails(req):
	expla = Lectures.objects.get(lecid=str(req[0]))
	result = expla.lecture_explanation
	return result


def organizeFormData(req):
	organized = map(lambda x:req[x],req)
	del(organized[5])#csrf tokens
	return map(lambda x:int(x),organized)




def main(request):
    form = DForms()
    """
    veritaanindaki traindatayi
    """
    if request.method == "POST":

    	userData = organizeFormData(request.POST)
        d = preparedata.fitDataToPandas(TrainData.objects.all())
        result= recommend.evaluate(d[0],d[1],userData)

        explanation = getFromLectures(str(result[0]))
        print str(result[0])
        

        return render(request, 'main.html', {'rec':explanation,'ders':str(result[0])})      




        exp =  loadLectureDetails(result)
        return render(request, 'main.html', {'rec':str(exp)})
    return render(request, 'main.html', {'form':form})
