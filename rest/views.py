from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest.serializers import CategorySerializer

from rest_framework.generics import CreateAPIView,ListAPIView

from rest.models import Category

from rest_framework.viewsets import ViewSet

from rest_framework.response import Response

# class CategoryListCreateView(CreateAPIView,ListAPIView):

#     serializer_class = CategorySerializer

#     queryset = Category.objects.all()


class CategoryViewSet(ViewSet):

    serializer_class = CategorySerializer

    def list(self,request,*args,**kwargs):

       qs = Category.objects.all()
       
       serializer_instance = self.serializer_class(qs,many=True)
       
       return Response(data=serializer_instance.data)
    
    def create(self,request,*args,**kwrsgs):

        serializer_instance =self.serializer_class(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
             return Response(data=serializer_instance.errors)
        
    def retrieve(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        qs = get_object_or_404(Category,id=id)

        serializer_instance = self.serializer_class(qs,many=False)

        return Response(data=serializer_instance.data)
    
    def update(self,request,*args,**kwargs):

        id = kwargs.get("pk")

        category_object = get_object_or_404(Category,id=id)

        serializer_instance=self.serializer_class(data= request.data , instance = category_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        
    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        category_object=get_object_or_404(Category,id=id)

        category_object.delete()

        return Response(data={"message":"deleted"})