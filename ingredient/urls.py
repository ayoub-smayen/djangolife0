from django.urls import path
from .views import ingredientView, searchView, get_ingredientId, get_match_recipe

urlpatterns = [
    #path('admin/', admin.site.urls),

    # view
    path('', ingredientView),
    path('search/<int:ingredientId>/', searchView),

    # api
    path('api/ingredient_id/<ingredientName>', get_ingredientId),
    path('api/match_recipe/', get_match_recipe),
]