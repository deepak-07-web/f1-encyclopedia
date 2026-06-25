from django.shortcuts import render
from .models import TerminologyTerm

def terminology_list(request):
    terms = TerminologyTerm.objects.all()
    return render(request, 'terminology/terminology_list.html', {'terms': terms})
