function openModal(id) {
	var modal = document.getElementById(id);
	modal.style.display = 'inherit';
}

function closeModal(id) {
	var modal = document.getElementById(id);
	modal.style.display = 'none';
}

// function to format time
String.prototype.toTime = function() {
	var sec_num = parseInt(this, 10);
	var hours   = Math.floor(sec_num / 3600);
	var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
	var seconds = sec_num - (hours * 3600) - (minutes * 60);
	if (hours   < 10) { hours   = "0" + hours; }
	if (minutes < 10) { minutes = "0" + minutes; }
	if (seconds < 10) { seconds = "0" + seconds; }
	return hours + ':' + minutes + ':' + seconds;
}

// --------------------------------------------------- play functions
// --------------------------------------------------- play functions
// --------------------------------------------------- play functions

var music = document.getElementById('music');
var playButton = document.getElementById('play-button');
var playhead = document.getElementById('playhead');
var timeline = document.getElementById('timeline');
var timelineWidth = timeline.offsetWidth - playhead.offsetWidth;
var onplayhead = false;
var duration;

// timeupdate event listener
music.addEventListener("timeupdate", timeUpdate, false);

//Makes timeline clickable
timeline.addEventListener("click", function (event) {
	moveplayhead(event);
	var percent = clickPercent(event);
	if (music.duration && clickPercent) {
		var currentTime = duration * percent;
		music.currentTime = currentTime;
	}
}, false);

// returns click as decimal (.77) of the total timelineWidth
function clickPercent(e) {
  return (e.pageX - timeline.offsetLeft) / timelineWidth;
}

// Makes playhead draggable
playhead.addEventListener('mousedown', mouseDown, false);
window.addEventListener('mouseup', mouseUp, false);

// mouseDown EventListener
function mouseDown() {
	onplayhead = true;
	window.addEventListener('mousemove', moveplayhead, true);
	music.removeEventListener('timeupdate', timeUpdate, false);
}

// mouseUp EventListener
// getting input from all mouse clicks
function mouseUp(e) {
	if (onplayhead == true) {
		window.removeEventListener('mousemove', moveplayhead, true);
		// change current time
		var percent = clickPercent(event);
		if (duration && percent) {
			music.currentTime = duration * percent;
		}
		music.addEventListener('timeupdate', timeUpdate, false);
	}
	onplayhead = false;
}

// mousemove EventListener
// Moves playhead as user drags
function moveplayhead(e) {
	var margin = e.pageX - timeline.offsetLeft;

	if (margin >= 0 && margin <= timelineWidth)
		playhead.style.marginLeft = margin + "px";

	if (margin < 0)
		playhead.style.marginLeft = "0px";

	if (margin > timelineWidth)
		playhead.style.marginLeft = timelineWidth + "px";
}

// timeUpdate
// Synchronizes playhead position with current point in audio
function timeUpdate() {
	var playPercent = timelineWidth * (music.currentTime / music.duration);
	playhead.style.marginLeft = playPercent + "px";
	if (music.currentTime == duration) {
		playButton.className = "play";
	}
}
//Play and Pause
function play() {
	if (music.paused) {
		music.play();
		playButton.className = "pause";
	} else { 
		music.pause();
		playButton.className = "play";
	}
}
// Gets audio file duration
music.addEventListener("canplaythrough", function () {
  duration = music.duration;
}, false)

// update current time of track
music.ontimeupdate = function() {
	setNowPlayingTime();
}

function setNowPlayingTime() {
	var current = Math.floor(music.currentTime).toString();
	var total = Math.floor(music.duration).toString();
	document.getElementById('tracktime').innerHTML = current.toTime() + ' / ' + total.toTime();
}
  

// --------------------------- Subscribe Functions
// --------------------------- Subscribe Functions
// --------------------------- Subscribe Functions

function APICALL(url, method, data, headers) {
    return new Promise((success, failure) => {
        $.ajax({
            url: url,
            method: method,
            data: data,
            processData: false,
            contentType: false,
            headers: headers
			})
			.done(res => {
				if (res)
					success(res)
				else
					success(`Unable to parse response: ${url}`)
			})
			.fail(err => {
				failure(err);
			})
	})
}

function subscribe(e) {
	e.preventDefault();
	var formData = new FormData();
	var email = $('#subscriber-email').val();
	formData.append('email', email);

	e.target.innerHTML = `Thanks! An email was sent to ${email}`;
  
	APICALL(`api/subscribe/`, `POST`, formData)
		.then(data => {
			console.log(data)
		})
		.catch(err => {
			console.log(err)
		})
}

var subscriptionForm = document.getElementById('subscription-form');

subscriptionForm.addEventListener('submit', function(event) {
	subscribe(event)
})

// -------------------------------------------
// ---------------------------- Live Functions
// -------------------------------------------

var checkForLiveInterval = 10000;
var checkInterval;

function checkForLiveStream() {
	checkInterval = setInterval(() => {
		getLiveStreamData()
		.then(live => {
			if (live) {
				goLive();
			} else {
				notLive();
			}
		});
	}, checkForLiveInterval)
}

function goLive() {
	setStatus(true);
	resetCheckForLive(true);
}

function notLive() {
	setStatus(false);
	resetCheckForLive(false);
}

function resetCheckForLive(live) {
	clearInterval(checkInterval);
	checkForLiveInterval = live ? 60000 : 10000;
	checkForLiveStream();
}

function setStatus(live) {
	var status = document.getElementById('status');
	if (live) {
		status.innerHTML = "<a href='http://live.introtorhythm.com:8000/stream' target='_blank'>Now Live!</a>";
	} else {
		status.innerHTML = "Offline";
	}
}

function getLiveStreamData() {
	return new Promise((success, fail) => {
		$.ajax({
			url: 'http://live.introtorhythm.com:8000/status-json.xsl'
		}).done(data => {
			if (data.icestats && data.icestats.source) {
				success(true)
			} else {
				success(false)
			}
		})
	})
}

checkForLiveStream();
