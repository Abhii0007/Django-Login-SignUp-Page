from django.http import JsonResponse
from django.shortcuts import render
import os
def login(request):
    return render(request, 'login.html')


def submit(request):
    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password  # To hash passwords

def signup(request):
    message = None
    success = False
    if request.method == 'POST':
        # Collect form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save data to the database
        try:
            user = User(
                name=name,
                phone=phone,
                email=email,
                password=make_password(password)  # Hash the password
            )
            user.save()
            message = "Signup successful!"
            success = True
        except Exception as e:
            message = f"Error: {e}"

    return render(request, 'signup.html', {'message': message, 'success': success})




'''def signup(request):
    if request.method == 'POST':
        # Get data from HTML page elements using 'name' variable (unique identifier)
        #'input1' is the name of the input field in the html form that returned the entered text
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Context should be dictionary or JSON data:
        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'password': password
        }
        os.system('cls')
        print(data)

        if name and phone and email and password:
            context = {'success': True, 'message': 'Signup successful!'}
        else:
            context = {'success': False, 'message': False}

        return render(request, 'signup.html', context)
 
    return render(request, 'signup.html')
'''




def main(request):
    if request.method == 'POST':
        # Get data from HTML page elements using 'name' variable (unique identifier)
        #'input1' is the name of the input field in the html form that returned the entered text
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username=='abhi' and password=='1234':
            return render(request, 'main.html')
        
            
    return render(request, 'login.html')
    
    
    