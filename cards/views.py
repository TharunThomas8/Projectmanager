from django.shortcuts import render,redirect
from . forms import NewCard,NewChat
from django.http import HttpResponse
from . models import Cards,Chat
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
	chat = Chat.objects.filter(card__c_id=cid).order_by('id')
	if card != None:
		return render(request,'card.html',{'card':card,'chat':chat})
	else:
		return HttpResponse("Nopidy nope")

def add_chat(request,cid):
	# print (request)
	form = NewChat(request.POST or None)
	if form.is_valid():
		form.save()

	context = {'form': form,'cid':cid}
	return render(request,'add_chat.html',context)