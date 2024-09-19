from flask_restful import Resource
from flask import jsonify, request
import requests
from http import HTTPStatus
from  config import Config
from ...application.report_service import ReportService
from ...domain.models import Invoice
import uuid
from datetime import datetime

config = Config()

class InvoiceReport(Resource):
    def post(self):
        report_service= ReportService()
        invoice=Invoice(uuid.uuid4(),uuid.uuid4(),'abc123',uuid.uuid4(),0,0,0,'Emprendedor',uuid.uuid4(),'paid',
                        datetime.now(),
                        datetime.now(),
                        datetime.now(),
                        datetime.now())
        report_service.create_invoice(invoice)
        return 'Invoice generated', HTTPStatus.OK