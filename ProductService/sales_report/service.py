from sales_report.repository import ReportRepository

class ReportService:
    def __init__(self):
        self.repository = ReportRepository()

    def get_sales_report(self, query_params):
        # Aquí podrías agregar lógica para filtrar el informe basado en fechas o parámetros.
        report = self.repository.generate_sales_report(query_params)
        
        return report
