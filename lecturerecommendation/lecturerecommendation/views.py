from django.shortcuts import render
from .forms import DForms
def main(request):
    form = DForms()
    if request.method == "POST":
    	if form.is_valid():
    	 print "valid oluyormu"
         form = DForms(request.POST)
         print form.cleaned_data["math"]
         return render(request, 'main.html', {})      
    return render(request, 'main.html', {'form':form})
