const copy = "© <a href='https://osm.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
const markers = JSON.parse(document.getElementById("markers-data").textContent);
const features = L.geoJSON(markers).bindPopup(layer => layer.feature.properties.name);
map.addLayer(features).fitBounds(features.getBounds());