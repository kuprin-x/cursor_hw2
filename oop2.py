class Person:
    def __init__(self):
        arm_l = Arm('Left arm')
        arm_r = Arm('Right arm')
        self.arms = [arm_l, arm_r]


class Arm:
    def __init__(self, whatis):
        self.whatis = whatis


result = Person()

for arm in result.arms:
    print(arm.whatis)

# 2b

class CellPhone:
    def __init__(self, type_glass):
        self.type_glass = type_glass


class Screen:
    def __init__(self, glass):
        self.glass = glass


result2b = Screen('Gorilla Glass')
print(result2b.glass)




