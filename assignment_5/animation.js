document.addEventListener('DOMContentLoaded', animate, false);

function animate() {
	var snap = Snap("#animation_svg")

	time = 0
	max_time = 1000

	fillBoxes(snap, time)	

	setInterval(function() {
		if (time+1 < max_time) {
			time += 1
			console.log(time)
			fillBoxes(snap, time)		
		} else {

		}
	}, 500);
}

function fillBoxes(snap, time) {
	var elements = snap.selectAll('.box')
	elements.forEach(function(elem) {
		fillBox(snap, elem, 100, time)
	})
}

function fillBox(snap, box, max_entities, time) {
	var box_id = box.attr('id')
	var value = run_data[box_id][time]

	for (var i = 0; i < max_entities; i += 1) {
		var entity_id = "#" + box_id + "_" + i
		var entity = snap.select(entity_id)

		if (value > 0 && value < 1) {
			entity.attr('visibility', 'hidden')
		} else if (i < value) {
			entity.attr('visibility', 'visible')
		} else {
			entity.attr('visibility', 'hidden')
		}
	}

	var partial_entity_id = "#" + box_id + "_partial"
	var partial_entity = snap.select(partial_entity_id)

	if (value > 0 && value < 1) {
		partial_entity.attr('visibility', 'visible')
		partial_entity.attr('style', 'fill: #CCCCCC')
	} else {
		partial_entity.attr('visibility', 'hidden')
	}
}