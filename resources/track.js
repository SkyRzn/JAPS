var trackColor = null;
var trackOptions = {
	geodesic: true,
	strokeWeight: 2,
	zIndex: 3
};

var altMin = 0;
var altMax = 12000;
var altNone = -5000;
var altT1 = altMax/5;
var altT2 = altMax/5*2;
var altT3 = altMax/5*3;
var altT4 = altMax/5*4;

function altColor(alt1, alt2) {
	if (alt1 < altNone && alt2 < altNone)
		return '#CCC';

	if (alt1 < altNone)
		alt1 = alt2;
	if (alt2 < altNone)
		alt2 = alt1;

	alt = (alt1 + alt2)/2.0

	if (alt < altMin)
		alt = altMin;
	if (alt > altMax-1)
		alt = altMax-1;


	var r = 0;
	var g = 0;
	var b = 0;
	var k = 255.0/(altT1-1);

	if (alt < altT1) {
		r = 255;
		g = alt*k;
	} else if (alt >= altT1 && alt < altT2) {
		r = (altT2-1-alt)*k;
		g = 255;
	} else if (alt >= altT2 && alt < altT3) {
		g = 255;
		b = (alt-altT2)*k;
	} else if (alt >= altT3 && alt < altT4) {
		g = (altT4-1-alt)*k;
		b = 255;
	} else if (alt >= altT4) {
		r = (alt-altT4)*k;
		b = 255;
	}

	return 'rgb('+Math.round(r)+','+Math.round(g)+','+Math.round(b)+')';
}

function rainbowTrack(points) {
	var track = [];
	var len = points.length;

	if (len > 1) {
		for (var i = 0; i < len - 1; i++) {
			trackOptions.path = [points[i], points[i+1]];
			trackOptions.strokeColor = altColor(points[i].alt, points[i+1].alt);
			track.push(new google.maps.Polyline(trackOptions));
		}
	}
	return track;
}

function colorTrack(points) {
	trackOptions.path = points;
	return [new google.maps.Polyline(trackOptions)];
}

function drawTrack(points) {
	if (trackColor == null)
		return rainbowTrack(points);
	return colorTrack(points);
}

function setTrackStyle(width, color) {
	trackOptions.strokeWeight = width;
	trackColor = color;
	if (color)
		trackOptions.strokeColor = color;
}

