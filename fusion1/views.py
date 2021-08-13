from django.shortcuts import render,HttpResponse,redirect
from .models import userform
from django.core.mail import send_mail
from django.forms import forms
# Create your views here.
def index(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d=request.POST.get('dob')
        e=request.POST.get('email')
        p=request.POST.get('phone')
        if e and userform.objects.filter(email=e).count() > 0:
            error_msg='this email id is alredy exits please use another'
            c={'error':error_msg}
            return render(request,'index.html',c)
        elif p and userform.objects.filter(phone_number=p).count() > 0:
            error_msg = 'this mobile no is alredy exits please use another'
            c = {'error': error_msg}
            return render(request, 'index.html', c)

        else:



            send_mail(
                'Thanks for register stackfusion',
                'Hi {},\nyour form successfully applied and i will conduct you as soon as possible.'
                '\n\n Thanks and Regards\nVinod Pal'.format(n),
                'palvinodr1996@gmail.com',
                [e],
                fail_silently=False,
                                  )
            data=userform()
            data.name=n
            data.dob=d
            data.email=e
            data.phone_number=p
            data.save()
            return redirect('/showall')
    return render(request,'index.html')


def showallsub_data(request):
    data=userform.objects.all().order_by('-id')
    context={'data':data}
    return render(request,'alluser.html',context)

