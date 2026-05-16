from django.shortcuts import render, get_object_or_404
from .models import Circuit

def circuit_list(request):
    circuits = Circuit.objects.all()
    return render(request, 'circuits/circuit_list.html', {'circuits': circuits})

def circuit_detail(request, pk):
    circuit = get_object_or_404(Circuit, pk=pk)
    return render(request, 'circuits/circuit_detail.html', {'circuit': circuit})