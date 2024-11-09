import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.shielded = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5) # random damage hit
        if opponent.shielded:
            print(f"{opponent.name} blocked the attack!!")
            opponent.shielded = False
        else:
            opponent.health -= self.attack_power
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # added heal function that checks if health is max before adding hp and displaying new hp
    def heal(self):
        heal_amount = 30
        if self.health < self.max_health:
            self.health += heal_amount
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} healed by {heal_amount}hp! Health is now {self.health}/{self.max_health}")
        else:
            print(f"{self.name} is already at max health!")


# Warrior class (inherits from Character) and its 2 special abilities
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def power_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} Power Strikes {opponent.name} with {damage} damage!")
    
    def spartan_rage(self):
        self.attack_power += 20
        print(f"{self.name} used Spartan Rage! Attack power increased to {self.attack_power} until end of this turn")


# Mage class (inherits from Character) and its 2 special abilities
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def arcane_spell(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} casts an Arcane Spell on {opponent.name}! {damage} damage!")
        
    def force_field(self):
        self.shielded = True
        print(f"{self.name} casted Force Field and blocks next attack!")    

# Added Archer class (inherits from Character) and its 2 special abilities
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
    
    def quick_shot(self, opponent): # double arrow attack
        arrow1 = random.randint(self.attack_power - 5, self.attack_power + 5)
        arrow2 = random.randint(self.attack_power - 5, self.attack_power + 5)
        damage = arrow1 + arrow2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot at {opponent.name}! {damage} damage!")
    
    def evade(self):
        self.shielded = True
        print(f"{self.name} uses Evade and blocks the next attack!")

# Added Paladin class (inherits from Character) and its champion chop move
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=50)

    def holy_strike(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} uses the Holy Strike on {opponent.name}! {damage} damage!")
    
    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} uses Divine Shield and blocks the next attack!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}/{self.max_health}")

    

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2") # added 2 options for special ability
        print("4. Heal")
        print("5. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2': # calling the corresponding first special ability
            if isinstance(player, Warrior):
                player.power_strike(wizard)
            elif isinstance(player, Mage):
                player.arcane_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3': # calling the corresponding second special ability
            if isinstance(player, Warrior):
                player.spartan_rage()
            elif isinstance(player, Mage):
                player.force_field()
            elif isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated by {wizard.name}!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    try:
        # Character creation phase
        player = create_character()

        # Evil Wizard is created
        wizard = EvilWizard("The Dark Wizard")

        # Start the battle
        battle(player, wizard)
    except Exception as e:
        print(f"Error Message: {e}. Please try again.")

if __name__ == "__main__":
    main()