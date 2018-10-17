from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# from shop.models import Product
# from shop.serializers import ProductSerializer


# class PlaceOrder(generics.CreateAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

#    def perform_create(self, serializer):
#        serializer.save()
from exchange.serializers import ProductSerializer, OrderSerializer

from exchange.models import WishList, Order, Product


@api_view(['GET'])
def api_root(request, format=None):
    """

    You either got here on purpose, or by mistake.

    Welcome to the main place, where you can see our API. Please remember, that you have to be logged in to see the API
    contents listed here.

    For more information regarding proper API usage, please consult following links. This documentation is interactive
    so you may browse our APIs and try and check the results in a prowser or via ``` curl ``` command.

    You may want to use ``` http ```, command. If so, use ``` pip install httpclient ``` to install most recent version
    of the curl-like client to try our API.
    """
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'products': reverse('api-product-list', request=request, format=format),
        'orders': reverse('api-place-order', request=request, format=format)
    })


class PlaceOrder(generics.CreateAPIView):
    """
        You may place the order here

        In Product provide PK of the Product you wish to order

        In MethodOfDelivery provide PK of the Delivery method

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)

@api_view(['GET'])
def search_by_name(request, format=None):
    pass


@api_view(['GET'])
def UserList():
    return None


class ProductList(generics.ListAPIView):
    """
        List of products.

        Please remember, you may not change anything here via API. Products may be added via Staff Panel. <a href='/panel/'> Staff panel login </a>

        You may query additional information appending id to the link i.e. product/1/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    """
        # Details of the product

        You may see the details of the product.

        To like the product POST a message to: product/id/like
        To unlike the product DELETE to: product/id/like

        ## Post an image
        To add an image, upload it to some kind of a service (we don't use FileField because of performance issues - on big tables it may kill instantly database)
        and then provide a link

        ##
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST', 'DELETE'])
def ProductLike(request, pk):
    """
        # Liking and disliking the product

        ## To like the product
        POST here a message (contents are not crucial, as long as they are properly formatted using method selected)

        ## To dislike the product
        DELETE here

        ## Returns:

            406 - if the product is already liked
            202 - if product has been liked successfyully
            400 - if there is an error during validation
            404 - if the product is not available

    """
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":

        try:
            wishlist = WishList.objects.get(Product=product, user=request.user)
            if wishlist.objects.count() > 0:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            pass


        try:
            wishlist = WishList()
            wishlist.Product = product
            wishlist.user = request.user
            wishlist.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        """
            This part is currently prone to errors.
        """
        try:
            wishlist = WishList.objects.get(Product=product, user=request.user)
            for w in wishlist:
                w.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST)


