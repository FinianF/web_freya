from cmath import e

from freya import jsonrpc, db, app
from freya.models import IridiumPacket, FreyaPacket
from datetime import datetime


@jsonrpc.method("pushdata")
def index(**args):
    try:
        data = args
        app.logger.info("got data from daemon. data: %s", data)
        
        iri_pack = IridiumPacket(header=data['MOHeader'][0],
                             loc=data['MOLocationInformation'][0])
        iri_pack.save()
        
        payload = data['MOPayload']

        for pack in payload:
            fre_pack = Freya_Packet(pack, iri_pack)
            fre_pack.save()
            
        print("АГА! Я что-то получил")
        return u"la-la-la"
    except Exception as e:
        app.logger.exception("something is not ok! data: %s", data)
        raise

