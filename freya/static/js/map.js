function draw(lat, lon, desc){
    var mousePositionControl = new ol.control.MousePosition({
        projection: 'EPSG:4326',
        coordinateFormat: function(coordinate) {
            return ol.coordinate.format(coordinate, '{y}, {x}', 5);
        }
    });

    var arcgisImagery = new ol.layer.Tile({
        source: new ol.source.TileArcGISRest({
            url: 'http://server.arcgisonline.com/arcgis/rest/services/ESRI_Imagery_World_2D/MapServer'
        })
    });

    var vector = new ol.layer.Vector({
        source: new ol.source.Vector({wrapX: false}),
        style: new ol.style.Style({
          fill: new ol.style.Fill({
            color: 'rgba(255, 255, 255, 0.2)'
          }),
          stroke: new ol.style.Stroke({
            color: '#ffcc33',
            width: 2
          }),
          image: new ol.style.Circle({
            radius: 3,
            fill: new ol.style.Fill({
              color: '#ff9933'
            })
          })
        })
    });

    var view = new ol.View({
        center: [ 4188426.7147939987, 7508764.236877314 ],
        zoom: 3
    });

    var map = new ol.Map({
        controls: ol.control.defaults().extend([
            mousePositionControl,
            new ol.control.ZoomSlider(),
            new ol.control.ScaleLine()
        ]),
        view: view,
        layers: [arcgisImagery, vector],
        target: 'map'
    });

    var pst = ol.proj.fromLonLat([lon, lat]);

    var popup = new ol.Overlay ({
        element: document.getElementById("popup")
    });
    map.addOverlay(popup);


    select = new ol.interaction.Select({
        condition: ol.events.condition.click
    });

    select.on('select', function(evt) {
        var element = popup.getElement();
        $(element).popover('hide');

        evt.selected.forEach( function(feature) {
            popup.setPosition(feature.getGeometry().getCoordinates());
            $(element).popover({
                'placement': 'top',
                'animation': false,
                'html': true
            });

            $(element).data('bs.popover').options.content = desc
            $(element).popover('show');

        });
    });

    map.addInteraction(select);


    feature = new ol.Feature({
        geometry: new ol.geom.Point(pst)
    });

    vector.getSource().addFeature(feature);
 };