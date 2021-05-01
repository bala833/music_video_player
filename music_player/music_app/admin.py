# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Song, Video, RelatedSimilar, Mostwatch


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'title',
        'description',
        'music',
        'artist',
        'poster',
    )
    list_filter = ('created', 'modified')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'title',
        'description',
        'video',
        'artist',
        'poster',
    )
    list_filter = ('created', 'modified')


@admin.register(RelatedSimilar)
class RelatedSimilarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'title',
        'description',
        'relatedsimilar',
    )
    list_filter = ('created', 'modified', 'relatedsimilar')


@admin.register(Mostwatch)
class MostwatchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'title',
        'description',
        'mostwatch',
    )
    list_filter = ('created', 'modified', 'mostwatch')
