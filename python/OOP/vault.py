class Vault:
    def __init__(self, galleons=0, sickless=0, knuts=0):
        self.galleons = galleons
        self.sickless = sickless
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons}, Galleons {self.sickless}, sickless {self.knuts} knuts"
    
    def __add__(self, other):
        return Vault(self.galleons + other.galleons, self.sickless + other.sickless, self.knuts + other.knuts)
    
potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

total = potter + weasly
print(total)
