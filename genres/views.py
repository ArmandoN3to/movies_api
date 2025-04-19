# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# import json

from rest_framework import generics
from genres.serializers import GenreSerializer
from genres.models import Genre  




class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Genre.objects.all()
    serializer_class = GenreSerializer
    


#Create your functions based views here.

# @csrf_exempt  
# def genre_create_list_view(request):

#     if request.method == 'GET':
#         genres = Genre.objects.all()  # Assuming you have a Genre model
#         data = [{'id':genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data,safe=False)  # Return the data as JSON response


#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name':new_genre.name},
#             status=201  # Created
#         )
# @csrf_exempt
# def genre_detail_view(request,pk):
#     genre=get_object_or_404(Genre,pk=pk)

#     if request.method =='GET':
#         data={'id': genre.id, 'name':genre.name}
#         return JsonResponse(data,safe = False)

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({
#             'id': genre.id, 'name':genre.name}, status = 200)
    
#     elif request.method =='DELETE':
#         genre.delete()
#         return JsonResponse({'message':f'{genre.name} deleted successfully'},
#         status=204) 



