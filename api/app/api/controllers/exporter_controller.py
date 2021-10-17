import pandas as pd

from io import BytesIO, StringIO
from flask_restx import Namespace, Resource
from flask import send_file

from pandas.io.json import json_normalize

from ...shared.models.furniture import FurnitureDAO

exporter_controller = Namespace(
    'Exporter', 'Exporter endpoint', '/export')

@exporter_controller.route('')
class CSVExporterController(Resource):

    @exporter_controller.response(200, 'Successfully exported CSV data')
    def post(self):
        all_daos = [dao._data for dao in FurnitureDAO.objects]
        df = pd.json_normalize(all_daos)
        buf_str = StringIO(df.to_csv())
        buf_byt = BytesIO(buf_str.read().encode('utf-8'))
        return send_file(
            buf_byt,
            mimetype='text/csv',
            attachment_filename='used_furniture_data.csv',
            as_attachment=True
        )

