# Assignment 1: Design Your Own Class! 🏗️
# Activity 2: Polymorphism Challenge! 🎭

print("=" * 50)
print("ASSIGNMENT 1: SUPERHERO CLASS DESIGN")
print("=" * 50)

# Base class: Superhero
class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, energy_level=100):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.energy_level = energy_level
        self.is_transformed = False
    
    def use_power(self, power_name):
        if power_name in self.powers:
            if self.energy_level >= 20:
                self.energy_level -= 20
                print(f"⚡ {self.name} uses {power_name}! Energy level: {self.energy_level}")
                return True
            else:
                print(f"😴 {self.name} is too tired to use {power_name}!")
                return False
        else:
            print(f"❌ {self.name} doesn't have the power: {power_name}")
            return False
    
    def rest(self):
        self.energy_level = min(100, self.energy_level + 30)
        print(f"💤 {self.name} rests. Energy level: {self.energy_level}")
    
    def transform(self):
        self.is_transformed = not self.is_transformed
        status = "transforms into superhero mode!" if self.is_transformed else "returns to normal form."
        print(f"🌟 {self.name} {status}")
    
    def display_info(self):
        print(f"\n🦸 Superhero: {self.name}")
        print(f"👤 Secret Identity: {self.secret_identity}")
        print(f"⚡ Powers: {', '.join(self.powers)}")
        print(f"💔 Weakness: {self.weakness}")
        print(f"🔋 Energy Level: {self.energy_level}%")
        print(f"🌟 Mode: {'Superhero' if self.is_transformed else 'Normal'}")

# Inheritance layer - Specialized superhero types
class FlyingSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, flight_speed, energy_level=100):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.flight_speed = flight_speed  # mph
        self.is_flying = False
    
    def fly(self):
        if self.energy_level >= 15:
            self.is_flying = not self.is_flying
            self.energy_level -= 15
            action = "takes off flying" if self.is_flying else "lands safely"
            print(f"✈️ {self.name} {action} at {self.flight_speed} mph! Energy: {self.energy_level}")
        else:
            print(f"😴 {self.name} is too tired to fly!")
    
    def move(self):
        if self.is_flying:
            print(f"🦅 {self.name} soars through the sky gracefully!")
        else:
            print(f"🚶 {self.name} walks on the ground.")

class TechSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, gadgets, energy_level=100):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.gadgets = gadgets  # List of gadgets
        self.active_gadget = None
    
    def use_gadget(self, gadget_name):
        if gadget_name in self.gadgets:
            if self.energy_level >= 10:
                self.energy_level -= 10
                self.active_gadget = gadget_name
                print(f"🔧 {self.name} uses {gadget_name}! Energy: {self.energy_level}")
                return True
            else:
                print(f"😴 {self.name} is too tired to use gadgets!")
                return False
        else:
            print(f"❌ {self.name} doesn't have the gadget: {gadget_name}")
            return False
    
    def move(self):
        if self.active_gadget == "Jet Boots":
            print(f"🚀 {self.name} zooms through the air with jet boots!")
        elif self.active_gadget == "Hover Board":
            print(f"🛹 {self.name} glides smoothly on a hover board!")
        else:
            print(f"🚶 {self.name} walks using advanced exoskeleton.")

class MagicSuperhero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, spell_book, energy_level=100):
        super().__init__(name, secret_identity, powers, weakness, energy_level)
        self.spell_book = spell_book  # Dictionary of spells
        self.active_spell = None
    
    def cast_spell(self, spell_name):
        if spell_name in self.spell_book:
            cost = self.spell_book[spell_name]
            if self.energy_level >= cost:
                self.energy_level -= cost
                self.active_spell = spell_name
                print(f"🔮 {self.name} casts {spell_name}! (-{cost} energy) Energy: {self.energy_level}")
                return True
            else:
                print(f"😴 {self.name} doesn't have enough energy for {spell_name}!")
                return False
        else:
            print(f"❌ {self.name} doesn't know the spell: {spell_name}")
            return False
    
    def move(self):
        if self.active_spell == "Teleportation":
            print(f"🌀 {self.name} instantly teleports to a new location!")
        elif self.active_spell == "Levitation":
            print(f"✨ {self.name} floats magically in the air!")
        else:
            print(f"🚶 {self.name} walks normally.")

print("\n" + "=" * 50)
print("ACTIVITY 2: POLYMORPHISM CHALLENGE - MOVE() METHOD")
print("=" * 50)

# Create instances of different superhero types
sky_guardian = FlyingSuperhero(
    "Sky Guardian", 
    "Alex Johnson", 
    ["Flight", "Super Strength", "Energy Blasts"], 
    "Kryptonite", 
    500
)

tech_hero = TechSuperhero(
    "Tech Hero", 
    "Sarah Chen", 
    ["Hacking", "Invention", "Combat Skills"], 
    "EMP Attacks", 
    ["Laser Gloves", "Jet Boots", "Hover Board", "Shield Generator"]
)

mage_warrior = MagicSuperhero(
    "Mage Warrior", 
    "David Martinez", 
    ["Spell Casting", "Element Control", "Healing"], 
    "Iron", 
    {"Fireball": 25, "Teleportation": 30, "Levitation": 15, "Shield": 20}
)

# Demonstrate polymorphism - same method name, different behavior
superheroes = [sky_guardian, tech_hero, mage_warrior]

print("\n🚀 DEMONSTRATING POLYMORPHISM:")
print("-" * 40)

for hero in superheroes:
    hero.transform()  # Activate superhero mode
    hero.move()  # Each hero moves differently!

print("\n" + "=" * 50)
print("INTERACTIVE DEMONSTRATION")
print("=" * 50)

# Interactive demonstration
def demonstrate_superhero(hero):
    print(f"\n🌟 DEMONSTRATING {hero.name.upper()}:")
    hero.display_info()
    
    # Special abilities based on hero type
    if isinstance(hero, FlyingSuperhero):
        hero.fly()
        hero.move()
    elif isinstance(hero, TechSuperhero):
        hero.use_gadget("Jet Boots")
        hero.move()
    elif isinstance(hero, MagicSuperhero):
        hero.cast_spell("Teleportation")
        hero.move()
    
    # Common superhero action
    hero.use_power(hero.powers[0] if hero.powers else "Unknown Power")
    hero.rest()

# Demonstrate each superhero
demonstrate_superhero(sky_guardian)
demonstrate_superhero(tech_hero)
demonstrate_superhero(mage_warrior)

print("\n" + "=" * 50)
print("POLYMORPHISM IN ACTION - MOVE() COMPARISON")
print("=" * 50)

# Clear previous states and show pure move() behavior
sky_guardian.is_flying = False
tech_hero.active_gadget = None
mage_warrior.active_spell = None

print("\n🧪 Testing move() method with default states:")
for hero in superheroes:
    print(f"{hero.name}: ", end="")
    hero.move()

print("\n🧪 Testing move() method with activated abilities:")
sky_guardian.fly()
tech_hero.use_gadget("Hover Board")
mage_warrior.cast_spell("Levitation")

for hero in superheroes:
    print(f"{hero.name}: ", end="")
    hero.move()

print("\n🎉 Assignment completed successfully!")
