from rest_framework import serializers
from .models import JobApplication
from django.utils.timezone import now

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = [
            'id',
            'company_name',
            'job_role',
            'status',
            'applied_date',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data['user'] = request.user
        return super().create(validated_data)
    
    def validate_company_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Company name cannot be empty.")
        return value
    
    def validate_job_role(self, value):
        if not value.strip():
            raise serializers.ValidationError("Position cannot be empty.")
        return value

    def validate_applied_date(self, value):
        if value > now().date():
            raise serializers.ValidationError("Applied date cannot be in the future.")
        return value

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in JobApplication.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid job status.")
        return value
    
    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None

        company = data.get('company_name')
        role = data.get('job_role')

        if user and JobApplication.objects.filter(
            user=user,
            company_name=company,
            job_role=role
        ).exists():
            raise serializers.ValidationError(
                "You have already added this job application."
            )

        return data

