import os

import django
from django.core.management import execute_from_command_line
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    cards = Passcard.objects.all()
    print(cards)

    for card in cards:
        print(f'owner_name: {card.owner_name} \npasscode: {card.passcode} \ncreated_at: {card.created_at} \nis_active: {card.is_active}\n')

    active_passcards = [card.owner_name for card in cards if card.is_active]
    print(f'Активных пропусков: {len(active_passcards)}')

    active_passcards_from_db = Passcard.objects.filter(is_active=True)
    print(f'Активных пропусков: {len(active_passcards_from_db)}')

    execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())