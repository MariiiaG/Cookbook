from django.urls import path
from .views import Index, UserLogoutView, UserLoginView, RegisterNewView, RecipeListView, recipe_detail, edit_recipe
from .views import publish_new, index, list_all, Published, recipe
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterNewView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('recipe/<int:recipe_id>/', recipe, name='recipe'),
    path('detailed/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('publish_new/', publish_new, name='publish'),
    path('edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('recipe_list/', list_all, name='recipe_list'),
    path('published/', Published.as_view(), name='published'),
]
urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
