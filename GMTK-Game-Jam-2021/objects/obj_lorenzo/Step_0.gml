if (keyboard_check(ord("A")))
{ 
	sprite_index = spr_lorenzo_l;
}
if (keyboard_check(ord("D"))) 
{ 
	sprite_index = spr_lorenzo_r;
}
if (!keyboard_check(ord("A"))) && (!keyboard_check(ord("D"))) 
{
	sprite_index = spr_lorenzo; 
}

if (global.oof) 
{
	sprite_index = spr_lorenzo_oof; 
}