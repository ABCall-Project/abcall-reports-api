from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ..domain.models import Invoice
from azure.storage.blob import BlobServiceClient
from  config import Config
import os

class ReportService:
    """
    This class is to generate reports for platform
    """
    def create_invoice(self,invoice: Invoice):
        """
        method to create a invoice document in pdf format
        Args:
            invoice (Invoice): invoice data object            
        """
        invoice_file=f'generated/invoice-{invoice.invoice_id}.pdf'
        c = canvas.Canvas(invoice_file, pagesize=letter)
        weight, high = letter

        
        
        c.drawString(100, 750, f"Factura # {invoice.invoice_id}")
        c.drawString(100, 730, f"Cliente {invoice.customer_id}")
        c.drawString(100, 710, f"Id Plan {invoice.plan_id}")
        c.drawString(100, 690, f"Monto {invoice.amount}")
        c.drawString(100, 670, f"Impuestos {invoice.tax}")
        c.drawString(100, 650, f"Total {invoice.total_amount}")
        c.drawString(100, 590, f"Estado {invoice.status}")
        c.drawString(100, 570, f"Fecha creación {invoice.created_at}")
        c.drawString(100, 550, f"Fecha de inicio {invoice.start_at}")
        c.drawString(100, 530, f"Fecha generación {invoice.generation_date}")
        c.drawString(100, 510, f"Fecha de fin {invoice.end_at}")
        
        
        c.save()

        self.__upload_invoice_to_storage(invoice_file)

        if os.path.exists(f'generated/invoice-{invoice.invoice_id}.pdf'):
            os.remove(f'generated/invoice-{invoice.invoice_id}.pdf')



    def __upload_invoice_to_storage(self,local_file):
        """
        method to send a document to  storage
        Args:
            local_file (str): file to send to storage
        """
        connection_string = Config.CONNECTION_STRING_STORAGE 
        container_name = Config.CONTAINER_STORAGE 
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        with open(local_file, "rb") as data:
            blob_client = container_client.get_blob_client(blob=local_file)
            blob_client.upload_blob(data, overwrite=True)


    def download_invoice_from_storage(self, invoice_id):
        """
        method to download a document from  storage
        Args:
            file (str): file to download from 
        """
        try:
            file=f'generated/invoice-{invoice_id}.pdf'
            blob_service_client = BlobServiceClient.from_connection_string(Config.CONNECTION_STRING_STORAGE)
            blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_STORAGE , blob=file)
            blob_data = blob_client.download_blob()
            return blob_data.readall()
        except Exception as ex:
                return None


        

