from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from core.permissions import HasCompanyInSession
from core.serializers import ToDoSerializer, AuthSerializer
from core.models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsAuthenticated, HasCompanyInSession)

    def get_queryset(self):
        queryset = super().get_queryset()
        session = self.request.session
        company_id = session.get('company_id')
        return queryset.filter(company_id=company_id).order_by('-date_quest')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['company_id'] = self.request.session.get('company_id')
        return context