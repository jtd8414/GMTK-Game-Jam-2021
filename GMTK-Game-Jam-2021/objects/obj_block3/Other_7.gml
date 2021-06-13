var rand = irandom_range(1,3);
if (rand == 1 && instance_number(obj_bullet) < global.maximum_bullet_count && place_free(x,y + 50))
{   
	instance_create_layer(x, y + 50, "Instances", obj_bullet);
}