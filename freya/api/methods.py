from flask import jsonify

from freya.api import rpc
from freya.database.packets import IridiumPacket, FreyaPacket
from freya.database.node import FreyaNode
from freya import app

@rpc.method("getdata")
def getdata(timerange):
    if timerange == "last":
        pack = FreyaPacket.query.order_by(FreyaPacket.id.desc()).first()
        if not pack: return "None"
        return jsonify(pack.to_dict())
    return "wrong args"

@rpc.method("pushdata")
def pushdata(MOHeader, MOLocationInformation, MOPayload):
    try:
        app.logger.info("Pushing data")
        
        if not FreyaNode.get(imei=MOHeader[0]['IMEI']):
            node = FreyaNode(imei=MOHeader[0]['IMEI'])
            node.save()
        
        iri_pack = IridiumPacket(header=MOHeader[0],
                             loc=MOLocationInformation[0])
        iri_pack.save()

        for pack in MOPayload:
            fre_pack = FreyaPacket(pack, iri_pack)
            fre_pack.save()
            fre_pack.calc_radiation() #Awful >_<
            fre_pack.save()
            
        return u"done"
        
    except Exception as e:
        app.logger.error("Pushing data failure. %s %s %s", MOHeader, MOLocationInformation, MOPayload)
        
        return u"error"

