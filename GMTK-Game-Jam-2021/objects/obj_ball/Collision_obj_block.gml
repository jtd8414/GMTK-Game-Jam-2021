move_bounce_all(true);

global.player_score += 15;
speed += 0.5
instance_destroy(other); 

var inst = instance_nearest(other.x, other.y, obj_block);
instance_create_depth(inst.x, inst.y, -10000,  obj_block2);
instance_destroy(inst);

var inst = instance_nearest(other.x, other.y, obj_block);
instance_create_depth(inst.x, inst.y, -10000,  obj_block2);
instance_destroy(inst);

