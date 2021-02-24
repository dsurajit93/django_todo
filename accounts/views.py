from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import Account
from django .core.files.storage import FileSystemStorage

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        upload_photo = False

        if request.FILES:
            photo = request.FILES['photo']
            upload_photo = True
            photo_path = 'photos/'+email+'.jpeg'
        else:
            photo_path = 'static/images/user.png'

        if password != password2:
            messages.error(request, 'Passwords must be same')
            return redirect('signup')

        if Account.objects.filter(email=email).exists():
            messages.error(
                request, "Email is alredy taken. Try with differnt email")
            return redirect('signup')

        if Account.objects.filter(phone=phone).exists():
            messages.error(
                request, "Phone is alredy taken. Try with differnt Phone number")
            return redirect('signup')

        user = Account.objects.create_user(name=name, phone=phone, email=email,
                       password=password, photo=photo_path)
        user.save()
        
        if upload_photo:
            fs = FileSystemStorage()
            if fs.exists(photo_path):
                fs.delete(photo_path)
            fs.save(photo_path, photo)

        messages.success(request, 'Account Created')
        return redirect('signin')

    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Successfully Logged In')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Email Id or Password')
            return redirect('signin')
        
    return render(request, 'accounts/signin.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def change_photo(request):
    if request.FILES and request.method == "POST":
        photo = request.FILES['photo']
        user = request.user
        email = user.email
        photo_path = 'photos/'+email+'.jpeg'

        user.photo = photo_path
        user.save()

        fs = FileSystemStorage()
        if fs.exists(photo_path):
            fs.delete(photo_path)
        fs.save(photo_path, photo)
        return redirect('profile')

def logout(request):
    auth.logout(request)
    return redirect('index')
