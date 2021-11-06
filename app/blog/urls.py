from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'blog'

urlpatterns = [
    path('blog/notes/', views.BlogNotesView.as_view(), name='notes'),
    path('blog/notes/<int:note_id>/', views.BlogNoteDetailView.as_view(), name='note_detail'),
    path('blog/note/add/', views.BlogNoteEditorView.as_view(), name='note_post'),
    path('blog/note/<int:note_id>/', views.BlogNoteEditorView.as_view(), name='note_patch'),

    path('blog/comment/<int:note_id>/add/', views.CommentDetailView.as_view(), name='comment_add'),
    path('blog/comment/<int:comment_id>/delete/', views.CommentDetailView.as_view(), name='comment_del'),
]