from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): #if you want clients to know what the issue is, pass this arg. Otherwise return statment after if block will execute
        # instance = serializer.save() 
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"Invalid Data": "Not Good Data"}, status=400)