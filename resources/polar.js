var polars = {};

function addPolar(id, color, data) {
	polars[id] = new google.maps.Polygon({	paths: data,
		strokeColor: color,
		fillColor: color,
		strokeOpacity: 0.7,
		strokeWeight: 1,
		fillOpacity: 0.1,
		map: map,
		zIndex: 1
	});
}

function updatePolar(id, color, data) {
	polars[id].setPaths(data);
	polars[id].setOptions({strokeColor: color, fillColor: color});
}

function removePolar(id) {
	polars[id].setMap(null);
	delete polars[id];
}
