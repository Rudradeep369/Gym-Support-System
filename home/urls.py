from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", views.index, name="home"),
   path("member", views.member, name="member"),
   path("search", views.search, name="search"),
   path("receipt", views.receipt, name="receipt"),
   path('receipt/<int:pk>/', views.receipt_detail, name='receipt_detail'),
   path("profile/<int:admission_id>/", views.profile, name="profile"),
   path('profile/<int:pk>/edit/', views.edit_profile, name='edit_profile'),
   path('profile/<int:pk>/delete/', views.delete_profile, name='delete_profile'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
