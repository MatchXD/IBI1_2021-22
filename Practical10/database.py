full_name = input('what is your full name:')
location = input('where are you(International Campus or Edinburgh):')
role = input('what is your role(leadership,faculty,or administration):')


class staff():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = staff(full_name, location, role)
print(p1.x,p1.y,p1.z)