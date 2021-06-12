if(instance_number(obj_block) <= 0) {
	room_restart();
}

if(gameover) {
	if(keyboard_check_pressed(vk_anykey))
	{
		room_restart();	
		global.player_score = 0;
		global.player_lives = 3;
	}
}