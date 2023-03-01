
from django.urls import path
from . import views


urlpatterns = [
    path("posts/",views.tech),
    path("tech_post/",views.tech_post),
    path("clients/",views.client),
    path("authors/",views.author),
    path("client_login/",views.client_login,name="client_loggin"),
    path("client_logout/",views.client_logout,name="client_loggin"),
    path("author_login/",views.author_login,name="author_loggin"),
    path("author_logout/",views.author_logout,name="author_loggin"),
    path('comment/',views.comment,name="comment"),
    path('client_pw_change/',views.client_change_password,name="client_pw_change"),
    path('author_pw_change/',views.author_change_password,name="author_pw_change"),
]
