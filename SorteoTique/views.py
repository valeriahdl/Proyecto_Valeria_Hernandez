from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from SorteoTique.models import *
from SorteoTique.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    avatar = getavatar(request)
    return render(request,"SorteoTique/inicio.html", {"avatar": avatar})

def draws(request):
    return render(request, "SorteoTique/draws.html")

@login_required
def clients(request):
    Clients = Client.objects.all()
    return render(request, "SorteoTique/clients.html",{"Clients":Clients})

def sellers(request):
    return render(request, "SorteoTique/sellers.html")

def prizes(request):
    return render(request, "SorteoTique/prizes.html")

def tickets(request):
    #return HttpResponse("Vista ticket")
    return render(request, "SorteoTique/tickets.html")

def contactClient(request):
    Clients = Client.objects.all()
    if request.method == 'POST':
        client = Client(client_id=request.POST["client_id"], name=request.POST["name"],last_name=request.POST["last_name"],email=request.POST["email"])
        client.save()   
            #para que el formulario se limpie despues de meterlo:
        myForm = formContactClient()
        return render(request, "SorteoTique/contactClient.html", {"myForm":myForm, "Clients":Clients})
    else:
        myForm = formContactClient()
    return render(request, "SorteoTique/contactClient.html", {"myForm":myForm, "Clients":Clients})

def getSeller(request):
    return render(request, "SorteoTique/getSeller.html")

def buscarVendedor(request):
    if request.GET["seller_region"]:
        seller_region = request.GET["seller_region"]
        sellers = Seller.objects.filter(seller_region = seller_region)
        return render(request, "SorteoTique/getSeller.html", {"sellers":sellers, "key":"value"})
    else:
        answer = "Recuerda escribir la primera letra de la región en mayúscula"
    return HttpResponse(answer)

def drawsSellers(request):
    return render(request, "SorteoTique/drawsSellers.html")

@login_required
def deleteContactClient(request, name_contactClient):
    client = Client.objects.get(name= name_contactClient)
    client.delete()
    myForm = formContactClient()
    Clients = Client.objects.all()
    return render(request, "SorteoTique/contactClient.html", {"myForm":myForm, "Clients":Clients})

@login_required
def editClient(request, name_contactClient):
    client = Client.objects.get(name= name_contactClient)
    if request.method == 'POST':
        myForm = formContactClient(request.POST)
        if myForm.is_valid():
            print(myForm)
            data = myForm.cleaned_data

            client.client_id = data['client_id']
            client.name = data['name']
            client.last_name = data['last_name']
            client.email = data['email']
            client.save()
            myForm = formContactClient()
            Clients = Client.objects.all()
            return render(request, "SorteoTique/contactClient.html", {"myForm":myForm, "Clients":Clients})
    else:
        myForm = formContactClient(initial={'client_id': client.client_id, 'name': client.name, 'last_name': client.last_name, 'email': client.email})
    return render(request, "SorteoTique/editClient.html", {"myForm":myForm})

def loginSellers(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['pwd'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
            #cambiar el redirect a mi perfil ventas cuando se cree
        else:
            return render(request, 'SorteoTique/login.html', {'error': 'Usuario y/o contraseña incorrectos'})
    else:
        return render(request, 'SorteoTique/login.html') 
    
def register(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'SorteoTique/login.html')
    else:
        return render(request, 'SorteoTique/register.html')

@login_required    
def profileView(request):
    return render(request, 'SorteoTique/Profile/profile.html')

@login_required
def editProfile(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, request, 'SorteoTique/Profile/profile.html')
    else:
        form = UserEditForm(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'SorteoTique/Profile/editProfile.html', {"form": form})

@login_required    
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user= usuario) 
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse("Las contraseñas no coinciden")
        return render(request, 'SorteoTique/inicio.html')
    else:
        form = ChangePasswordForm(user= usuario)
        return render(request, 'SorteoTique/Profile/changePassword.html',{"form" : form})

def changeAvatar(request):
    pass
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "SorteoTique/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "SorteoTique/Profile/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar