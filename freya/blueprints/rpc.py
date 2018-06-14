from freya import jsonrpc, db
from freya.models import IridiumPacket, FreyaPacket

from pprint import pprint

@jsonrpc.method("pushdata")
def index(**kwargs):

    pprint(kwargs)
    payload = kwargs

    irid = IridiumPacket()

    header = payload['MOHeader'][0]
    loc = payload['MOLocationInformation'][0]

    ir_pack = IridiumPacket()

    



    db.session.add(irid)

    db.session.commit()


    return u"la-la-la"

