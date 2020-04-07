from django.shortcuts import render
from .models import Product
from .models import Male_Cap
from .models import Male_Earring
from .models import Male_Eyeglasse
from .models import Male_Necklace
from .models import Female_Cap
from .models import Female_Earring
from .models import Female_Eyeglasse
from .models import Female_Necklace
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserForm
import cv2
import numpy as np
import dlib
from math import hypot   
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import(TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.shortcuts import redirect
import os
import sqlite3
"""products = [
    {
        'product_name':'Eyeglasses1',
        'brand':'Rayban',
        'price':'300',
        'date_added':'June 26, 2019'
    },
    {
        'product_name':'Eyeglasses2',
        'brand':'Tom Ford',
        'price':'500',
        'date_added':'June 27, 2019'
    }
]"""



    #from blog.models import Post
    #from django.contrib.auth.models import User
    #product = Product(product_name='adf',brand='asd',price=11,stock=123,script='asd',image_directory='ad',buyer=user)
    # return render(request, 'product/home.html')
    # context = {
    #     'products': Product.objects.all()
    # }

def male_products(request):
    return render(request, 'product/male_products.html')

def male_eyeglasses(request):
    context = {
        'products' : Male_Eyeglasse.objects.all()
    }
    return render(request, 'product/male_eyeglasses.html', context)

def male_necklace(request):
    context = {
        'products' : Male_Necklace.objects.all()
    }
    return render(request, 'product/male_necklace.html', context)

def male_caps(request):
    context = {
        'products' : Male_Caps.objects.all()
    }
    return render(request, 'product/male_caps.html', context)

def male_earrings(request):
    context = {
        'products' : Male_Earrings.objects.all()
    }
    return render(request, 'product/male_earrings.html', context)
    

def female_products(request):
    product = Product.objects.all()
    return render(request, 'product/female_products.html')

def female_eyeglasses(request):
    context = {
        'products' : Female_Eyeglasse.objects.all()
    }
    return render(request, 'product/female_eyeglasses.html', context)

def female_necklace(request):
    context = {
        'products' : Female_Necklace.objects.all()
    }
    return render(request, 'product/female_necklace.html', context)

def female_caps(request):
    context = {
        'products' : Female_Cap.objects.all()
    }
    return render(request, 'product/female_caps.html', context)

def female_earring(request):
    context = {
        'products' : Female_Earring.objects.all()
    }
    return render(request, 'product/female_earring.html', context)


def about(request):
    return render(request, 'product/about.html')

def home(request):
    return render(request, 'product/home.html')

def customer(request):
    return render(request, 'product/customer.html')

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product/female_caps.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'product'
#     ordering = ['-date_added']

class VideoCamera(object):
    def face_detect(request, pk):
        import cv2
        import numpy as np
        import dlib
        from math import hypot
        # from .models import Female_Cap

        # Loading Camera and Nose image and Creating mask
        # 'products' : Female_Earring.objects.all()
        cap = cv2.VideoCapture(0)
        id_pk = int(pk)
        # nose_image = cv2.imread("C:/Users/Cossette/Desktop/New folder/pig_nose.png")
        image = str(Female_Cap.objects.get(id=pk))
        
        print(image)
        # nose_image = cv2.imread("media/product_pic/facemarks_points.png")
        nose_image = cv2.imread(image[1:])
        _, frame = cap.read()
        rows, cols, _ = frame.shape
        nose_mask = np.zeros((rows, cols), np.uint8)

        # Loading Face detector
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("C:/Users/Cossette/Desktop/New folder/shape_predictor_68_face_landmarks.dat")

        while True:
            _, frame = cap.read()
            nose_mask.fill(0)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = detector(frame)
            for face in faces:
                landmarks = predictor(gray_frame, face)

                # Nose coordinates
                # top_nose = (landmarks.part(29).x, landmarks.part(29).y)
                # center_nose = (landmarks.part(30).x, landmarks.part(30).y)
                # left_nose = (landmarks.part(31).x, landmarks.part(31).y)
                # right_nose = (landmarks.part(35).x, landmarks.part(35).y)

                top_nose = (landmarks.part(27).x, landmarks.part(27).y)
                center_nose = (landmarks.part(28).x, landmarks.part(28).y)
                left_nose = (landmarks.part(19).x, landmarks.part(19).y)
                right_nose = (landmarks.part(25).x, landmarks.part(25).y)

                # nose_width = int(hypot(left_nose[0] - right_nose[0],
                #                 left_nose[1] - right_nose[1]) * 1.7)
                # nose_height = int(nose_width * 0.77)

                nose_width = int(hypot(left_nose[0] - right_nose[0],
                                left_nose[1] - right_nose[1]) * 1.7)
                nose_height = int(nose_width * 0.75)

                # New nose position
                top_left = (int(center_nose[0] - nose_width / 2),
                                    int(center_nose[1] - nose_height / 2))
                bottom_right = (int(center_nose[0] + nose_width / 2),
                            int(center_nose[1] + nose_height / 2))


                # Adding the new nose
                nose_pig = cv2.resize(nose_image, (nose_width, nose_height))
                nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
                _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)

                nose_area = frame[top_left[1]: top_left[1] + nose_height,
                            top_left[0]: top_left[0] + nose_width]
                nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
                final_nose = cv2.add(nose_area_no_nose, nose_pig)

                frame[top_left[1]: top_left[1] + nose_height,
                            top_left[0]: top_left[0] + nose_width] = final_nose

                # cv2.imshow("Nose area", nose_area)
                # cv2.imshow("Nose pig", nose_pig)
                # cv2.imshow("final nose", final_nose)



            cv2.imshow("Frame", frame)



            key = cv2.waitKey(1)
            if key == 27:
                cap.release()
                break
        return redirect('/gender_select')

    def face_detect3(request, pk):
        import cv2

        id_pk = int(pk)
        image = str(Female_Cap.objects.get(id=pk))

        face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # hat=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/hat.png')
        hat=cv2.imread(image[1:])
        # glass=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/glasses.png')
        # dog=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/dog.png')

        # def put_dog_filter(dog, fc, x, y, w, h):
        #     face_width = w
        #     face_height = h

        #     dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
        #     for i in range(int(face_height * 1.75)):
        #         for j in range(int(face_width * 1.5)):
        #             for k in range(3):
        #                 if dog[i][j][k] < 235:
        #                     fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
        #     return fc

        def put_hat(hat, fc, x, y, w, h):
            face_width = w
            face_height = h

            hat_width = face_width + 1
            hat_height = int(0.50 * face_height) + 1

            hat = cv2.resize(hat, (hat_width, hat_height))

            for i in range(hat_height):
                for j in range(hat_width):
                    for k in range(3):
                        if hat[i][j][k] < 235:
                            fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
            return fc


        # def put_glass(glass, fc, x, y, w, h):
        #     face_width = w
        #     face_height = h

        #     hat_width = face_width + 1
        #     hat_height = int(0.50 * face_height) + 1

        #     glass = cv2.resize(glass, (hat_width, hat_height))

        #     for i in range(hat_height):
        #         for j in range(hat_width):
        #             for k in range(3):
        #                 if glass[i][j][k] < 235:
        #                     fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
        #     return fc
        global choise

        # choice = 0
        # print('enter your choice filter to launch that: 1="put hat & glasses" ,any number="put fog filters" ')
        # choise= int(input('enter your choice:'))
        webcam = cv2.VideoCapture(0)
        while True:
            size=4
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fl = face.detectMultiScale(gray,1.19,7)

            for (x, y, w, h) in fl:
                # if choise ==1:
                im = put_hat(hat, im, x, y, w, h)
                # im = put_glass(glass, im, x, y, w, h)

                # else:
                #     im = put_dog_filter(dog, im, x, y, w, h)

            cv2.imshow('Hat & glasses',im)
            key = cv2.waitKey(1) & 0xff
            if key == 27:  # The Esc key
                webcam.release()
                break
    def face_detect4(request, pk):
        import cv2

        id_pk = int(pk)
        image = str(Female_Eyeglasse.objects.get(id=pk))
        
        face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # hat=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/hat.png')
        # hat=cv2.imread(image[1:])
        glass=cv2.imread(image[1:])
        # glass=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/glasses.png')
        # dog=cv2.imread('C:/Users/Cossette/Desktop/Insta_flters_with_python-master/Filters/dog.png')

        # def put_dog_filter(dog, fc, x, y, w, h):
        #     face_width = w
        #     face_height = h

        #     dog = cv2.resize(dog, (int(face_width * 1.5), int(face_height * 1.95)))
        #     for i in range(int(face_height * 1.75)):
        #         for j in range(int(face_width * 1.5)):
        #             for k in range(3):
        #                 if dog[i][j][k] < 235:
        #                     fc[y + i - int(0.375 * h) - 1][x + j - int(0.35 * w)][k] = dog[i][j][k]
        #     return fc

        # def put_hat(hat, fc, x, y, w, h):
        #     face_width = w
        #     face_height = h

        #     hat_width = face_width + 1
        #     hat_height = int(0.50 * face_height) + 1

        #     hat = cv2.resize(hat, (hat_width, hat_height))

        #     for i in range(hat_height):
        #         for j in range(hat_width):
        #             for k in range(3):
        #                 if hat[i][j][k] < 235:
        #                     fc[y + i - int(0.40 * face_height)][x + j][k] = hat[i][j][k]
        #     return fc


        def put_glass(glass, fc, x, y, w, h):
            face_width = w
            face_height = h

            hat_width = face_width + 1
            hat_height = int(0.50 * face_height) + 1

            glass = cv2.resize(glass, (hat_width, hat_height))

            for i in range(hat_height):
                for j in range(hat_width):
                    for k in range(3):
                        if glass[i][j][k] < 235:
                            fc[y + i - int(-0.20 * face_height)][x + j][k] = glass[i][j][k]
            return fc
        global choise

        # choice = 0
        # print('enter your choice filter to launch that: 1="put hat & glasses" ,any number="put fog filters" ')
        # choise= int(input('enter your choice:'))
        webcam = cv2.VideoCapture(0)
        while True:
            size=4
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            fl = face.detectMultiScale(gray,1.19,7)

            for (x, y, w, h) in fl:
                # if choise ==1:
                # im = put_hat(hat, im, x, y, w, h)
                im = put_glass(glass, im, x, y, w, h)

                # else:
                #     im = put_dog_filter(dog, im, x, y, w, h)

            cv2.imshow('Hat & glasses',im)
            key = cv2.waitKey(1) & 0xff
            if key == 27:  # The Esc key
                webcam.release()
                break

