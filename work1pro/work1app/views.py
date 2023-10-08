#CRUD
from rest_framework.decorators import api_view
from work1app.models import Dictionary
from work1app.serializers import DictSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


#Search
class Search(ListAPIView):
    queryset=Dictionary.objects.all()
    serializer_class=DictSerializer
    filter_backends=(SearchFilter,)
    search_fields=('label','description')
    

# CRUD
@api_view(['GET'])
def apiOverview(request):
    api_urls = {\
        'Create':'/create/',
        'Search':'/search/',
        # 'SearchCount':'/search_count/',
        'Update':'/update/<str:pk>',
        'Delete':'/delete/<str:pk>',
        'ReadAll':'/readAll/',
    }
    return Response(api_urls)

# CREATE
@api_view(['POST'])
def create(request):
    serializer = DictSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# UPDATE
@api_view(['PUT'])
def update(request,pk):
    rec = Dictionary.objects.get(id=pk) 
    serializer = DictSerializer(instance=rec,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#DELETE BY ID
@api_view(['DELETE'])
def delete(request,pk):
    rec = Dictionary.objects.get(id=pk)
    rec.delete()
    return Response("item succesfully deleted")

# READ
@api_view(['GET'])
def readAll(request):
    tasks = Dictionary.objects.all() #ALL
    serializer = DictSerializer(tasks,many=True)
    return Response(serializer.data)












