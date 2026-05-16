from django.shortcuts import render
from .models import GlossaryTerm

def glossary_list(request):
    terms = GlossaryTerm.objects.all()
    return render(request, 'glossary/glossary_list.html', {'terms': terms})
