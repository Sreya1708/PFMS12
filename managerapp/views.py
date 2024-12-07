from django.shortcuts import render

# Create your views here.
def managerhomepage(request):
    return render(request,'managerapp/managerhomepage.html')

