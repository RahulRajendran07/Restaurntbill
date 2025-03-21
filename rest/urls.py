from django.urls import path
from rest import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("category",views.CategoryViewSet,basename="category")
router.register("products",views.ItemViewSet,basename="product")
urlpatterns = [
    
    path("category/<int:pk>/product/",views.ItemCreateView.as_view()),

]+ router.urls
