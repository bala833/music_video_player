from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from django.conf.urls import url
from music_app.views import( landing_page, play_music,second_login_,login_page,admin_all_list,
                            logout_view,add_song,edit_song,delete_song,initial_delete,video_player,play_video,
                            add_video,admin_all_video_list,edit_video,initial_delete_video,delete_video,song_autocomplete,
                            search_song_submit,video_autocomplete,search_video_submit)

urlpatterns = [
    path("", landing_page, name="landing_page"),
    url(r'^play_music/(?P<pk>[-\w]+)/$', play_music, name="play_music"),
    url(r'^login_page/$', login_page, name="login_page"),
    url(r'^second_login_/$', second_login_, name="second_login_"),

    url(r'^video_player/(?P<pk>[-\w]+)/$', video_player, name="video_player"),
    url(r'^play_video/$', play_video, name="play_video"),
    url(r'^add_video/$', add_video, name="add_video"),
    url(r'^admin_all_video_list/$', admin_all_video_list, name="admin_all_video_list"),
    url(r'^edit_video/(?P<pk>[-\w]+)/$', edit_video, name="edit_video"),
    url(r'^initial_delete_video/(?P<pk>[-\w]+)/$', initial_delete_video, name="initial_delete_video"),
    url(r'^delete_video/(?P<pk>[-\w]+)/$', delete_video, name="delete_video"),
    
    # search song autocomplete 
    url(r'^song_autocomplete/$', song_autocomplete, name="song_autocomplete"),
    url(r'^search_song_submit/$', search_song_submit, name="search_song_submit"),
    # search video autocomplete 
    url(r'^video_autocomplete/$', video_autocomplete, name="video_autocomplete"),
    url(r'^search_video_submit/$', search_video_submit, name="search_video_submit"),
    
    # admin
    url(r'^admin_all_list/$', admin_all_list, name="admin_all_list"),
    url(r'^logout_view/$', logout_view, name="logout_view"),
    url(r'^add_song/$', add_song, name="add_song"),
    url(r'^edit_song/(?P<pk>[-\w]+)/$', edit_song, name="edit_song"),
    url(r'^initial_delete/(?P<pk>[-\w]+)/$', initial_delete, name="initial_delete"),
    url(r'^delete_song/(?P<pk>[-\w]+)/$', delete_song, name="delete_song"),
    # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("music_player.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
