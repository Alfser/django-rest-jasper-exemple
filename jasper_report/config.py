"""
    Module to configurate jasper report for application
"""
from django.conf import settings
import os 

from pyreportjasper import PyReportJasper
from pyreportjasper.config import Config

class JasperPostgresConfig(PyReportJasper):
    config: Config = Config()
    
    def __init__(self) -> None:
        self.config.input = None
        self.config.locale = 'pt_BR'
        self.config.outputFormats = ["pdf"]
        self.config.resource = None
        self.config.subreports = {}
        self.config.params = {}
        self.config.output = None
        self.config.dbType = 'postgres'
        self.config.dbUser = settings.DB_USER
        self.config.dbPasswd = settings.DB_PASSSWORD
        self.config.dbHost = settings.DB_HOST
        self.config.dbName = settings.DB_NAME
        self.config.dbPort = settings.DB_PORT
        self.config.dbDriver = 'org.postgresql.Driver'
    
    def set_input_file(self, filename):
        """Set jasper report to be used. That have to be in a root folder `report/`

        Args:
            filename (str): a name of report file. Example: postgres.jrxml
        """
        self.config.input = os.path.join(settings.REPORTS_DIR, filename)
    
    def set_output_file(self, filename):
        """Set a name for output report file . That will be created in a root folder `report/`

        Args:
            filename (str): a name of report file. Example: 'people_report'
        """
        self.config.output = os.path.join(settings.REPORTS_DIR, filename)