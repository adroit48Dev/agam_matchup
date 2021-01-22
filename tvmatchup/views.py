from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
from . import models

# from .models import Matchup, Templates
from .serializers import MatchupSerializer, TemplateSerializer


# from rest_framework.decorators import api_view

# Create your views here.
# @api_view(['GET', 'POST', 'DELETE'])
class ListCreateTemplate(generics.ListCreateAPIView):
    queryset = models.Templates.objects.all()
    serializer_class = TemplateSerializer

    # def perform_create(self, serializer):
    #     serializer.save()

class RetrieveUpdateDestroyTemplate(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Templates.objects.all()
    serializer_class = TemplateSerializer(queryset, many=True)


class ListCreateMatchup(generics.ListCreateAPIView):
    queryset = models.Matchup.objects.all()
    serializer_class = MatchupSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(template_name_id=self.kwargs.get('template_pk'))
    #
    # def perform_create(self, serializer):
    #     # templates = get_object_or_404(models.Templates, pk=self.kwargs.get('template_pk'))
    #     # serializer.save(templates=templates)
    #     serializer.save()
    #
    # def pre_save(self, obj):
    #     obj.file = self.request.FILES.get('file')


class RetrieveUpdateDestroyMatchup(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Matchup.objects.all()
    serializer_class = MatchupSerializer

    # def get_object(self):
    #     return get_object_or_404(self.get_queryset(),
    #                              template_name_id=self.kwargs.get('template_pk'),
    #                              pk=self.kwargs.get('pk'))



#
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
#
# from .models import Templates, Matchup
# from .serializers import TemplateSerializer, MatchupSerializer
# from rest_framework.decorators import api_view
#
#
# @api_view(['GET', 'POST', 'DELETE'])
# def template_list(request):
#     if request.method == 'GET':
#         templates = Templates.objects.all()
#
#         template_name = request.GET.get('temp_name', None)
#         if template_name is not None:
#             templates = templates.filter(temmplate_name__icontains=template_name)
#
#         template_serializer = TemplateSerializer(templates, many=True)
#         return JsonResponse(template_serializer.data, safe=False)
#
#
#     elif request.method == 'POST':
#         template_data = JSONParser().parse(request)
#         template_serializer = TemplateSerializer(data=template_data)
#         if template_serializer.is_valid():
#             template_serializer.save()
#             return JsonResponse(template_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(template_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         count = Templates.objects.all().delete()
#         return JsonResponse({'message': '{} Templates were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)