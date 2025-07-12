class Gamer:
    def __init__(self,username: str,level: int):
        assert level >= 1, "Level must be at least 1"
        self.username=username
        self.level=level

    def level_up(self)->None :
        self.level+=1
    
    def get_info(self) -> str:
        return f"Player: {self.username} | Level: {self.level}"
    
    def play_game(self, game: 'Game' ) -> str:
        return game.join_game(self)
    
class Game:
    def __init__(self,name,min_level):
        assert min_level >= 1, "Minimum level must be at least 1"
        self.name=name
        self.min_level=min_level
        self.players=[]
    
    def join_game(self, gamer: Gamer) -> str:
        assert isinstance(gamer, Gamer), "Input must be a Gamer object"
        if gamer.level>=self.min_level:
            self.players.append(gamer)
            return f"{gamer.username} joined {self.name}"
        else:
            return f"{gamer.username} is not high enough level to join {self.name}"


    def show_players(self) -> None:
        print(f'Players in {self.name}:')
        for player in self.players:
            print(player.get_info())

# Step 1: Create Gamers
gamer1 = Gamer("Aryan", 2)
gamer2 = Gamer("Teena", 1)
gamer3 = Gamer("Ravi", 5)

# Step 2: Create Games
game1 = Game("BattleZone", 2)
game2 = Game("DragonQuest", 4)

# Step 3: Join Attempt
print("Players are joining the games:")
print(game1.join_game(gamer1))
print(game1.join_game(gamer2))
print(game1.join_game(gamer3))
print()
print(game2.join_game(gamer1))
print(game2.join_game(gamer2))
print(game2.join_game(gamer3))
print()

# Step 4: Level Up and Retry
print("After leveling up some players:")
gamer2.level_up()  # Teena's level becomes 2
print(game1.join_game(gamer2))  # Should now join BattleZone
print()

# Step 5: Show Final Players
print("Final List:")
game1.show_players()
print()
game2.show_players()