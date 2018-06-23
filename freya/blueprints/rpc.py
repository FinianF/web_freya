from freya import jsonrpc, db, app
from freya.models import IridiumPacket, FreyaPacket
from datetime import datetime

@jsonrpc.method("pushdata")
def index(*kwargs):

    data = kwargs[0]

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

        freya_pack.bmp_press = pack['BMPPress'] / 133.3224
        freya_pack.bmp_temp = pack['BMPTemp'] / 100
        freya_pack.ds_temp = pack['DSTemp'] / 16

        freya_pack.accx = pack['X']
        freya_pack.accy = pack['Y']
        freya_pack.accz = pack['Z']

        freya_pack.cdm_conc = pack['CDMConc']
        #надо перевести это во что-то нормальное
        freya_pack.mq7_conc = pack['MQ7Conc']
        #и это
        freya_pack.geiger_ticks = pack['GeigerTicks']
        freya_pack.height = pack['Height']
        freya_pack.latitude = pack['Latitude']

        freya_pack.longitude = pack['Longitude']
        freya_pack.has_fix = pack['HasFix']

        db.session.add(freya_pack)

    db.session.commit()

    return u"la-la-la"