from ursina import *
import random 

random_generator = random.Random()
texoffset = 0.0
texoffset2 = 0.0

 
#Update function
def update():

	#rotate the cubes in cube list along their y axis
	for entity in cubes:
		entity.rotation_y += time.dt * 50

	#rotates the sky
	sky.rotation_y += time.dt * 10

	#rotates the marble
	marble.rotation_y -= time.dt * 30

	if mouse.hovered_entity == marble:
		info.visible = True
	else:
		info.visible = False

	#moves the camera up at 'w' press, and down at 's' press
	#moves the camera left at 'a' press, and right at 'd' press
	if held_keys['w']:
		camera.position += (0, time.dt * 2, 0)
	if held_keys['s']:
		camera.position -= (0, time.dt * 2, 0)
	if held_keys['a']:
		camera.position	-= (time.dt * 2, 0, 0)
	if held_keys['d']:
		camera.position += (time.dt * 2, 0, 0)
	if held_keys['q']:
		camera.position -= (0,0,time.dt * 2)
	if held_keys['e']:
		camera.position += (0,0,time.dt * 2)

	if mouse.left == True:
		info.visible = True
	else:
		info.visible = False

	#water movement
	global texoffset
	global texoffset2
	texoffset += time.dt * 0.2
	setattr(waterfall, "texture_offset", (0, texoffset))
	texoffset2 += time.dt * 0.3
	setattr(waterfall2, "texture_offset", (0, texoffset2))


def input(key):
	# sets cubes to random color upon 'c' press
	if key == 'c':
		red = random_generator.random() * 255
		green = random_generator.random() * 255
		blue = random_generator.random() * 255

		for cube in cubes:
			cube.color = color.rgb(red, green, blue)


	if key == 'space':

		#sets random values in specific range for position
		x = random_generator.random() * 10 - 5
		y = random_generator.random() * 10 - 5
		z = random_generator.random() * 10 - 5
		s = random_generator.random() * 1
		
		#sets red, green, and blue to a random color value
		red = random_generator.random() * 255
		green = random_generator.random() * 255
		blue = random_generator.random() * 255

		#create new cube and appends it to cube list
		newcube = Entity(parent='cube', model='cube', color=color.rgb(red, green, blue), position=(x, y, z,), scale = (s, s,s), texture="crate")
		cubes.append(newcube)

app = Ursina()

#setting the window attributes
window.title = 'My Game'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = True

#creating cube list
cubes = []

#initiating cube entity
cube = Entity(model='cube', color=color.white, scale=(2,2,2), texture="crate", position=(-3,0,-5))

#initiating sky_dome entity
sky = Entity(model='sky_dome', color=color.white, scale=(15,15,15), texture="sky")

# initiates a sphere entity
marble = Entity(model='sphere', color=color.white, scale=(3,3,3), texture="marble", position=(5,0,5))

#initates another cube for the waterfall
waterfall = Entity(model='cube', color=color.white, scale=(2,10,2), texture="water", position=(0,0,0))
waterfall2 = Entity(model='cube', color=color.rgba(255,255,255,150), scale=(2.15,10,2.15), texture="water", position=(0,0,0))


#adds default cube to the list of cubes
cubes.append(cube)

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="Fuck you")
info.x = -0.105
info.y = 0 
info.background = True
info.visible = False


app.run()