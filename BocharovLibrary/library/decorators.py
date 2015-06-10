from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _


def ban_check(func, *args, **kwargs):
    """
    Decorator for checking if authorized user is banned.
    Called with login_required decorator.
    """
    @login_required
    def check(*args, **kwargs):
        request = args[0]
        if request.user.banned:
            messages.error(request, _('Вы забанены на неопределённый срок!'),
                           extra_tags='danger')
            return HttpResponseRedirect(reverse('home'))
        else:
            return func

    return check
