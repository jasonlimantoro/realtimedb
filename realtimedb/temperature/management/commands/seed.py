from django.core.management.base import BaseCommand
from realtimedb.temperature.management.commands._seeder import executor


class Command(BaseCommand):
    help = 'Seed Temperature table'

    def add_arguments(self, parser):
        parser.add_argument('number', nargs='?', default=5, type=int)

    def handle(self, *args, **options):
        executor(options['number'])
        self.stdout.write(
            self.style.SUCCESS(f"Successfully seeded {options['number']} temperatures!")
        )
