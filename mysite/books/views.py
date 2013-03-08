# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from books.forms import ContactForm


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.txt', {'books': books, 'query': q})
    return render_to_response('search_form.txt', {'errors': errors})


@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            # send_mail(
            #     request.POST['subject'],
            #     request.POST['message'],
            #     request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'],)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.txt', {'form': form})


def thanks(request):
    return render_to_response('thanks.txt')