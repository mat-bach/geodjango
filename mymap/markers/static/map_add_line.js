document.getElementById("map").style.cursor = "crosshair";

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

const csrf_token = getCookie('csrftoken');
var name;

function name_prompt() {
    name = prompt("Please enter marker's name: ");
}

function onMapClick(e) {
    var marker = new L.marker(e.latlng).addTo(map);
    name_prompt();
    fetch('create-marker/', {
        method: 'POST',
        body:
            JSON.stringify({
            "name": name,
            "location": `SRID=4326;POINT(${e.latlng.lng} ${e.latlng.lat})`
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
