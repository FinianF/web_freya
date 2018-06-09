var mousePositionControl = new ol.control.MousePosition({
    projection: 'EPSG:4326',
    coordinateFormat: function(coordinate) {
        return ol.coordinate.format(coordinate, '{y}, {x}', 5);
    }
});

var container = document.getElementById('popup');
var content = document.getElementById('popup-content');
var closer = document.getElementById('popup-closer');

var overlay = new ol.Overlay({
element: container,
autoPan: true,
autoPanAnimation: {
  duration: 250
}
});

closer.onclick = function() {
overlay.setPosition(undefined);
closer.blur();
return false;
};

var map = new ol.Map({
    controls: ol.control.defaults().extend([
        mousePositionControl,
        new ol.control.ZoomSlider(),
        new ol.control.ScaleLine()
    ]),
    overlays: [overlay],
    target: 'map'
});

var arcgisImagery = new ol.layer.Tile({
    source: new ol.source.TileArcGISRest({
        url: 'http://server.arcgisonline.com/arcgis/rest/services/ESRI_Imagery_World_2D/MapServer'
    })
});
map.addLayer(arcgisImagery);

var view = new ol.View({
    center: [ 4188426.7147939987, 7508764.236877314 ],
    zoom: 3
});
map.setView(view);

map.on('singleclick', function(evt) {
var coordinate = evt.coordinate;
var hdms = ol.coordinate.format(ol.proj.transform(
    coordinate, 'EPSG:3857', 'EPSG:4326'), '{y}, {x}', 5);

content.innerHTML = '<p>You clicked here:</p><code>' + hdms + '</code>';
overlay.setPosition(coordinate);
});