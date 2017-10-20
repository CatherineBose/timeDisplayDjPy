from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
	context = {
	"time": strftime("%B %d,%Y %H:%M %p", gmtime()),
	"year": strftime("%Y", gmtime())
	}
	return render(request,'first_app/index.html', context)
