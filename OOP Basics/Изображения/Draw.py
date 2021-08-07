from PIL import Image, ImageDraw, ImageColor
import os.path

HOME = 'C:\\Temp'
TEXT = 'Hello,\nWorld!'
OFFSET = 15
path_in = HOME + '\\' + 'test.png'
path_out = HOME + '\\' + 'res.png'

im = Image.open(path_in)
draw = ImageDraw.Draw(im)
sz = im.size
center = [sz[0]/2, sz[1]/2]
draw.line([center[0], 0, center[0], sz[1]], fill = (255, 128, 255))
t_width = draw.multiline_textsize(TEXT)
draw.multiline_text((center[0]-t_width[0]/2, center[1] - t_width[1]/2), 'Hello\nWorld!', align='center')
max_dim = max(t_width[0], t_width[1])
r_width = max_dim + OFFSET
top_left_x = (sz[0] - r_width)/2
top_left_y = (sz[1] - r_width)/2
bottom_right_x = (sz[0] + r_width)/2
bottom_right_y = (sz[1] + r_width)/2
draw.rectangle([top_left_x, top_left_y, bottom_right_x, bottom_right_y], fill = None, outline = (255, 255, 255))
if os.path.isdir(path_out):
    os.path.remove(path_out)
im.save(path_out)
del draw
im.show()