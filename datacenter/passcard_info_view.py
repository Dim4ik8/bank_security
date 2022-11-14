from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    # passcard = Passcard.objects.all()[0]
    passcard = Passcard.objects.get(passcode=passcode)
    # Программируем здесь
    this_passcard_visits = []
    visites = Visit.objects.filter(passcard=passcard.id)
    for visit in visites:
        duration = get_duration(visit)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
                'is_strange': is_visit_long(visit)
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