@gzip.gzip_page
def face_detect2(request):
    return StreamingHttpResponse(face_detect(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")

def video(request):
    return render(request, 'product/video.html')

class Female_CapListView(ListView):
    model = Female_Cap 
    template_name = 'product/female_caps.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Female_CapDetailView(DetailView):
    model = Female_Cap 
    template_name = 'product/female_caps_detail.html'
    # product_id = Female_Cap.objects.filter(pk=1)
    context_object_name = 'product'

    # def print(request):
    #     for item in product:
    #         print(item)
    #     return render(request, 'product/print.html')
    # ordering = ['-date_added']

class Female_EyeglassesListView(ListView):
    model = Female_Eyeglasse
    template_name = 'product/female_eyeglasses.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Female_EyeglassesDetailView(ListView):
    model = Female_Eyeglasse 
    
class Female_EarringListView(ListView):
    model = Female_Earring
    template_name = 'product/female_earring.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Female_EarringDetailView(ListView):
    model = Female_Earring 

class Female_NecklaceListView(ListView):
    model = Female_Necklace
    template_name = 'product/female_necklace.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Female_NecklaceDetailView(ListView):
    model = Female_Necklace 

class Male_CapsListView(ListView):
    model = Male_Cap
    template_name = 'product/male_caps.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Male_CapsDetailView(ListView):
    model = Male_Cap 

class Male_EarringListView(ListView):
    model = Male_Earring
    template_name = 'product/male_earring.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Male_EarringDetailView(ListView):
    model = Male_Earring 

class Male_NecklaceListView(ListView):
    model = Male_Necklace
    template_name = 'product/male_necklace.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Male_NecklaceDetailView(ListView):
    model = Male_Necklace

class Male_EyeglassesListView(ListView):
    model = Male_Eyeglasse
    template_name = 'product/male_eyeglasses.html'
    context_object_name = 'products'
    ordering = ['-date_added']

class Male_EyeglassesgDetailView(ListView):
    model = Male_Eyeglasse




class PrintFemale_CapDetailView(DetailView):
    model = Female_Cap 
    template_name = 'product/print.html'
    # product_id = Female_Cap.objects.filter(pk=1)
    context_object_name = 'product'
    
    def printss(request):
        print(request)
        product_name = request.POST.get("product_name", "")
        price = request.POST.get("price", "")
        brand = request.POST.get("brand", "")
        description = request.POST.get("description", "")
        quantity = request.POST.get("stock", "")
        id = request.POST.get("id", "")
        
        content = { product_name, price, brand, description }
        # print(id)
        # os.system("sudo chmod a+w /dev/usb/lp0")
        # os.system("sudo echo -e '--- Product Details ---\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Product Name : "+product_name+"\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Brand : "+brand+"\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Price : "+price+"\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Description : "+description+"\n'> /dev/usb/lp0")
        # os.system("sudo echo -e '\n\n\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Please proceed to cashier for payment\n\n'> /dev/usb/lp0")
        # os.system("sudo echo -e 'Thank you for using IVS Kiosk!\n\n\n\n'> /dev/usb/lp0")

        

        def updateFemaleCap(request, id):
            print(id)
            queryset = Female_Cap.objects.get(id=id)
            getCap = int(queryset.stock)
            print(getCap)
            updateCap = getCap - 1
            print(updateCap)
            Female_Cap.objects.select_related().filter(id=id).update(stock=updateCap)

            

        updateFemaleCap(request, id)

        return render(request, 'product/thankyou.html')




        # ;laskdjfl
        # asldfkj
        # asdlfkj