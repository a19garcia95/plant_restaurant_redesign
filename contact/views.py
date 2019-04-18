from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def send_email(request):
    '''if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_email(name, phone, message, from_email, ['admin@example.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')

    else:
        form = ContactForm()'''

    context = {
        
    }

    return render(request, 'contact/contact.html', context)

def send_success(request):
    pass