from flask_jsonrpc import jsonify

from freya import map_bp
from freya import app
from freya.models import FreyaPacket

global last_time
global last_ticks

last_time = 0
last_ticks = 0


@map_bp.route('/map_data')
def get_data():
    try:
        global telemetry
        global last_time
        global last_ticks

        freya_packet = FreyaPacket.query.order_by(FreyaPacket.id.desc()).first()

        time = freya_packet.time
        ticks = freya_packet.geiger_ticks

        lat = round(freya_packet.latitude, 4)
        lon = round(freya_packet.longitude, 4)
        press = round(freya_packet.bmp_press / 133.3224, 2)
        temp = round(freya_packet.ds_temp, 2)
        cdm = freya_packet.cdm_conc
        mq7 = round(freya_packet.mq7_conc, 2)

        if time != last_time:
            dticks = ticks - last_ticks
            dtime = (time - last_time) * 0.001
            geiger = round((dticks / 78) / dtime * 3600, 2)

            last_time = time
            last_ticks = ticks

            format_data = "Координаты: {0}, {1}<br>Давление: {2} мм рт. ст.<br>Температура: {3} °C<br>" \
                          "Концентрация CO2: {4} ppm<br>Концентрация CO: {5} ppm<br>Уровень радиации: {6} мкР/ч".format(
                lat, lon, press, temp, cdm, mq7, geiger
            )

            telemetry = {
            'last_time': last_time,
            'time': time,
            'lat': freya_packet.latitude,
            'lon': freya_packet.longitude,
            'press': round(freya_packet.bmp_press, 2),
            'temp': round(freya_packet.ds_temp, 2),
            'cdm': freya_packet.cdm_conc,
            'mq7': freya_packet.mq7_conc,
            'geiger': freya_packet.geiger_ticks,
            'format_data': format_data
            }

        return jsonify(telemetry)
    except Exception as e:
        app.logger.exception("Не могу получить данные для обновления карты")

        telemetry = {
            'lat': 0,
            'lon': 0,
            'format_data': 'Ого, похоже, данных нет'
        }

        return jsonify(telemetry)
