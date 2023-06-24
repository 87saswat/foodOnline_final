from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def registerUser(request):
    
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # SAVE THE USER USING FORM------------------------------------------------>
            # password = form.cleaned_data["password"] #get the password
            # user = form.save(commit=False)
            # user.set_password(password)                # make the password hashable
            # user.role=User.CUSTOMER                     # assign role as customer to the user
            # user.save()
            # ------------------------------------------------------------------------

            #CREATE THE USER USING create_user METHOD FROM THE MODEL----->
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.role = User.CUSTOMER
            user.save()
            
            return redirect('registerUser')
        else:
            print(form.errors)
    form = UserForm()
    context={
        'form':form,
    }
    return render(request, 'account/registerUser.html',context)