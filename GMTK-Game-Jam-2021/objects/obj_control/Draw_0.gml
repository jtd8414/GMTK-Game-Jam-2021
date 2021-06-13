draw_text(8, 8, "Score: " + string(global.player_score));
draw_set_halign(fa_right)
draw_text(room_width-8, 8, "High Score: " + string(global.high_score));
draw_set_halign(fa_left)

_x = (room_width/2) - (global.player_lives-1) * 32;
repeat(global.player_lives) {
	draw_sprite_ext(
		spr_heart,
		0, 
		_x - 50, 
		room_height - 64,
		0.30,
		0.30,
		0, 
		c_white,
		0.5
	);
	_x += 128
}