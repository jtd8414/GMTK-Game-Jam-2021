draw_set_font(fnt_game);
gameover = false;
  
var i = 0;
var ii = 0;
var _rows = 14;
var _columns = 7;
var _width = 85;
var _height = 50;
var _spacing = 0;
var _xoffset = 640 + 85;
var _yoffset = (room_height / 2) - 575;
var _depth = -10000;
var _object = obj_block;

for(i = 0; i < _rows; i++)
{
	for(ii = 0; ii < _columns ; ii++)
	{
		var _cur_grid_x = _xoffset + (i * (_width + _spacing));
		var _cur_grid_y = _yoffset + (ii * (_height + _spacing));
		var inst = instance_create_depth(_cur_grid_x,_cur_grid_y,_depth,_object);
		inst.image_xscale = 0.025;		
		inst.image_yscale = 0.025;
		global.block_list[i][ii] = inst;
		inst.row = i;
		inst.column = ii;
	}
}
     