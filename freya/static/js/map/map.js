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
    layers: [arcgisImagery],
    overlays: [marker],
    target: 'map'
});