from datacenter.models import Visit
from datacenter.models import get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_serialized = []
    non_closed_visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in non_closed_visits:
        duration = get_duration(person)
        non_closed_visits_serialized.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits_serialized,
    }
    return render(request, 'storage_information.html', context)
