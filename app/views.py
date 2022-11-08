from django.http import HttpResponse
from django.shortcuts import render
from .models import Donor, DonorRegister
from PIL import Image, ImageDraw, ImageFont
from django.views.decorators.csrf import csrf_exempt
import datetime
from .serializers import DonorRegisterSerialiser

@csrf_exempt
def index(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        password= request.POST['password']  
        print(fname, email, password)
        e_mail = DonorRegister.objects.filter(email = email).distinct()
        if e_mail == email:
            DonorRegister.objects.get(email = e_mail).delete()
            print("Duplicate accounts")
        else:
            ins = DonorRegister.objects.create(full_name = fname, email = email, password = password)
            ins.save()

            img = Image.open("C:\\Users\\navee\\django_application\\blood_app\\backend\\media\\certi.png", mode='r')
            font = ImageFont.truetype(
                "C:\\Users\\navee\\AppData\\Local\\Microsoft\\Windows\\Fonts\\GILROY-EXTRABOLD.otf",
                48
            )

            today = datetime.date.today()
            
            draw = ImageDraw.Draw(img)
            draw.text(((img.width)/2-100, 430), fname, font= font, fill='black')
            draw.text(((img.width)/2-140, 640), today.strftime("%dth %b %y"), font= font, fill='black')

            img.save("{}.png".format(fname))
        return render(request, 'sucess.html')
    return render(request, 'index.html')



def home(request):
    return render(request, 'home.html')


