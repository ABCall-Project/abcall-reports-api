from flask_restful import Resource
from flask import jsonify, request,Response
import requests
from http import HTTPStatus
from  config import Config
from ...application.report_service import ReportService
from ...domain.models import Invoice
import uuid
from datetime import datetime

from ...utils import Logger

log = Logger()

class InvoiceReport(Resource):
    """
    This class represent to invoce report api
    """
    def post(self):
        """
        api method to create a invoice document in pdf format      
        """
        try:
            invoice_id=uuid.UUID(request.json["id"])
            log.info(f'Receive request to generate invoice {request.json["id"]}')
            report_service= ReportService()


             
            invoice=Invoice(invoice_id,
                            uuid.UUID(request.json["customer_id"]),
                            request.json["invoice_id"],
                            uuid.UUID(request.json["plan_id"]),
                            float(request.json["amount"]),
                            float(request.json["tax"]),
                            float(request.json["total_amount"]),
                            request.json["status"],
                            request.json["created_at"],
                            request.json["start_at"],
                            request.json["generation_date"],
                            request.json["end_at"])
            report_service.create_invoice(invoice)
            log.info(f'Invoice {id} generated')
            return 'Invoice generated', HTTPStatus.OK
        except Exception as ex:
            log.error(f'Some error occurred trying to generated invoice {invoice_id}: {ex}')
            return {'message': 'Something was wrong trying generate invoice'}, HTTPStatus.INTERNAL_SERVER_ERROR
        

    def get(self,invoice_id):
        """
        api method to download a invoice document from storage
        Args:
            file (str): file to download from storage
        """
        try:
            report_service= ReportService()
            invoice =report_service.download_invoice_from_storage(invoice_id)
            if invoice:
                response = Response(invoice, mimetype='application/octet-stream')

                response.headers.set('Content-Disposition', 'attachment', filename=f'invoice-{invoice_id}.pdf')

                return response
            else:
                return 'Invoice not found', HTTPStatus.NOT_FOUND
        except Exception as ex:
            log.error(f'Some error occurred trying to download invoice {invoice_id}: {ex}')
            return {'message': 'Something was wrong trying download invoice'}, HTTPStatus.INTERNAL_SERVER_ERROR
        
        
        
