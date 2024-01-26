from django.db import models

class WasteBin(models.Model):
    longitude = models.CharField(max_length = 32)
    latitude = models.CharField(max_length = 32)
    area = models.CharField(max_length = 128)
    def __str__(self):
        return f'Bin at {self.area}'

class WasteBinData(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    wet_organic = models.FloatField()
    dry_organic = models.FloatField()
    non_recyclable = models.FloatField()
    recyclable = models.FloatField()
    last_sanitized = models.DateTimeField()

    def __str__(self):
        return f'Data for Bin {self.bin} at {self.timestamp}'

class DailyBinSummary(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    date = models.DateField()
    wet_organic = models.FloatField()
    dry_organic = models.FloatField()
    non_recyclable = models.FloatField()
    recyclable = models.FloatField()
    last_sanitized = models.DateTimeField()

    def __str__(self):
        return f'Daily Summary for Bin {self.bin} on {self.date}'

