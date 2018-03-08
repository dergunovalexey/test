from django.contrib.auth import get_user_model, logout, login
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from core.serializers import ToDoSerializer, AuthSerializer


class Auth(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet,):
    queryset = get_user_model().objects.all()
    serializer_class = AuthSerializer

    def get_object(self):
        queryset = self.get_queryset()
        data = self.request.data
        email = data.get('email')

        user = queryset.filter(email=email).first()
        if not user:
            raise ValidationError({'detail': ['incorrect email or password']})

        password = data.get('password')

        if not user.check_password(password):
            raise ValidationError({'detail': ['incorrect email or password']})
        return user

    def create(self, request, *args, **kwargs):
        user = self.get_object()
        company_id = request.data.get('company_id')
        if not user.companies.filter(id=company_id).exists():
            raise ValidationError({'company_id': ['incorrect data']})
        login(request=request, user=user)
        request.session['company_id'] = company_id
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
