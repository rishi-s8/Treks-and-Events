from django.shortcuts import render, get_object_or_404
from .models import Trek, Event

def index(request):
    all_treks = Trek.objects.all()
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
        'all_treks': all_treks,
    }
    return render(request, 'college/index.html', context)

def detailsT(request, trek_id):
    trek = get_object_or_404(Trek, id=trek_id)
    return render(request, 'college/detailsT.html', {'trek': trek})

def detailsE(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'college/detailsE.html', {'event': event})
