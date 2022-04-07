
import django
from ninja import Router
from django.conf import settings
from ninja.security import django_auth
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.middleware.csrf import get_token
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
    PasswordChangeForm
)

from django.contrib.auth import (
    login as django_login,
    logout as django_logout,
    authenticate
)

from utils.schema import ErrorOut

from .schema import (
    CRSFOut,
    UserOut,
    LoginIn,
    RequestPasswordResetIn,
    SetPasswordIn,
    ChangePasswordIn,
    ValidSessionOut,
)


router = Router()
_LOGIN_BACKEND = 'django.contrib.auth.backends.ModelBackend'
_TAGS= ['Auth']


@router.get('/csrf/', response={200: CRSFOut})
def csrf(request):
    response = {"message": "Success - Set CSRF cookie"}
    response["csrf_token"] = get_token(request)
    return 200, response

@router.get('/session/', tags=_TAGS, response={200: ValidSessionOut}, auth=django_auth)
def session(request):
    return 200, {"email": request.user.email, "status": 200}


@router.post('/', tags=_TAGS, response={200: UserOut, 403: ErrorOut}, auth=None)
def login(request, data: LoginIn):
    user = authenticate(backend=_LOGIN_BACKEND, **data.dict())
    if user is not None and user.is_active:
        django_login(request, user, backend=_LOGIN_BACKEND)
        return user
    return 403, {"title":"Login failed","detail":"Invalid user or password", "status":403}


@router.delete('/', tags=_TAGS, response={204: None}, auth=django_auth)
def logout(request):
    django_logout(request)
    return 204, None


@router.get('/me/', tags=_TAGS, response=UserOut, auth=django_auth)
def me(request):
    return request.user


