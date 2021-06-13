move_bounce_all(true);

global.player_score += 15;
speed += 0.5
instance_destroy(other); 

if (instance_exists(obj_block3)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block3);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block4);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}

if (instance_exists(obj_block3)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block3);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block4);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}

