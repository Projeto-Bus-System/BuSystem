function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
    else {
        alert("O seu navegador não suporta Geolocalização.");
    }
}

function showPosition(position){
    renderMap(position.coords.latitude, position.coords.longitude);
}

function renderMap(lat, long) {
    var mymap = L.map('mapid').setView([lat, long], 13);
  
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiamFja3Nvbi1tYXJjb255IiwiYSI6ImNrZXR5MGl5dzBnYWQydW8zazhzOHB3OXkifQ.KZ5x5JwGx6JVdFiGVxSfqQ'
    }).addTo(mymap);

mymap.on('click', (ev) => {
    
    let coord =  ev.latlng;
    console.log(coord);
    L.marker([coord.lat, coord.lng]).addTo(mymap);
});

}

function marker(lat, long, mymap) {
    return (L.marker([lat, long]).addTo(mymap));
}

getLocation();