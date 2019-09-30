from django.shortcuts import render
from . import models


def all_rooms(requet):
    all_rooms = models.Room.objects.all()
    return render(requet, "rooms/home.html", context={"rooms": all_rooms})
