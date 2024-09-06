from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

@api_view(['POST'])
def create_note(request):
    response = {
        'note_created': False,
        'success': False
    }
    status_code = status.HTTP_400_BAD_REQUEST

    try:
        
        serializer = NoteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            response['note_created'] = True
            response['success'] = True
            response['message'] = 'Note created successfully'
            status_code = status.HTTP_201_CREATED
        else:
            response['message'] = serializer.errors

    except Exception as e:
        response['message'] = str(e)
    return Response(response, status=status_code)


@api_view(['GET'])
def get_note(request, pk):
    response = {
        'note_found': False,
        'success': False
    }
    status_code = status.HTTP_404_NOT_FOUND

    try:
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note)
        response['note_found'] = True
        response['success'] = True
        response['message'] = 'Note retrieved successfully'
        response['data'] = serializer.data
        status_code = status.HTTP_200_OK
    except Note.DoesNotExist:
        response['message'] = 'Note not found'
    return Response(response, status=status_code)


@api_view(['GET'])
def query_notes_by_title(request):
    response = {
        'success': True
    }
    title_substring = request.query_params.get('title','')
    notes = Note.objects.filter(title__icontains=title_substring)
    serializer = NoteSerializer(notes, many=True)
    response['data'] = serializer.data

    return Response(response, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_note(request, pk):
    response = {
        'note_updated': False,
        'success': False
    }
    status_code = status.HTTP_400_BAD_REQUEST

    try:
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response['note_updated'] = True
            response['success'] = True
            response['message'] = 'Note updated successfully'
            status_code = status.HTTP_200_OK
        else:
            response['message'] = serializer.errors
    except Note.DoesNotExist:
        response['message'] = 'Note not found'
    return Response(response, status=status_code)