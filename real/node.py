class Node:
    def __init__(self, w, v):
        self.weight = w
        self.visit = v
    
    def __repr__(self):
        return "{ w: %s, v: %s }" % (self.weight, self.visit)

    def __str__(self):
        return "{ w: %s, v: %s }" % (self.weight, self.visit)
