function altColor(alt1, alt2) {
	if (alt1 == -10000 && alt2 == -10000)
		return '#CCC';
	if (alt1 == -10000)
		alt1 = alt2
		if (alt2 == -10000)
			alt2 = alt1
			alt = (alt1 + alt2)/2.0

			if (alt < 0)
				alt = 0;
			if (alt > 9999)
				alt = 9999;


			var r = 0;
		var g = 0;
		var b = 0;
		var k = 255.0/1999;

		if (alt < 2000) {
			r = 255;
			g = alt*k;
		} else if (alt >= 2000 && alt < 4000) {
			r = (3999-alt)*k;
			g = 255;
		} else if (alt >= 4000 && alt < 6000) {
			g = 255;
			b = (alt-4000)*k;
		} else if (alt >= 6000 && alt < 8000) {
			g = (7999-alt)*k;
			b = 255;
		} else if (alt >= 8000) {
			r = (alt-8000)*k;
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

