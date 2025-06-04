


from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from myapp.models import *
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def register(request):
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']  
        print(username,email,password,confirm_password)  
        uid = data.objects.filter(email=email).exists()
        if uid:
            contaxt={
                "message":"Email is already exists." 
            }
        
            return render(request,"register.html",contaxt)
        else:
            if password == confirm_password:
                data.objects.create(username=username,email=email,password=password,confirm_password=confirm_password)
                return redirect(index)
            else:
                contaxt={
                "message":"Enter a valid password" 
            }
        
            return render(request,"register.html",contaxt)
    else:
        print("invalid data ")
        return render(request,"register.html")

# ----------------------------------------------------------------------------------------

def login(request):
    if "email" in  request.session:
        return redirect(index)
    else:
        if request.POST:
            email=request.POST["email"]
            password=request.POST["password"]       
            uid=data.objects.filter(email=email).exists()

            if uid:
                uid=data.objects.get(email=email)
                if password==str(uid.password):
                    request.session['email']=email
                    return redirect(index)
                else:
                    contaxt={
                        "msg":"invalide password",
                    }
                    return render(request,"login.html",contaxt)
            else:
                print(email,password)
                return render(request,"login.html")    
        else:  
            return render(request,"login.html")

# ----------------------------------------------------------------------------------------------

def logout(request):
    del request.session['email']
    return redirect(login)

# ==================================================================
import random
 
def forgot_password(request):
        if request.POST:
                email=request.POST["email"]  
                uid=data.objects.filter(email=email).exists()
                otp=random.randint(100000,999999)
                print(otp)
                if uid:
                     uid=data.objects.get(email=email)
                     uid.otp=otp
                     uid.save()
                     send_mail("way to interior",f"Your OTP is - {otp}","gohiljayb10@gmail.com", [email])
                     contaxt={
                         "uid":uid
                     }
                     return render(request,"con_password.html",contaxt)
                else:
                    contaxt={
                    "uid":uid,
                    "message":"invalid email"
                    }

                    return render(request,"forgot_password.html",contaxt)
        return render(request,"forgot_password.html")

# =============================================================================================

def confirm_password(request):
    if request.POST:
        email=request.POST["email"]  
        otp=request.POST["otp"]  
        password=request.POST["password"]  
        confirm_password=request.POST["confirm_password"]  
        uid=data.objects.get(email=email)
        if uid.otp == int(otp):
            if password == confirm_password:
                uid.password=password
                uid.confirm_password=confirm_password
                uid.save()
                return redirect(login)
            else:
                contaxt={
                    "msg":"Invalid Password",
                    "uid":uid
                }
                return render(request,"con_password.html",contaxt)
        else:
            contaxt={
                "msg":"Invalid Otp",
                "uid":uid
            }
            return render(request,"con_password.html",contaxt)


    return render(request,"con_password.html")


def add_requirements(request):
    return render(request, 'add_requirements.html')






def designs(request):
    designs = Design.objects.filter(is_approved=True).order_by("-id")  # Only show approved
    return render(request, 'designs.html', {'designs': designs})

def add_design(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        designer_name = request.POST.get('designer_name')
        image = request.FILES.get('image')

        design=Design.objects.create(
            title=title,
            designer_name=designer_name,
            image=image,
            is_approved=False  # Always False when a user submits
        )
        design.save()
        return redirect('designs')  # Redirect to designs page after submission

    return render(request, 'add_designs.html')



def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')

def success(request):
    return render(request, 'success.html')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        contact=ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

        messages.success(request, 'Thank you for contacting us! We have received your message.')
        return redirect('contact')  # Reload to clear POST

    return render(request, 'contact.html')



def add_designer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        specialization = request.POST.get('specialization')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')

        designer=Designer.objects.create(
            name=name,
            specialization=specialization,
            bio=bio,
            image=image,
            is_approved=False   # Always False when user submits

        )
        designer.save()
        return redirect('designers')

    return render(request, 'add_designer.html')


def designers(request):
    designers = Designer.objects.filter(is_approved=True).order_by("-id") 
    return render(request, 'designers.html', {'designers': designers})



def add_requirements(request):
    if request.method == 'POST':
        space_type = request.POST.get('space_type')
        style = request.POST.get('style')
        budget = request.POST.get('budget')
        services = request.POST.getlist('services')  # Multiple checkboxes
        timeline = request.POST.get('timeline')
        description = request.POST.get('description')

        requirements = Requirement.objects.create(
            space_type=space_type,
            style=style,
            budget=budget,
            timeline=timeline,
            description=description
        )
        requirements.save()

        return redirect('index')  # redirect after successful submission

    return render(request, 'add_requirements.html')



def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review=Review.objects.create(
            name=name,
            email=email,
            rating=rating,
            comment=comment
        )
        review.save()

        messages.success(request, 'Thank you for your review!')
        return redirect('review')

    reviews = Review.objects.all().order_by("-id")  # Show existing reviews
    return render(request, 'review.html', {'reviews': reviews})
