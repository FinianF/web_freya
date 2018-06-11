var pst = ol.proj.fromLonLat([37.8519, 55.9317]);

var marker = new ol.Overlay({
position: pst,
positioning: 'center-center',
element: document.getElementById('marker'),
stopEvent: false
});