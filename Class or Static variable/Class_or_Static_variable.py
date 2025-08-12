class Player:
  team_run = 0   # This is a class variable: total runs scored by the whole team

  def __init__(self, run):
     self.run = run   # This is each player's own runs (instance variable)

  def hit_four(self):
    self.run += 4           # Add 4 runs to this player’s score
    Player.team_run += 4    # Add 4 runs to the team's total runs

  def hit_six(self):
    self.run += 6           # Add 6 runs to this player’s score
    Player.team_run += 6    # Add 6 runs to the team's total runs

# Create player objects with 0 runs at start
sakib = Player(0)
tamim = Player(0)

# tamim hits two fours
tamim.hit_four()  # tamim's runs become 4, team runs become 4
tamim.hit_four()  # tamim's runs become 8, team runs become 8

# sakib hits one six and one four
sakib.hit_six()   # sakib's runs become 6, team runs become 14
sakib.hit_four()  # sakib's runs become 10, team runs become 18

# Print each player’s runs
print("sakib:", sakib.run)      # Prints sakib's runs → 10
print("Tamim:", tamim.run)      # Prints tamim's runs → 8

# Mistake here: This prints tamim's runs again, not team runs
print("Team run:", tamim.run)   

# Correct way to print team runs (using class or any player)
print("team run:", sakib.team_run)   
print("Team run:", Player.team_run)  
