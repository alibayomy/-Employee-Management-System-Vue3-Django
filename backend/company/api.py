from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
#defining all the Company realted end points


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_companies(request):
    """Return a json response with
        all the companies from the database
        Only if the user is authenticated"""
    companies = Company.objects.all()
    company_serialzier = CompanySerializer(companies, many=True)
    return Response(company_serialzier.data, status=status.HTTP_202_ACCEPTED )


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_company_by_id(request, id):
    """Given the id in the request
        return the desired company"""
    try:
        company = Company.objects.get(id = id)
        company_serliazer = CompanySerializer(company)
        return Response(company_serliazer.data, status=status.HTTP_202_ACCEPTED)
    except Company.DoesNotExist:
        return Response({
            'details': 'Company not found'
            }
        , status=status.HTTP_404_NOT_FOUND)