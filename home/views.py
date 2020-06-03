from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import userProfile,appoint

def index(request):
    id = request.user.id
    usersobj = User.objects.get(pk=id)
    user_profile = userProfile.objects.get(user=usersobj)
    appointments = appoint.objects.filter(pate=user_profile)
    if user_profile.is_doctor:
        return render(request,'doctordash.html')
    else:
        return render(request,'index.html',{'appointments':appointments})

def index2(request):
    return render(request,'accounts/register.html')

def doctors(request):
    doctors = userProfile.objects.filter(is_doctor = True)
    context = {'doctors':doctors}
    return render(request, 'doctors.html',context)

def doctorsingle(request, id):
    doctor = userProfile.objects.get(is_doctor = True, id=id)
    context = {'doctor':doctor}
    return render(request, 'doctorsingle.html',context)

def doctortime(request):
    doctor_id = request.user.id
    doctor = userProfile.objects.get(id=doctor_id)
    if request.method == "POST":
        fromm = request.POST.get("from")
        to = request.POST.get("to")
        doctor.appontment_availablity_from = fromm
        doctor.appontment_availablity_to = to
        doctor.save()
    
    return redirect('index')


