from django.db import models

# Create your models here.


class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)
    # rating
    rating = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.title, self.artist, self.rating)


class Artists(models.Model):
    # First Name
    firstName = models.CharField(max_length=255, null=False)
    # Last Name
    lastName = models.CharField(max_length=255, null=False)

    def __str__(self):
        return"{} - {}".format(self.firstName, self.lastName)
