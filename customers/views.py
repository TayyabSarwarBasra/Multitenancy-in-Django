from django.shortcuts import render
from customers.models import Client, Domain
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework import viewsets, status, generics, exceptions


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ClientSignUpSerializer


    def create(self, request, *args, **kwargs):
        """
        Create a new client
        :Parameter: name, paid_until, on_trial
        :Authentication: nill
        """

        try:

            tenant = Client(schema_name=request.data.get("username"),
                            email=request.data.get("email"),
                            first_name=request.data.get("first_name"),
                            last_name=request.data.get("last_name"),
                            mobile_number=request.data.get("mobile_number"),
                            business_name=request.data.get("business_name"),
                            password=request.data.get("password"),
                            address=request.data.get("address"), )

            tenant.save()

            domain = Domain()
            domain.domain = request.data.get("username")+".localhost.com"             # don't add your port or www here! on a local server you'll want to use localhost here
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
            response = {"statusCode": 200, "error": False, "message": "Client created successfully!"}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            error = {"statusCode": 400, "error": True, "data": "", "message": "Bad Request, Please check request",
                     "errors": e.args[0]}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)















