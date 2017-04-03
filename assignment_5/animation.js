document.addEventListener('DOMContentLoaded', animate, false);

function animate() {
	var snap = Snap("#animation_svg")

	time = 0
	max_time = run_settings['run_length']
	max_entities = run_settings['max_entities']

	fillBoxes(snap, max_entities, time)	

	setInterval(function() {
		if (time+1 < max_time) {
			time += 1
			fillBoxes(snap, max_entities, time)		
		} else {

		}
	}, run_settings['run_speed']);
}

function fillBoxes(snap, max_entities, time) {
	var elements = snap.selectAll('.box')
	elements.forEach(function(elem) {
		fillBox(snap, elem, max_entities, time)
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