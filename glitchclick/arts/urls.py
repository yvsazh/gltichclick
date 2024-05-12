from django.urls import path
from . import views

app_name = 'arts'
urlpatterns = [
    path('', views.popular, name="popular"),
    path('most_saved/', views.saviest, name="saviest"),
    path('art/<int:art_id>', views.detail, name="detail"),
    path('search/', views.search, name="search"),
    path('add_favorite/<int:art_id>', views.add_favorite, name="add_favorite"),
    path('remove_favorite/<int:art_id>', views.remove_favorite, name="remove_favorite"),
    path('leave_comment/<int:art_id>/', views.leave_comment, name="leave_comment"),
    path('delete_comment/<int:comment_id><int:art_id>/', views.delete_comment, name="delete_comment"),
    path('recomendations/', views.recomendations, name="recomendations")
]
