from rest_framework import serializers
from core.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = ToDo

    def create(self, validated_data):
        company_id = self.context['company_id']
        validated_data['company_id'] = company_id
        return super().create(validated_data)
