from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ..domain.models import Invoice
from azure.storage.blob import BlobServiceClient
from  config import Config
import os

class ReportService:
    def create_invoice(self,invoice: Invoice ):

        invoice_file=f'generated/invoice-{invoice.invoice_id}.pdf'
        c = canvas.Canvas(invoice_file, pagesize=letter)
        weight, high = letter

        
        
        c.drawString(100, 750, f"Factura # {invoice.invoice_id}")
        c.drawString(100, 730, f"Cliente {invoice.customer_id}")
        c.drawString(100, 710, f"Id Pago {invoice.payment_id}")
        c.drawString(100, 690, f"Monto {invoice.amount}")
        c.drawString(100, 670, f"Impuestos {invoice.tax}")
        c.drawString(100, 650, f"Total {invoice.total_amount}")
        c.drawString(100, 630, f"Suscripción {invoice.subscription}")
        c.drawString(100, 610, f"Id Suscripción {invoice.subscription_id}")
        c.drawString(100, 590, f"Estado {invoice.status}")
        c.drawString(100, 570, f"Fecha creación {invoice.created_at}")
        c.drawString(100, 550, f"Fecha actualización {invoice.updated_at}")
        c.drawString(100, 530, f"Fecha generación {invoice.generation_date}")
        c.drawString(100, 510, f"Periodo {invoice.period}")
        
        
        c.save()

        self.upload_invoice_to_storage(invoice_file)

        if os.path.exists(f'generated/invoice-{invoice.invoice_id}.pdf'):
            os.remove(f'generated/invoice-{invoice.invoice_id}.pdf')



    def upload_invoice_to_storage(self,local_file):
        config = Config()
        connection_string = Config.CONNECTION_STRING_STORAGE #"DefaultEndpointsProtocol=https;AccountName=abcallstorage;AccountKey=sYcvU0A8NNajwyzkx/Z8vsVQ9h8OCe9F+NYRKp2CWcUbH1uKCUhxfU+jMGATU3jtQHM1QuJafbcT+ASta3TjmQ==;EndpointSuffix=core.windows.net"  
        container_name = Config.CONTAINER_STORAGE # "invoices"
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        with open(local_file, "rb") as data:
            blob_client = container_client.get_blob_client(blob=local_file)
            blob_client.upload_blob(data, overwrite=True)

        

