from freya import app, db
from freya.blueprints.rpc import index

nan = None
a = {'MOHeader': [{'CDRReference': 1730168,
                   'IMEI': '333030323334303639313032303030',
                   'MOMSN': 297,
                   'MTMSN': 0,
                   'SessionStatus': 0,
                   'TimeOfSession': 1528896490}],
     'MOLocationInformation': [{'CEPRadius': 86,
                                'Indicator': '1',
                                'LatitudeDegrees': 65,
                                'LatitudeThousandthsOfMinute': 59214,
                                'LongitudeDegrees': 36,
                                'LongitudeThousandthsOfMinute': 56811}],
     'MOPayload': [{'BMPPress': 782176,
                    'BMPTemp': 3506,
                    'CDMConc': 730,
                    'DSTemp': 503,
                    'Flag': 'f4',
                    'GeigerTicks': 413,
                    'HasFix': False,
                    'Height': nan,
                    'Latitude': 55,
                    'Longitude': 35,
                    'MQ7Conc': 112,
                    'Time': 39280,
                    'X': 1.0440000295639038,
                    'Y': 0.06400000303983688,
                    'Z': 0.0}]}

db.init_app(app)
with app.app_context():
    index(a)

