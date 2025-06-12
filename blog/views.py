from django.shortcuts import render

def home(requet):
    return render(requet, 'index.html')