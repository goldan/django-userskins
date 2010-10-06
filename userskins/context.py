from userskins.models import SkinPreference
from django.conf import settings


def userskins(request):
    skin = settings.USERSKINS_DEFAULT
    if request.COOKIES.has_key("userskins") and request.COOKIES["userskins"] in settings.USERSKINS_DETAILS:
        skin = request.COOKIES["userskins"]
    skin_list = settings.USERSKINS_DETAILS.keys()
    if getattr(settings,"USERSKINS_USE_COMPRESS_GROUPS",False):
        return {"userskins_skin": skin, "userskins_use_compress":True, "userskins_skin_list": skin_list }
    else:
        skin_uri = u"%s%s%s" % (settings.STATIC_URL, settings.USERSKINS_SKINS_URL, settings.USERSKINS_DETAILS[skin][0])
        return {"userskins_current_skin_name": skin, "userskins_skin": skin_uri, "userskins_use_compress":False, "userskins_skin_list": skin_list }
