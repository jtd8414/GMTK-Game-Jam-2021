if (bbox_top < 0) {
	vspeed *= -1;
}

if (bbox_bottom > room_height) {
	instance_destroy();
} 