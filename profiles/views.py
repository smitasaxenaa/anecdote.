from django.shortcuts import render

def sde(request):
    return render(request, 'profiles/sde.html')

def businessanalyst(request):
    return render(request,"profiles/ba.html")

def datascience(request):
    return render(request,"profiles/ds.html")

def product(request):
    return render(request,"profiles/product.html")

def coreelectrical(request):
    return render(request,"profiles/coreelectrical.html")

def cna(request):
    return render(request,"profiles/cna.html")
