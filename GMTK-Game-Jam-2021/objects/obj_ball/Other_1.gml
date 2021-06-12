if(bbox_left < 0 or bbox_right >  room_width){
	hspeed = hspeed * -1;
}

if (bbox_top < 0) {
	vspeed *= -1;
}

if (bbox_bottom > room_height) {
	global.player_lives -= 1;
	instance_destroy();
	instance_create_layer(xstart, ystart, "Instances", obj_ball);
} 