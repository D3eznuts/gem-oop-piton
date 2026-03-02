class Character:
    def __init__(self, name,hitPoint,energy,attack,defense,bruteCh,bruteDmg):
        self.name = name
        self.hitPoint = hitPoint
        self.energy = energy
        self.attack = attack
        self.defense = defense
        self.bruteCh = bruteCh
        self.bruteDmg = bruteDmg

    def info(self):
     print(f"Character: {self.name}, HP: {self.hitPoint}, Energy: {self.energy}, Attack: {self.attack}, Defense: {self.defense}, Brute Chance: {self.bruteCh}, Brute Multiplier: {self.bruteDmg}x")
    def is_alive(self):
        return self.hitPoint > 0
    def take_damage(self, damage):
        self.hitPoint -= damage
        if self.hitPoint < 0:
            self.hitPoint = 0
    def heal(self, amount):
        self.hitPoint += amount
    def use_energy(self, amount):
        if self.energy >= amount:
            self.energy -= amount
            return True
        return False
    def restore_energy(self, amount):
        self.energy += amount
    def attack_target(self, target):
        import random
        if not self.is_alive():
            return 0, 0, 0
        base_damage = self.attack - target.defense
        if base_damage < 0:
            base_damage = 0
        brute_damage = 0
        total_damage = base_damage
        if random.random() < self.bruteCh:
            brute_damage = base_damage * self.bruteDmg
            total_damage = base_damage + brute_damage
        target.take_damage(total_damage)
        print(f"{self.name} menyerang {target.name}!")
        print(f"  - Pure Damage: {base_damage}")
        if brute_damage > 0:
            print(f"  - Brute Damage: {brute_damage} ({self.bruteDmg}x multiplier)")
        print(f"  - Total Damage: {total_damage}")
        return base_damage, brute_damage, total_damage
    def __str__(self):
        return f"{self.name}: HP={self.hitPoint}, Energy={self.energy}, Attack={self.attack}, Defense={self.defense}, BruteChance={self.bruteCh}, BruteDamage={self.bruteDmg}"
class Frontliner(Character):
    def __init__(self, name):
        super().__init__(name, hitPoint=2000, energy=750, attack=100, defense=50, bruteCh=0.5, bruteDmg=2.5)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hitPoint=1100, energy=1000, attack=150, defense=30, bruteCh=0.3, bruteDmg=3.0)

class Marksman(Character):
    def __init__(self, name):
        super().__init__(name, hitPoint=1000, energy=800, attack=120, defense=40, bruteCh=0.4, bruteDmg=2.0)

class Assassin(Character):
    def __init__(self, name):
        super().__init__(name, hitPoint=1200, energy=900, attack=180, defense=20, bruteCh=0.6, bruteDmg=4.0)

class Support(Character):
    def __init__(self, name):
        super().__init__(name, hitPoint=1300, energy=1100, attack=80, defense=60, bruteCh=0.2, bruteDmg=1.5)

def skill_fireball(self, lawan): 
        if self.mana >= 20: 
            print(f"{self.name} using fireball to {lawan.name}!") 
            self.mana -= 20 
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat 
        else: 
            print(f"{self.name} skill failed! Not Enough Mana.")