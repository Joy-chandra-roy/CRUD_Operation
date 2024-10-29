from django.shortcuts import render
from myapp.models import student

# Create your views here.
def home(request):
    if request.method=="POST":
        sname=request.POST.get('n')
        sdep=request.POST.get('dp')
        sroll=request.POST.get('r')
        simage=request.FILES.get('Im')

        obj=student()
        obj.name=sname
        obj.dep=sdep
        obj.roll=sroll
        obj.image=simage
        obj.save()
    data=student.objects.all()
    return render(request,"index.html",{"d":data})