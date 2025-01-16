from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Update last activity
            User.objects.filter(id=request.user.id).update(last_login=now())
        response = self.get_response(request)
        return response
