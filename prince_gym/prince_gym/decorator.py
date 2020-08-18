from django.shortcuts import HttpResponseRedirect
from functools import wraps


def  login_register_check(url='/'):
    def decorator(view_func):
        @wraps(view_func)
        def _is_logged_in(request, *args, **kwargs):
            if request.user.is_authenticated:
                return HttpResponseRedirect(url)
            else:
                return view_func(request, *args, **kwargs )
        return _is_logged_in
    return decorator
