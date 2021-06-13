if (keyboard_check(ord("A")))
{ 
	sprite_index = spr_paddle_l;
}
if (keyboard_check(ord("D"))) 
{ 
	sprite_index = spr_paddle_r;
}
if (!keyboard_check(ord("A"))) && (!keyboard_check(ord("D"))) 
{
	sprite_index = spr_paddle; 
}