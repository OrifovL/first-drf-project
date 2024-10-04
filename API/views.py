# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
# from .models import Products
# from .serializer import ProductSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# # Create your views here.

# class ListView(ListAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class RetrieveView(RetrieveAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class CreateView(CreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class UpdateView(UpdateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class DeleteView(DestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer


# class GetProduct(APIView):
#     def get(self,request):
#         data = Products.objects.all()
#         serialaze = ProductSerializer(data, many = True).data
#         return Response({"total":len(data),'product':serialaze})
    
#     def post(self, request):
#         serialaze = ProductSerializer(data = request.data)
#         if serialaze.is_valid():
#             serialaze.save()
#             return Response({"Message":'Post qilindi'})
#         else:
#             return Response({"Error":"Error (post)"})
        
#     def delete(self, request, pk):
#         data = Products.objects.get(pk=pk)
#         data.delete()
#         return Response({"Message":"Malumot uchirildi"})
    
#     def put(self, request, pk):
#         data = Products.objects.get(pk=pk)
#         serialize = ProductSerializer(data = request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response({"Message":"Malumot yangilandi"})
#         else:
#             return Response({"Error":"Error (update)"})


from rest_framework import viewsets
from .models import Products
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer