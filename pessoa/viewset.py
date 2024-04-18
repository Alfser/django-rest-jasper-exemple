
import os
import base64

from django.http import HttpResponse
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from pyreportjasper import PyReportJasper

from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="PDF file",
                content_type={'application/pdf': {}},
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
            Export People as PDF
        """
        
        input_file = os.path.join(settings.REPORTS_DIR, 'postgres.jrxml')
        conn = {
            'driver': 'postgres',
            'username': settings.DB_USER,
            'password': settings.DB_PASSSWORD,
            'host': settings.DB_HOST,
            'database': settings.DB_NAME,
            'port': settings.DB_PORT,
            'jdbc_driver': 'org.postgresql.Driver'
        }
        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
            input_file=input_file,
            db_connection=conn,
            output_formats=["pdf"],
            locale='pt_BR'
        )
        
        report = pyreportjasper.instantiate_report()
        output_stream_pdf = report.get_output_stream_pdf()
        byte_array = output_stream_pdf.toByteArray()
        pdf_bytes = bytes(byte_array)
        
        # config pdf in a response
        response = HttpResponse(content=pdf_bytes)
        response['Content-Type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment; filename="people.pdf"'
        return response