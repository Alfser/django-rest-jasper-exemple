from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from jasper_report.services import JasperReportService

from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """
        Endpoints people data registred in a system
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="PDF file",
                content={
                    'application/pdf': {}
                }
            )
        }
    )
    @action(
        detail=False,
        methods=['GET'],
        url_name='export_people', 
        url_path='export-people'
    )
    def export_people(self, request):
        """
            Export People registered as PDF
        """
        jasper_service = JasperReportService()

        pdf_bytes = jasper_service.get_pdf_bytes('postgres.jrxml')
        
        # config pdf in a response
        response = HttpResponse(content=pdf_bytes)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename="people.pdf"'
        return response