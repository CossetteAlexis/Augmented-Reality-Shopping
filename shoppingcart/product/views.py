from django.shortcuts import render
from .models import Product
from .models import Female_Cap
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import UserForm
import cv2
import numpy as np
import dlib
from math import hypot   
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

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
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_eyeglasses.html', {'page_obj': page_obj})

def male_necklace(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_necklace.html', {'page_obj': page_obj})

def male_caps(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_caps.html', {'page_obj': page_obj})

def male_earrings(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/male_earrings.html', {'page_obj': page_obj})

def female_products(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_products.html', {'page_obj': page_obj})

def female_eyeglasses(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_eyeglasses.html', {'page_obj': page_obj})

def female_necklace(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_necklace.html', {'page_obj': page_obj})

def female_caps(request):
    product = Female_Cap.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_caps.html', {'page_obj': page_obj})

def female_earring(request):
    product = Product.objects.all()
    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/female_earring.html', {'page_obj': page_obj})



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
    def face_detect(request):
        import cv2
        import numpy as np
        import dlib
        from math import hypot

        # Loading Camera and Nose image and Creating mask
        cap = cv2.VideoCapture(0)
        nose_image = cv2.imread("C:/Users/Cossette/Desktop/New folder/pig_nose.png")
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
                top_nose = (landmarks.part(29).x, landmarks.part(29).y)
                center_nose = (landmarks.part(30).x, landmarks.part(30).y)
                left_nose = (landmarks.part(31).x, landmarks.part(31).y)
                right_nose = (landmarks.part(35).x, landmarks.part(35).y)

                nose_width = int(hypot(left_nose[0] - right_nose[0],
                                left_nose[1] - right_nose[1]) * 1.7)
                nose_height = int(nose_width * 0.77)

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
                break
        return HttpResponse('Ok')

@gzip.gzip_page
def face_detect2(request):
    return StreamingHttpResponse(face_detect(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")

def video(request):
    return render(request, 'product/video.html')