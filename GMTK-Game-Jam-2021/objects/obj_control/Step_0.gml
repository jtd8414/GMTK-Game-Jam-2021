if(instance_number(obj_block) <= 0 && instance_number(obj_block2) <= 0 && instance_number(obj_block3) <= 0 && instance_number(obj_block4) <= 0) {
	if(keyboard_check_pressed(vk_space))
	{
		room_restart();
	}
}

if(gameover) {
	if(keyboard_check_pressed(vk_space))
	{
		global.oof = false;
		room_restart();	
		global.player_score = 0;
		global.player_lives = 3;
	}
}