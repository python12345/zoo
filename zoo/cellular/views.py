from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse

from .models import Barzel, BarzelType

def index(request):
	barzel_list = get_list_or_404(Barzel.objects.all())
	btype_list = get_list_or_404(BarzelType.objects.all())
	context = {
		'barzel_list' : barzel_list,
		'btype_list' : btype_list,
	}

	if 'imei' in request.POST:
		add(request)

	return render(request, 'cellular/index.html', context)

def add(request):
	# try:
	btype_object = BarzelType.objects.get(name=request.POST['btype'])
	barzel_object = Barzel.objects.create(imei=request.POST['imei'])
	barzel_object.btype = btype_object
	barzel_object.save()
	return HttpResponse("GOOOD!")
	# except:
	# 	return HttpResponse("Something went wrong :(")