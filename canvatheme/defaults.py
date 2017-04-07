from mezzanine.conf import register_setting
from django.utils.translation import gettext as _

register_setting(
    name = "TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK","IS_SHOW_COPYRIGHT",)
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
        "header."),
    editable=True,
    default="https://facebook.com/khangvo88",
)

register_setting(
    name="IS_SHOW_COPYRIGHT",
    label = _("Is show copyright?"),
    editable=True,
    default="Copyrights &copy; 2014 All Rights Reserved by Canvas Inc.",
)