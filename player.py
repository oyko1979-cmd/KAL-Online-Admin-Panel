

class Player:

    def __init__(
            self,
            uid,
            pid,
            admin,
            name,
            char_class,
            specialty,
            level,
            contribute,
            exp,
            gid,
            grole,
            strength,
            health,
            intelligence,
            wisdom,
            dexterity,
            curhp,
            curmp,
            pupoint,
            supoint,
            killed,
            map,
            x,
            y,
            z
    ):
        self.uid = uid
        self.pid = pid
        self.admin = admin
        self.name = name
        self.char_class = char_class
        self.specialty = specialty
        self.level = level
        self.contribute = contribute
        self.exp = exp
        self.gid = gid
        self.grole = grole
        self.strength = strength
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.curhp = curhp
        self.curmp = curmp
        self.pupoint = pupoint
        self.supoint = supoint
        self.killed = killed
        self.map = map
        self.x = x
        self.y = y
        self.z = z