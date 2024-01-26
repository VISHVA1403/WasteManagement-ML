from django.core.management.base import BaseCommand
from django.db.models import Max
from datetime import date, timedelta
from ...models import WasteBinData, DailyBinSummary,WasteBin
   
class Command(BaseCommand):
    help = 'Generate daily summaries for bin levels'

    def handle(self, *args, **options):
        bins = WasteBin.objects.all()

        for bin in bins:
            last_data = WasteBinData.objects.filter(bin=bin).latest('timestamp')

            # Calculate the date for yesterday
            yesterday = date.today()

            # Create or update the daily summary
            summary, created = DailyBinSummary.objects.update_or_create(
                bin=bin,
                date=yesterday,
                defaults={
                    'wet_organic': last_data.wet_organic,
                    'dry_organic': last_data.dry_organic,
                    'non_recyclable': last_data.non_recyclable,
                    'recyclable': last_data.recyclable,
                    'last_sanitized': last_data.last_sanitized,
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created summary for Bin {bin} on {yesterday}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated summary for Bin {bin} on {yesterday}'))