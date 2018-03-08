from rest_framework.permissions import BasePermission


class HasCompanyInSession(BasePermission):

    def has_permission(self, request, view):
        return bool(request.session.get('company_id'))
