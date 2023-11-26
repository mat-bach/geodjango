const copy = "© <a href='https://osm.org/copyright'>OpenStreetMap</a> contributors";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const osm = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [osm], minZoom: 5 });
map
    .locate()
    .on("locationfound", (e) => map.setView(e.latlng, 8))
    .on("locationerror", () => map.setView([0, 0], 5));
//const markers = JSON.parse(document.getElementById("markers-data").textContent);
//const features = L.geoJSON(markers).bindPopup(layer => layer.feature.properties.name);
//map.addLayer(features).fitBounds(features.getBounds());
async function load_markers() {
    const markers_url = `/api/markers/?in_bbox=${map.getBounds().toBBoxString()}`;
    const response = await fetch(markers_url);
    const geoJSON = await response.json();
    return geoJSON
}

async function render_markers() {
    const markers = await load_markers();
    L.geoJSON(markers)
      .bindPopup((layer) => layer.feature.properties.name)
      .addTo(map);
}

map.on('moveend', render_markers)

function getCookie(name) {
  if (!document.cookie) {
    return null;
  }

  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }
  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

function onMapClick(e) {
    const csrf_token = getCookie('CSRF-TOKEN');
    var marker = new L.marker(e.latlng).addTo(map);
    fetch('create-marker/', {
        method: 'POST',
        body:
            JSON.stringify({
            "name": "test_js",
            "location": "SRID=4326;POINT(13 13)"
        }),
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrf_token
        }
    })
        .then((response) => response.json())
        .then((json) => console.log(json));
}

map.on('click', onMapClick);
