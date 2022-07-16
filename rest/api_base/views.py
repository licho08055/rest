import sre_compile
from turtle import st
from django.http import HttpResponse,JsonResponse
from requests import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics




 
 




from .models import Article 
from .serializers import ArticleSerializer
from api_base import serializers




class ApiMixinView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   
    generics.GenericAPIView):
    
    queryset =  Article.objects.all()
    serializer_class =  ArticleSerializer
    lookup_field = 'id'
    
    
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        if id is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        if id is not None:
            return self.update( request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
            pk = self.kwargs.get('pk')
            if pk is not None:
               return self.destroy( request, *args, **kwargs)
        

 
 
 
class ArticleApiView(APIView):
    
    def get(self,request):
        serializer=ArticleSerializer(Article.objects.all(),many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ArticleDetailView(APIView):
    
    def get(self, request,pk):
        try:
            article=get_object_or_404(Article,pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
        
    
    
    def put(self,request,pk):
            article=get_object_or_404(Article,pk=pk)
            serializer=ArticleSerializer(article,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        article=get_object_or_404(Article,pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 
 
 
 
 
 
 

@api_view(['GET','POST'])
def article_list(request, *args, **kwargs):
    if request.method=='GET':
        serializer=ArticleSerializer(Article.objects.all(),many=True)
        return  Response(serializer.data )
    
    elif request.method=='POST':
         serializer=ArticleSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse( status=404)
    if request.method=='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return  Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
     
