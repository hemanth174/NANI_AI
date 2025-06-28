from django.shortcuts import render

def home(request):
    return render(request, 'assistant/index.html')

def talk_to_nani(request):
    # Logic for talking to NANI will go here
    return render(request, 'talk.html')

def explore(request):
    # Logic for exploring features will go here
    return render(request, 'explore.html')

def emergency(request):
    # Logic for emergency features will go here
    return render(request, 'emergency.html')

def profile(request):
    # Logic for user profile will go here
    return render(request, 'profile.html')


from django.http import JsonResponse
from .assistant import run_giri_once

def start_assistant(request):
    if request.method == "POST":
        conversation = run_giri_once()
        return JsonResponse({"conversation": conversation})
    return JsonResponse({"error": "POST request required."}, status=400)

from django.shortcuts import render

def talk_assistant(request):
    return render(request, 'assistant/talk_assistant.html')


