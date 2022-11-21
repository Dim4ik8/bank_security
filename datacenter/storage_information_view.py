from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for person in not_leaved:
        duration = get_duration(person)
        non_closed_visits.append(
            {
                'who_entered': person.passcard,
                'entered_at': person.entered_at,
                'duration': format_duration(duration),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
