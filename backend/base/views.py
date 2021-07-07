
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product, Reservation
from .serializers import ProductSerializer, ReservationSerializer
# Create your views here.


class MyRoutes(APIView):
    def get(self, request):
        return Response("Hello")


class ProductsList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'brand': request.data.get('brand'),
            'image': request.data.get('image'),
            'countInStock': request.data.get('countInStock'),
            'category': request.data.get('category'),
            'description': request.data.get('description')
        }
        serializer = ProductSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('erreur: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'brand': request.data.get('brand'),
            'image': request.data.get('image'),
            'countInStock': request.data.get('countInStock'),
            'category': request.data.get('category'),
            'description': request.data.get('description')
        }
        serializer = ProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('erreur: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """  def post(self, request):
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'brand': request.data.get('brand'),
            'image': request.data.get('image'),
            'countInStock': request.data.get('countInStock'),
            'category': request.data.get('category'),
            'description': request.data.get('description')
        }
        serializer = ProductSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('erreur: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response({'res': 'Produit supprimé'}, status=status.HTTP_200_OK)


class ReservationList(APIView):
    def get(self, request):
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = {
            'fullname': request.data.get('fullname'),
            'phone': request.data.get('phone'),
            'brand': request.data.get('brand'),
            'idDest': request.data.get('idDest'),
            'email': request.data.get('email'),
        }
        serializer = ReservationSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('erreur: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
