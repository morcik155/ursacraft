from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()
andesite = 'stone'
ls1 = [andesite, andesite, andesite, andesite, '1', '1', '3', 'drn']
lands = {
    1: 'берёзовый лес',
    2: 'тёмный лес',
    3: 'дубовый лес',
    4: 'равнина',
    5: 'горы'
}


def do_ls():
    global andesite
    ls = [[[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)],
           [andesite, random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1), andesite,
            random.choice(ls1), random.choice(ls1), random.choice(ls1), random.choice(ls1)]
           ],
          [[andesite] * 10] * 10,
          [['grass_all'] * 10] * 10]
    return ls


asas = 5
aaa = '12121'
obg = []
ls = do_ls()
for i in range(len(ls)):
    for j in range(len(ls[i])):
        random.shuffle(ls[i][j])
punch_sound = Audio('assets/stone3', loop=False, autoplay=False)
Light(tupe='ambient', color=(0.5, 0.5, 0.5, 1))
Light(tupe='directional', color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1))
player = FirstPersonController(y=10)
b = 1
cnt = 0
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
window.fps_counter.enabled = False
window.exit_button.visible = False

def update():
    global b, cnt, asas
    for q in obg:
        q.rotation_y += time.dt + 50
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

class Voxel(Button):
    def __init__(self, position2=(0, 0, 0), texture2=aaa, model2='cube', scale=1.0):
        super().__init__(
            parent=scene,
            position=position2,
            model=model2,
            origin_y=0.5,
            texture=texture2,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=scale
        )

    # ставим удаляем и меняем блоки
    def input(self, key):
        global aaa
        if self.hovered:
            if key == 'right mouse down':
                punch_sound.play()
                if ls[y][x - (10 * i)][z] == 'grass_all' or ls[y][x - (10 * i)][z] == 'drn':
                    voxel = Voxel(position2=self.position + mouse.normal, texture2=aaa, model2='block', scale=0.5)
                else:
                    voxel = Voxel(position2=self.position + mouse.normal, texture2=aaa)
            if key == 'left mouse down':
                punch_sound.play()
                destroy(self)
            if key == '1':
                aaa = 'grass_all'
            if key == '2':
                aaa = 'drn'
            if key == '3':
                aaa = andesite
            elif key == '4':
                aaa = '12121'
            if key == 'q':
                obg.append(Entity(model='cube', texture=aaa,
                                  rotation=(0, 0, 0),
                                  position=(self.position[0], self.position[1] + 0.5, self.position[2]), scale=0.2))
            for s in range(len(obg)):
                if int(player.position[0]) == int(obg[s].position[0]) and int(player.position[1]) == int(
                        obg[s].position[1]) and int(player.position[2]) == int(obg[s].position[2]):
                    destroy(obg[s])
                    del obg[s]


# небо
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)


# рука
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


# создаём платформу
for z in range(10):
    for x in range(10):
        for y in range(10):
            if ls[y][x][z] == 'grass_all' or ls[y][x][z] == 'drn':
                voxel = Voxel(position2=(x, float(y) - 0.25, z), texture2=ls[y][x][z], model2='block', scale=0.5)
            else:
                voxel = Voxel(position2=(x, y, z), texture2=ls[y][x][z])


for i in range(1, 2):
    ls = do_ls()
    for z in range(10):
        for x in range(10, 10 + (10 * i)):
            for y in range(10):
                if ls[y][x - (10 * i)][z] == 'grass_all' or ls[y][x - (10 * i)][z] == 'drn':
                    voxel = Voxel(position2=(x, float(y) - 0.25, z), texture2=ls[y][x - (10 * i)][z], model2='block', scale=0.5)
                else:
                    voxel = Voxel(position2=(x, y, z), texture2=ls[y][x - (10 * i)][z])

sky = Sky()
hand = Hand()

app.run()



