from django.shortcuts import render,redirect
from . forms import NewCard
from django.http import HttpResponse
from . models import Cards
# Create your views here.

def add_card(request):
	# print (request)
	form = NewCard(request.POST or None)
	if form.is_valid():
		form.save()

	context = {'form': form}
	return render(request,'add_cards.html',context)

def view_card(request,cid):
	card = Cards.objects.filter(c_id=cid).first()
	if card != None:
		return render(request,'card.html',{'card':card})
	else:
		return HttpResponse("Nopidy nope")
