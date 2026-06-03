from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def predict(request):
    return render(request, 'ml/predict.html')