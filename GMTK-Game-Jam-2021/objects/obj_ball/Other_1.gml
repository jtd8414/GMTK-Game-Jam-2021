if(bbox_left < 0 or bbox_right >  room_width){
	hspeed = hspeed * -1;
}

if (bbox_top < 0) {
	vspeed *= -1;
}

if (bbox_bottom > room_height) {
	// subtract a life
}