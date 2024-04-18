"""
    Jasper Report services to generate reports files.
"""

from .config import JasperPostgresConfig


class JasperReportService:
    
    def __init__(self) -> None:
        """ Class 

        Args:
            report_file_jrxml (_type_): _description_
        """
        self.__config = JasperPostgresConfig()
        
    def __instantiate_report(self, report_file: str):
        
        self.__config.set_input_file(report_file)
        return self.__config.instantiate_report()
        
    def get_pdf_bytes(self, report_file: str) -> bytes:
        """
        Args:
            filename (str): a name of report file. Example: postgres.jrxml.
            Also, set jasper report file .jrxml to be used. That have to be in a root folder `report/` by default

        Returns:
            bytes: pdf bytes of report generated from jasper engine.
        """
        report = self.__instantiate_report(report_file)
        output_stream_pdf = report.get_output_stream_pdf()
        byte_array_pdf = output_stream_pdf.toByteArray()
        return bytes(byte_array_pdf)