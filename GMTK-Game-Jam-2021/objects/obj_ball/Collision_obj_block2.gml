move_bounce_all(true);

global.player_score += 25;
speed += 0.5
instance_destroy(other); 

if (instance_exists(obj_block2)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block2);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block3);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}

if (instance_exists(obj_block2)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block2);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block3);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}

if (instance_exists(obj_block)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block2);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}

if (instance_exists(obj_block)) 
{
	var nearestInst = instance_nearest(other.x, other.y, obj_block);
	var newBlock = instance_create_depth(nearestInst.x, nearestInst.y, -10000,  obj_block2);
	newBlock.image_xscale = 0.03;		
	newBlock.image_yscale = 0.03;
	instance_destroy(nearestInst);
}







