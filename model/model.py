from database.dao import DAO
import networkx as nx
class Model:
    def __init__(self):
        self.g=nx.Graph()
        self.peso_massimo=0
        self.percorso_migliore=0
        self.dao=DAO()
    def get_year(self):
        return self.dao.get_year()
    def get_team(self,year):
        self.lista_team=[]
        self.lista_team=self.dao.search_team(year)
        self.dizionario_team={}
        for i in self.lista_team:
            self.dizionario_team[i.id]=i

        return self.lista_team
    def build_graph(self,anno):
        self.g.clear()
        self.g.add_nodes_from(self.lista_team)
        for team in self.lista_team:

            for team2 in self.lista_team:
                if  self.g.has_edge(team,team2) or team.id == team2.id:
                    pass
                else:
                    self.g.add_edge(team,team2,weight=team2.stipendio+team.stipendio)
        return
    def get_dettagli(self,id):
        nodo=self.dizionario_team[int(id)]

        lista=[]
        for vicino in self.g.neighbors(nodo):
            peso=self.g[vicino][nodo]['weight']
            lista.append([vicino,peso])
        lista.sort(key=lambda x: x[1],reverse=True)
        return lista
    def get_percorso_massimo(self,id):
        nodo=self.dizionario_team[int(id)]
        parziale=[nodo]
        self.peso_massimo=0
        self.percorso_migliore=[]
        print(nodo)
        for vicino in self.g.neighbors(nodo):
            peso=self.g[vicino][nodo]['weight']
            parziale.append(vicino)
            self.ricorsione(parziale,peso,peso)
            parziale.pop()
        print(self.peso_massimo,self.percorso_migliore)
        return self.peso_massimo,self.percorso_migliore

    def ricorsione(self,parziale,peso_totale,peso_ultimo_edge):
        if peso_totale>self.peso_massimo:
            self.peso_massimo=peso_totale
            self.percorso_migliore=parziale.copy()
        ultimo_nodo=parziale[-1]
        for vicino in self.g.neighbors(ultimo_nodo):
            if vicino not in parziale:
                peso_edge=self.g[vicino][ultimo_nodo]['weight']
                if peso_ultimo_edge>peso_edge:
                    parziale.append(vicino)
                    self.ricorsione(parziale,peso_totale+peso_edge,peso_edge)
                    parziale.pop()







