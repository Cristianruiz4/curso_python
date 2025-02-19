class Sport:
    ''' Clase para representar un depote
    '''
    def __init__(self, name:str, players:int, league:str):
        self.name = name
        if type(players) != int:
            self.players = int(players)
        else:
            self.players = players
        self.league = league
    
    def  __str__(self)->str:
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)->str:
        """ Representacion en string de Sport """
        return f"Sport('{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        """ Convertir Spor a JSON """
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
    nfl = Sport("Football", 11, "NFL")
    print(nfl)
    print(repr(nfl))
    print(nfl.to_json())
    lmp = Sport("Baseball", "9", "LMP")
    print(lmp)
    print(repr(lmp))
    print(lmp.to_json())

    
        
