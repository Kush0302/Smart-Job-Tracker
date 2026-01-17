from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from jobs.models import JobApplication

class AnalyticsOverviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        total_jobs=JobApplication.objects.filter(user=user).count()

        status_counts = (
            JobApplication.objects
            .filter(user=user)
            .values("status")
            .annotate(count=Count("id"))
        )

        return Response({
            "total_jobs": total_jobs,
            "status_breakdown": status_counts
        })