from django.shortcuts import render, get_object_or_404

from .models import Author, Quote

def index(request):
    quotes = Quote.objects.prefetch_related('author').order_by('?')[:10]
    return render(request, 'index.html', { 'quotes': quotes })

def detail_by_id(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/detail.html', {'quote': quote})

def detail_by_author(request, slug):
    quotes = Quote.objects.prefetch_related('author').order_by('?').filter(author__slug=slug)
    return render(request, 'quotes/detail.html', {'quotes': quotes})
