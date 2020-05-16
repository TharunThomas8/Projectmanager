from django.shortcuts import render,redirect
from django.views import generic
from datetime import datetime, timedelta, date
from datetime import datetime
from . forms import NewCard,NewChat
from django.http import HttpResponse
from .utils import Calendar
from django.utils.safestring import mark_safe
from . models import Cards,Chat
import calendar
# Create your views here.

def add_card(request):
	# print (request)
	form = NewCard(request.POST or None,request.FILES or None)
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
    form = NewChat(request.POST or None,request.FILES or None)
    if form.is_valid():
        print (form)
        form.save()

    context = {'form': form,'cid':cid}
    return render(request,'add_chat.html',context)

class CalendarView(generic.ListView):
    model = Cards
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month