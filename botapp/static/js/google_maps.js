let map;
let marker;
let coordinates = {lat: 48.866667, lng: 2.333333};

function initMap() {
	let options = {
		zoom: 3,
		center: coordinates,
	};
	map = new google.maps.Map(document.getElementById('map'), options);

	marker = new google.maps.Marker({ // to set a default marker
		position: coordinates,
		map: map,
		title: 'Paris'
	});
	marker.setMap(map);
};

google.maps.event.addDomListener(window, "load", initialize);

function setLocation(latitude, longitude) { // to update marker location according to returned data
    coordinates = {lat: latitude, lng: longitude};
    marker.setPosition(coordinates);
    map.panTo(coordinates);
    map.setZoom(15);
};

