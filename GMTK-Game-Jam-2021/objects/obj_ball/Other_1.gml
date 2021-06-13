
if (bbox_top < 0) {
	vspeed *= -1;
}

if (bbox_bottom > room_height) {
	global.player_lives -= 1;
	instance_destroy();
	audio_play_sound(snd_destroy, 10, false);
	global.oof = true;
	
	if (global.player_lives <= 0) 
    {
		audio_play_sound(snd_game_over, 10, false);

		obj_control.gameover = true;
		if (global.player_score > global.high_score) 
		{
			global.high_score = global.player_score
		}
	} 
	else 
	{
		instance_create_layer(xstart, ystart, "Instances", obj_ball);
	}
	//vspeed *= -1;
} 