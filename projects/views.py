from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, UserStory, Ticket
from companies.models import Company, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def projects(request):
    # print(request.user)

    if request.method == "GET":
        userProfile = UserProfile.objects.get(user=request.user)
        projects = Project.objects.filter(company=userProfile.company)
        return render(request, "projects.html", {"projects":projects})
    else:
        try:
            project = get_object_or_404(Project, nombre=request.POST["project"])
            userStories = UserStory.objects.filter(project=project)
            return redirect("projectid",id=project.nombre)
        except ValueError:
            return render(request,"projects.html",{"error": "Error listando projectos"})

@login_required
def userStories(request, id):
    if request.method == "GET":
        project = get_object_or_404(Project, nombre=id)
        userStories = UserStory.objects.filter(project=project)
        return render(request, "userStories.html",{"userStories":userStories})
    else:
        try:
            project = get_object_or_404(Project,nombre=id)
            nombre = request.POST["nombre"]
            userStory = UserStory(project=project,nombre=nombre)
            userStory.save()
            return redirect("tickets",userStory=userStory.id)
        except ValueError:
            return render(request,"userStories.html",{"error": "Error creando historia de usuario"})
            
@login_required
def tickets(request,userStory):
    userStory = get_object_or_404(UserStory, id=userStory)
    print(userStory)
    if request.method == "GET":
        # userStory = UserStory.objects.get(nombre=userStory)
        return render(request,"tickets.html",{"userStory":userStory})
    else:
        try:
            project = get_object_or_404(Project,nombre=userStory.project.nombre)
            nombre = request.POST["nombre"]
            descripcion = request.POST["descripcion"]
            estado = request.POST["estado"]
            ticket = Ticket(userStory=userStory,nombre=nombre,descripcion=descripcion,estado=estado)
            ticket.save()
            return redirect('listTickets', listTickets=userStory.nombre)
        except ValueError:
            return render(request,"tickets.html",{"error": "Error creando ticket"})
    
@login_required
def update_tickets (request,id):
    ticket = get_object_or_404(Ticket, id=id)
    if request.method == "GET":
        return render(request,'update_tickets.html',{"ticket":ticket})
    else:
        try:
            ticket.nombre = request.POST["nombre"]
            ticket.descripcion = request.POST["descripcion"]
            ticket.estado = request.POST["estado"]
            ticket.save()
            return redirect('listTickets', listTickets=ticket.userStory.nombre)
        except ValueError:
            return render(request,"update_tickets.html",{"error": "Error actualizando ticket"})

@login_required
def delete_tickets (request,id):
    try:
        ticket = get_object_or_404(Ticket, id=id)
        ticket.delete()
        return redirect('listTickets', listTickets=ticket.userStory.nombre)
    except ValueError:
        return redirect('listTickets', error=error)

@login_required
def list_tickets(request, listTickets):
    try:
        userStory=get_object_or_404(UserStory,nombre=listTickets)
        tickets = Ticket.objects.filter(userStory=userStory)
        return render(request, "list_tickets.html", {"projectName":listTickets, "tickets":tickets, "userStory":userStory})
    except ValueError:
        return render(request,"list_tickets.html",{"error": "Error listando tickets"})


@login_required
def history_tickets(request):
    try:
        userProfile = UserProfile.objects.get(user=request.user)
        # projects = Project.objects.filter(company=userProfile.company)
        tickets = Ticket.objects.filter(userStory__project__company=userProfile.company) 
        return render(request, "history_tickets.html" ,{"tickets":tickets})
    except ValueError:
        return render(request,"history_tickets.html",{"error": "Error listando ticket"})
