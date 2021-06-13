if (go == false) {
	direction = random_range(45, 135);
	speed = 12;
	go = true;
	audio_play_sound(snd_fire, 20, false);
	global.oof = false;
}