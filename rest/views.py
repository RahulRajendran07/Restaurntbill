from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest.serializers import CategorySerializer,ItemSerializer

from rest_framework.generics import CreateAPIView,ListAPIView

from rest.models import Category,Item

from rest_framework.viewsets import ViewSet,ModelViewSet

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
    

class ItemCreateView(CreateAPIView):

    serializer_class = ItemSerializer

    def perform_create(self, serializer):

        id = self.kwargs.get("pk")

        category_instance = get_object_or_404(Category,id=id)

        serializer.save(category_object = category_instance)



class ItemViewSet(ModelViewSet):

   

    serializer_class = ItemSerializer

    queryset = Item.objects.all()

    http_method_names = ["get","put","delete"]

    def get_queryset(self):
        
         qs = Item.objects.all()

         if "category" in self.request.query_params:
             
             category_name = self.request.query_params.get("category")

             qs = qs.filter(category_object__name = category_name)

         return qs