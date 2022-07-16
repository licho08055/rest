from django.urls import path
from .import views
from .views import ArticleApiView,ArticleDetailView,ApiMixinView

urlpatterns = [
   
    #path('', ArticleApiView.as_view()),
    #path('detail/<int:pk>/',  ArticleApiView.as_view()),
   # path('<int:pk>/', views.article_detail),
    #path('update/<int:id>/',  ApiMixinView.as_view()),
    path('list/', ApiMixinView.as_view()),
     path('<int:id>', ApiMixinView.as_view()),
     path('create/',  ApiMixinView.as_view()),
    path('update/<int:id>/',  ApiMixinView.as_view()),
    path('delete/<int:id>/',  ApiMixinView.as_view()),
]