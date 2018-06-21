from flask import render_template, abort
from jinja2 import TemplateNotFound

from freya import map_bp
from freya import db
from freya.models import FreyaPacket, IridiumPacket

@map_bp.route('/')
def map_index():
    try:
        irid_packet = IridiumPacket.query.order_by(IridiumPacket.id.desc()).first()
        freya_packet = FreyaPacket.query.order_by(FreyaPacket.id.desc()).first()

        format_data = "Координаты: {lat}, {lon}<br>Давление: {press}<br>Температура: {temp}<br>" \
            "Концентрация CO2: {cdm}<br>Концентрация CO: {mq7}<br>Уровень радиации: {geiger}".format(
            lat=irid_packet.latitude, lon=irid_packet.longitude, press=freya_packet.bmp_press,
            temp=freya_packet.bmp_temp, cdm=freya_packet.cdm_conc, mq7=freya_packet.mq7_conc,
            geiger=freya_packet.geiger_ticks
        )
        return render_template('map.html', lat=irid_packet.latitude, lon=irid_packet.longitude, desc=format_data)
    except TemplateNotFound:
        abort(404)