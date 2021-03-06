from django.urls import path

from pawbook import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "pawbook"

urlpatterns = [
    path('', views.home, name='home'),
    path("myPosts/<slug:name_slug>/", views.my_posts, name = "my_posts"),

    path('marketplace/', views.listings, name='marketplace'),
    path("marketplace/<slug:name_slug>/", views.show_listing, name = "show_listing"),

    path('posts/', views.posts, name='posts'),
    path("posts/<slug:name_slug>/", views.show_post, name = "show_post"),
    path('like_post/', views.LikePostView.as_view(), name='like_post'),
    path('dislike_post/', views.DislikePostView.as_view(), name='dislike_post'),

    path('pet-o-pedia/', views.pet_pedia, name='pet-o-pedia'),
    path("pet-o-pedia/<slug:name_slug>/", views.show_petPedia, name = "show_petPedia"),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),

    path('register/', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path("logout/", views.userLogout, name = "logout"),

    path("user/<slug:name_slug>/", views.show_profile, name = "show_profile"),
    path("editProfile/<slug:name_slug>", views.edit_profile, name="editProfile"),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)