from freya.api import rpc
from freya.database.packets import IridiumPacket, FreyaPacket
from freya import app


@rpc.method("pushdata")
def pushdata(MOHeader, MOLocationInformation, MOPayload):
    try:
        app.logger.info("Pushing data")
        
        iri_pack = IridiumPacket(header=MOHeader[0],
                             loc=MOLocationInformation[0])
        iri_pack.save()

        for pack in MOPayload:
            fre_pack = FreyaPacket(pack, iri_pack)
            fre_pack.save()
            
        return u"done"
        
    except Exception as e:
        app.logger.error("Pushing data failure. %s %s %s", MOHeader, MOLocationInformation, MOPayload)
        
        return u"error"

