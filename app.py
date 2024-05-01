from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from modelo.codigo_produccion import AnalisisSentimientos

app = Flask(__name__)
CORS(app)  
analisis= AnalisisSentimientos()

api = Api(
    app, 
    version='1.0', 
    title='Analisis de sentimientos',
    description='Logic Gates Predictor')

ns =api.namespace('Verificar_sentimientos')
   
parser = api.parser()

parser.add_argument(
    'Mensaje', 
    type=str, 
    required=True, 
    help='Introduccir mensaje', 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/Analisis')
class sentimientos(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()

        return {
         "result": analisis.clasificar_sentimiento(args['Mensaje'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)