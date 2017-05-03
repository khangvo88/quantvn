from django.db import models

from django.utils.translation import ugettext_lazy as _
# Create your models here.

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

# from colorfield.fields import ColorField


class HomePage(Page, RichText):
    """
    A page representing the format of the home page
    """
    heading = models.CharField(max_length=200, help_text="Call on action text", blank=True)
    subheading = models.CharField(max_length=200, help_text="Call on action button")
    heading_link = models.CharField(max_length=2000, blank=True,
                                    help_text="Optional, if provided will redirect to this link")
    featured_works_heading = models.CharField(max_length=200, help_text="Featured works!")
    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True, help_text="")
    content_heading = models.CharField(max_length=200, help_text="About us!")
    latest_posts_heading = models.CharField(max_length=200, help_text="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable):
    """A slide in a slider connected to a Homepage"""
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
                      upload_to=upload_to("canvatheme.Slide.image",'slider'),
                      format="Image",max_length=255, null=True, blank=True)
    header = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=2000, blank=True)
    is_active = models.BooleanField(verbose_name = _("Active"),default=True)
    #text_color = models.TextField(max_length = 6,default="021430")

class IconBlurb(Orderable):
    """An icon box on a Homepage"""
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
                     upload_to=upload_to("canvatheme.IconBlurb.icon","icons"),
                     format="Image", max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
                            help_text="Optional, if provided cliking the blurb will go here")

class Portfolio(Page):
    '''
    A collection  of individual portfolio items
    '''

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
