from django.core.management.base import BaseCommand, CommandParser
from wordle.models import WordleModel
import requests

from backend.settings import WORDS_DICTIONARY_URL

class Command(BaseCommand):

    help = "Flushes and Repopulate Wordle List From URL"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('-f', '--flush', type=bool, default=False)

    def handle(self, *args, **options):
        if options.get('flush', False): WordleModel.objects.all().delete()

        # This needs an active internet connection to work, 
        # in case there is no internet, this code will default to
        # hardcoded words
        try:
            res = requests.get(WORDS_DICTIONARY_URL)
            words = [ x for x in res.text.splitlines() ]
        except:
            words = ["WEARY", "PILLS", "VAGUE"]

        words = [WordleModel(wordle=x) for x in words]
        
        WordleModel.objects.bulk_create(words, ignore_conflicts=True)
        
        self.stdout.write(self.style.SUCCESS('Successfully Loaded Wordle Data From URL'))