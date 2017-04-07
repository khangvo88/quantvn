from django.contrib import admin

# Register your models here.
from .models import Slide,IconBlurb, HomePage, Portfolio
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

class SlideAdmin(TabularDynamicInlineAdmin):
    """Slide admin"""
    model = Slide

class IconBlurbAdmin(TabularDynamicInlineAdmin):
    """Icon Blurb admin"""
    model = IconBlurb

class HomePageAdmin(PageAdmin):
    inlines = [SlideAdmin, IconBlurbAdmin]


admin.site.register(HomePage,HomePageAdmin)
admin.site.register(Portfolio,PageAdmin)