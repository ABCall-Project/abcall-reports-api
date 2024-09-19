from flask_restful import Resource
from flask import jsonify, request
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
    def post(self):
        try:
            invoice_id=uuid.UUID(request.json["id"])
            log.info(f'Receive request to generate invoice {request.json["id"]}')
            report_service= ReportService()
            invoice=Invoice(invoice_id,
                            uuid.UUID(request.json["customer_id"]),
                            request.json["invoice_id"],
                            uuid.UUID(request.json["payment_id"]),
                            float(request.json["amount"]),
                            float(request.json["tax"]),
                            float(request.json["total_amount"]),
                            request.json["subscription"],
                            uuid.UUID(request.json["subscription_id"]),
                            request.json["status"],
                            request.json["created_at"],
                            request.json["updated_at"],
                            request.json["generation_date"],
                            request.json["period"])
            report_service.create_invoice(invoice)
            log.info(f'Invoice {id} generated')
            return 'Invoice generated', HTTPStatus.OK
        except Exception as ex:
            log.error(f'Some error occurred trying to generated invoice {invoice_id}: {ex}')
            return {'message': 'Something was wrong trying generate invoice'}, HTTPStatus.INTERNAL_SERVER_ERROR
