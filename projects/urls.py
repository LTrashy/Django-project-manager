from django.contrib import admin
from django.urls import path, include
from .views import projects, userStories, tickets, list_tickets, update_tickets, history_tickets, delete_tickets

urlpatterns = [
    path("", projects, name="projects"),
    path("<id>/", userStories, name="projectid"),
    path("userStory/<userStory>", tickets, name="tickets"),
    path("tickets/<listTickets>", list_tickets, name="listTickets"),
    path("tickets/update/<id>", update_tickets, name="updateTickets"),
    path("tickets/delete/<id>", delete_tickets, name="deleteTickets"),
    path("history", history_tickets, name="historyTickets")
]