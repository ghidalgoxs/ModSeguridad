
class Cliente():
    def __init__(self,idPersona,username,password,strUrl = []) -> None:
        self.idPersona = idPersona
        self.username = username
        self.password = password
        self.strUrl = strUrl
    
    def __str__(self) -> str:
        return {
            'idPersona': self.idPersona, 
            'username': self.username, 
            'password': self.password,
            'strUrl': self.get_strUrl()
        }
    
    def add_strUrl(self,strUrl):
        self.strUrl.append(strUrl)
    
    def get_strUrl(self):
        return self.strUrl
        