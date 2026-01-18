from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from jobs.models import JobApplication
from django.db.models.functions import TruncDay, TruncMonth

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

        daily_applications = (
            JobApplication.objects
            .filter(user=user)
            .annotate(day=TruncDay("applied_date"))
            .values("day")
            .annotate(count=Count("id"))
            .order_by("day")
        )

        monthly_applications = (
            JobApplication.objects
            .filter(user=user)
            .annotate(month=TruncMonth('applied_date'))
            .values('month')
            .annotate(count=Count('id'))
            .order_by('month')
        )


        return Response({
            "total_jobs": total_jobs,
            "status_breakdown": status_counts,
            "daily_applications": daily_applications,
            "monthly_applications": monthly_applications,
        })