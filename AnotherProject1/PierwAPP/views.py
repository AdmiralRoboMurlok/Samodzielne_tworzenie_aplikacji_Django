from django.shortcuts import render
from .models import Chusteczki
# Create your views here.
def main(request):
    Model_Data = Chusteczki.objects.all()
    return render(request, 'index.html', context={
        "HTML_DATA": Model_Data
    })