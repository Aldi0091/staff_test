from rest_framework import serializers
from .models import Staff


class StaffSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    position = serializers.CharField(max_length=150)
    emp_date = serializers.DateField()
    salary = serializers.IntegerField()
    # parent = serializers.IntegerField()
    parent = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.emp_date = validated_data.get('emp_date', instance.emp_date)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.parent = validated_data.get('staff_id', instance.parent)
        instance.save()
        return instance