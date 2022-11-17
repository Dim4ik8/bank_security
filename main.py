import os
from datetime import datetime
import django
import pytz

from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard, Visit

if __name__ == '__main__':
    print('Количество пропусков:', Passcard.objects.count())
    cards = Passcard.objects.all()

    print(cards)

    for card in cards:
        print(
            f' owner_name: {card.owner_name} \n passcode: {card.passcode} \n created_at: {card.created_at} \n is_active: {card.is_active}\n')

    active_passcards = [card.owner_name for card in cards if card.is_active]
    print(f'Активных пропусков: {len(active_passcards)}')

    active_passcards_from_db = Passcard.objects.filter(is_active=True)
    print(f'Активных пропусков: {len(active_passcards_from_db)}')

    not_leaved = Visit.objects.filter(leaved_at=None)
    print(not_leaved)

    for person in not_leaved:
        entered_time = django.utils.timezone.localtime(person.entered_at)
        now_time = datetime.now(pytz.timezone('Europe/Moscow')).replace(microsecond=0)

    time_spent = now_time - entered_time
    print(person.passcard)
    print(f'Зашел в хранилище, время по Москве:  \n {entered_time}')
    print(f'Находится в хранилище:  \n {time_spent}')

    execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
