move_bounce_all(true);

global.player_score += 4;
speed = global.maxixmum_ball_speed;
audio_play_sound(snd_squish, 10, false);
instance_destroy(other); 
var inst = instance_create_depth(other.x, other.y, -100000, obj_splat);
inst.image_xscale = 0.05;
inst.image_yscale = 0.05;

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

