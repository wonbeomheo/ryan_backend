from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)

from django.db.models import Subquery
from django.contrib.postgres.aggregates import ArrayAgg
from skill.models import Skill

from .models import Experience
from .serializers import ExperienceSerializer, ExperienceCreateSerializer, ExperienceUpdateSerializer

import logging

logger = logging.getLogger("dev.debug")

class ExperienceCreateView(CreateAPIView):
    serializer_class = ExperienceCreateSerializer
    permission_classes = [IsAuthenticated]
    

class ExperienceRetrieveView(RetrieveAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Experience.objects.all()


class ExperienceListView(ListAPIView):
    """
        List all experiences
    """
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return Experience.objects.all()
    
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        logger.info("[GET] List All Experiences.")
        return response
    

class ExperienceUpdateView(UpdateAPIView):
    # serializer_class = ExperienceSerializer
    serializer_class = ExperienceUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Experience.objects.all()

class ExperienceDeleteView(DestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Experience.objects.all()