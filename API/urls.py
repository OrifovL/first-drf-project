# # from .views import ListView,CreateView,UpdateView,RetrieveView,DeleteView
# from .views import GetProduct
# from django.urls import path

# urlpatterns = [
#     # path('list/',ListView.as_view()),
#     # path('list/<int:pk>',RetrieveView.as_view()),
#     # path('list/create',CreateView.as_view()),
#     # path('list/update/<int:pk>',UpdateView.as_view()),
#     # path('list/delete/<int:pk>',DeleteView.as_view()),
#     path('list',GetProduct.as_view()),
#     path('list/<int:pk>',GetProduct.as_view()),
    
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
