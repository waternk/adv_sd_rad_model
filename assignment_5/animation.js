document.addEventListener('DOMContentLoaded', setUp, false);

var time = 0
var currentTime = 0
var timer_label
var timer
var playing = false

function setUp() {
	var play_button = document.getElementById("play")
	play_button.addEventListener("click", play)

	var pause_button = document.getElementById("pause")
	pause_button.addEventListener("click", pause)

	var stop_button = document.getElementById("stop")
	stop_button.addEventListener("click", stop)

	timer_label = document.getElementById("timer")
	timer_label.innerText = time

	var snap = Snap("#animation_svg")
	var boxes = snap.selectAll('.box')
	boxes.forEach(function(box) {
		box.mouseover(function() { showPopUp(snap, box) })
	})
}

function showPopUp(snap, box) {
	var x = parseInt(box.attr('x'))-2
	var y = parseInt(box.attr('y'))-2
	var width = parseInt(box.attr('width'))+4
	var height = parseInt(box.attr('height'))+4
	
	console.log(width+1 + " " + height)

	var dim_string = 'width="' + width + '" height="' + height + '" x="' + x + '" y="' + y + '"'
	var popup_id = box.attr('id') + '_popup'
	var popup_tag = '<foreignObject id="' + popup_id + '" class="popup" ' + dim_string
	var popup_body = '<body><div class="popup_text"><h1>' + box.attr('id').replace(/_/g, " ") + '</h1></div></body>'
	var popup_end_tag = '</foreignObject>'

	snap.append(Snap.parse( popup_tag + popup_body + popup_end_tag ))
	var popup = snap.select('#' + popup_id)
	popup.mouseout(function() { popup.remove() })
}

function play() {
	if (playing) {

	} else {
		playing = true
		var snap = Snap("#animation_svg")
	
		var max_time = run_settings['run_length']
		var max_entities = run_settings['max_entities']
		var run_speed = run_settings['run_speed']
	
		time = currentTime
		timer_label.innerText = time

		animate(snap, timer_label, max_time, max_entities, run_speed)
	}
}

function stop() {
	currentTime = 0
	playing = false
	clearInterval(timer)
}

function pause() {
	currentTime = time
	playing = false
	clearInterval(timer)
}

function animate(snap, timer_label, max_time, max_entities, run_speed) {
	timer = setInterval(function() {
		if (time < max_time) {
			timer_label.innerText = time
			fillBoxes(snap, max_entities, time)
			time += 1
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