from django.core.management.base import BaseCommand, CommandError
from shorten.models import KirrURL
class Command(BaseCommand):
    help = 'Refresh all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcode(items=options['items'])