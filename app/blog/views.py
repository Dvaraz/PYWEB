from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db.models import Avg

from .models import Note, Comment
from .serializers import NotesSerializer, NoteDetailSerializer, NoteEditorSerializer, CommentAddSerializer, CommentsSerializer
from django.conf import settings


class BlogNotesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        # notes = Note.objects.all().order_by('-date_add', 'title')

        notes = Note.objects.filter(public=True).order_by('-date_add', 'title').select_related('author')
        notes = notes.only('id', 'title', 'message', 'date_add', 'author__username')

        notes = notes.annotate(average_rating=Avg('comments__rating'))
        serializer = NotesSerializer(notes, many=True)

        return Response(serializer.data)


class BlogNoteDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, note_id):

        note = Note.objects.filter(pk=note_id, public=True, author=request.user).first()

        if not note:
            raise NotFound(f'Note with id {note_id} not found')

        serializer = NoteDetailSerializer(note)

        return Response(serializer.data)


class BlogNoteEditorView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):

        new_note = NoteEditorSerializer(data=request.data)

        if new_note.is_valid():
            new_note.save(author=request.user)
            return Response(new_note.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, note_id):

        note = Note.objects.filter(pk=note_id, author=request.user).first()

        if not note:
            raise NotFound(f'Note with id {note_id} for user {request.user} not found')

        new_note = NoteEditorSerializer(note, data=request.data, partial=True)

        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, status=status.HTTP_200_OK)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):

        note = Note.objects.filter(pk=note_id, author=request.user).first()

        if not note:
            raise NotFound('Not found')

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentDetailView(APIView):
    """ Note comments """
    permission_classes = (IsAuthenticated, )

    def post(self, request, note_id):
        """ New comment """

        note = Note.objects.filter(pk=note_id).first()
        if not note:
            raise NotFound(f'Note with id={note_id} not found')

        new_comment = CommentAddSerializer(data=request.data)
        if new_comment.is_valid():
            new_comment.save(note=note, author=request.user)
            return Response(new_comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        """ Delete comment """
        comment = Comment.objects.filter(pk=comment_id, author=request.user)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


