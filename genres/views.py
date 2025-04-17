from django.http import JsonResponse
from genres.models import Genre  
import json

# Create your views here.
def genre_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()  # Assuming you have a Genre model
        data = [{'id':genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data,safe=False)  # Return the data as JSON response


    elif request.method == 'POST':
        json.loads(request.body.decode('utf-8'))


