var planes = {};


var planeIcon = {
	path: "M 31.905133,19.520033 17.924874,9.196407 c 0.103467,-1.594857 0.170761,-5.156102 0.110170,-5.817176 -0.507919,-5.541654 -4.025643,-3.154674 -4.058277,-0.681443 -0.008933,0.676447 -0.130838,4.175266 -0.142400,6.511255 L 0.036643,19.772734 0.000000,23.079827 l 14.243781,-6.465884 0.514748,10.283910 -4.130361,2.937965 -0.026276,2.164192 5.448929,-1.485195 0.001031,0.017867 5.505819,1.398500 -0.065649,-2.162297 -4.183362,-2.868912 0.336605,-10.291649 14.354555,6.212758 -0.094735,-3.301050 z",
	fillColor: 'yellow',
	fillOpacity: 1,
	scale: 1,
};

var planeOptions = {
	icon: planeIcon,
	zIndex: 4
};


function addPlane(id, points, info) {
	planeIcon.rotation = info.azimuth;
	lastPoint = points[points.length - 1];

	planeOptions.position = lastPoint;
	planeOptions.title = id + ': ' + lastPoint.alt;

	var marker = new google.maps.Marker(planeOptions);

	planes[id] = {marker: marker, track: drawTrack(points)};
}

function addPlanePoints(id, points, info) {
	planeIcon.rotation = info.azimuth;
	lastPoint = points[points.length - 1];

	planes[id].marker.setPosition(lastPoint);
	planes[id].marker.setOptions({icon: planeIcon, title: title = id + ': ' + lastPoint.alt});

	planes[id].track = planes[id].track.concat(drawTrack(points));
}

function removePlane(id) {
	planes[id].marker.setMap(null);
	var track = planes[id].track;
	for (var i = 0; i < track.length; i++) {
		track[i].setMap(null);
	}
	delete planes[id];
}

function cleanPlanes() {
	for (id in planes) {
		console.log('remove ' + id)
		removePlane(id);
	}
}

function setPlaneStyle(size, color) {
	planeIcon.scale = size/32.0;
	planeIcon.fillColor = color;
}


