from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ..domain.models import Invoice


class ReportService:
    def create_invoice(self,invoice: Invoice ):
        c = canvas.Canvas(f'{invoice.invoice_id}.pdf', pagesize=letter)
        ancho, alto = letter

        # self.period = 
        
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