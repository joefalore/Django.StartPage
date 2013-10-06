from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponseRedirect

from .models import Contact
from .forms import ContactForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        return HttpResponseRedirect('/pages/received')
    
    return render_to_response('contact/contact.html', locals(), context_instance=RequestContext(request))

