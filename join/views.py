from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .models import Join
from .forms import JoinForm


def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        return HttpResponseRedirect('/pages/thankyou')
    
    return render_to_response('join/home.html', locals(), context_instance=RequestContext(request))

#def thankyou():
    
#    return render_to_response('templates/thankyou.html', locals(), context_instance=RequestContext(request))
