from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     # Класс APIView стоит во главе иерархии всех классов представления DRF.
#     # Представляет самый базовый функционал для работы различных классов представлений.
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         # post_new = Women.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     cat_id=request.data['cat_id']
#         # )
#
#         # return Response({'post': WomenSerializer(post_new).data})
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exist"})
#
#         return Response({"post": "delete post" + str(pk)})
