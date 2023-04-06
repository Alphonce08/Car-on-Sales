from django.shortcuts import render, redirect
from .models import Cars


def displayindex(request):
    return render(request, "index.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        carname = request.POST.get('carname')
        date = request.POST.get('date')
        client = request.POST.get('client')
        phonenum = request.POST.get('phonenum')

        query = Cars(name=name, phonenumber=phonenumber, carname=carname, date=date, client=client, phonenum=phonenum)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def index(request):
    data = Cars.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def deleteData(request, id):
    d = Cars.objects.get(id=id)
    d.delete()
    return redirect("/")
    return redirect(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        numplate = request.POST.get('numplate')
        date = request.POST.get('date')
        client = request.POST.get('client')
        phonenum = request.POST.get('phonenum')

        edit = Cars.objects.get(id=id)
        edit.name = name
        edit.phonenumber = phonenumber
        edit.carname = carname
        edit.date = date
        edit.client = client
        edit.phonenum = phonenum
        edit.save()
        return redirect("/")
    d = Cars.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
