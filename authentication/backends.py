import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request=request)
        if not auth_data:
            return None
        
        prefix, token = auth_data.decode('utf-8').split(' ') # o dado vem da internet em formato de bytes e aqui eh convertido para string
        
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY) # mudar para .env posteriormente
            
            user = User.object.get(username=payload['username'])
            return (user, token)
            
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed('Your token is invalid - login.')
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed('Your token is expired - login.')
        
        return super().authenticate(request)