from django.db import models


# Create your models here.

class Image(models.Model):
    """Model definition for Image."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Image."""

        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        """Unicode representation of Image."""
        pass

    def save(self):
        """Save method for Image."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Image."""
        return ('')

    # TODO: Define custom methods here
)