from cmath import e

from freya import jsonrpc, db, app
from freya.models import IridiumPacket, FreyaPacket
from datetime import datetime


def gps_convert(raw_data):
    raw_data = str(raw_data)
    data_degree = raw_data[:2] + "."
    data_minute = int(raw_data[3:]) // 60
    convert_data = float(data_degree + str(data_minute))

    return convert_data

def do_push_data(data):

    irid = IridiumPacket()

    header = data['MOHeader'][0]
    loc = data['MOLocationInformation'][0]

    irid.sdr_reference = header['CDRReference']
    irid.imei = header['IMEI']
    irid.session_status = header['SessionStatus']
    irid.momsn = header['MOMSN']
    irid.mtmsn = header['MTMSN']
    irid.time_of_session = datetime.utcfromtimestamp(header['TimeOfSession'])

    irid.indicator = loc['Indicator']
    irid.latitude = loc['LatitudeDegrees']
    irid.longitude = loc['LongitudeDegrees']
    irid.cep_radius = loc['CEPRadius']

    db.session.add(irid)


    payload = data['MOPayload']

    for pack in payload:
        freya_pack = FreyaPacket()
        freya_pack.ref_iridium_packet = irid

        freya_pack.flag = pack['Flag']
        freya_pack.time = pack['Time']

        freya_pack.bmp_press = pack['BMPPress']
        freya_pack.bmp_temp = pack['BMPTemp'] / 100
        freya_pack.ds_temp = pack['DSTemp'] / 16

        freya_pack.accx = pack['X']
        freya_pack.accy = pack['Y']
        freya_pack.accz = pack['Z']

        freya_pack.cdm_conc = pack['CDMConc']
        freya_pack.mq7_conc = 3.027 * e**(1.0698 * (5 / 1023 * pack['MQ7Conc']))
        freya_pack.geiger_ticks = pack['GeigerTicks']
        freya_pack.height = pack['Height']
        freya_pack.has_fix = pack['HasFix']

        pre_lat = pack['Latitude'] / 100
        pre_lon = pack['Longitude'] / 100
        freya_pack.latitude = gps_convert(pre_lat)
        freya_pack.longitude = gps_convert(pre_lon)

        db.session.add(freya_pack)

        print("АГА! Я что-то получил")

    db.session.commit()


@jsonrpc.method("pushdata")
def index(**args):

    try:
        data = args
        app.logger.info("got data from daemon. data: %s", data)
        do_push_data(data)
        print("АГА! Я что-то получил")
        return u"la-la-la"
    except Exception as e:
        app.logger.exception("something is not ok! data: %s", data)
        raise

