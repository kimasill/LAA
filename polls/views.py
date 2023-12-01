from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from .models import Character
import lostAPI

def index(request):
    characters = lostAPI.getCharacterInfo("엉루지") #test string
    context = {'characters' : characters}
    return render(request, 'index.html', context)

def detail(request, character_name):
    try:
        character = lostAPI.getArmories(character_name,'profiles')
    except:
        raise Http404("캐릭터가 존재하지 않습니다")

    equipment = lostAPI.getArmories(character_name, 'equipment')

    context = {
        'character': character,
        'equipment': equipment,
        'stats' : character['Stats']
    }
    return  render(request, 'detail.html', context)

def results(request, character_id):
    response = "looking here character's details %s."
    return HttpResponse(response % character_id)

