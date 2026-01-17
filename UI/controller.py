import flet as ft
from UI.view import View
from database.dao import DAO
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
    def get_year(self):
        return self._model.get_year()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._view.pulsante_dettagli.disabled =False
        self._view.pulsante_percorso.disabled=False

        self._model.build_graph(int(self._view.dd_anno.value))
        print(self._model.g)
        self._view.update()


    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        team=self._view.dd_squadra.value
        if team:
            lista=self._model.get_dettagli(team)
            self._view.txt_risultato.controls.clear()
            for team in lista:
                self._view.txt_risultato.controls.append(ft.Text(f'{team[0]} : {team[1]}'))
            self._view.update()
        else:
            self._view.show_alert('inserire una squadra')
            return
        pass

    def mostra_team(self,e):
        anno=int(self._view.dd_anno.value)
        lista_team=self._model.get_team(anno)
        self._view.dd_squadra.options.clear()
        self._view.txt_out_squadre.controls.clear()


        for team in lista_team:
            self._view.txt_out_squadre.controls.append(ft.Text(f'{team}'))

            self._view.dd_squadra.options.append(ft.dropdown.Option(key=team.id,text=team))
        self._view.page.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO
        team = self._view.dd_squadra.value
        if team:
            peso,lista = self._model.get_percorso_massimo(team)
        else:
            return self._view.show_alert('inserire una squadra')
        self._view.txt_risultato.controls.clear()
        id=True
        for team in lista:
            if id==True:
                self._view.txt_risultato.controls.append(ft.Text(f''))
                print(team.id,team)
                id=team.id
                print(self._model.dizionario_team[id])
                print(11111111)
            else:
                self._view.txt_risultato.controls.append(ft.Text(f'{self._model.dizionario_team[id]} ----{self._model.g[team][self._model.dizionario_team[id]]["weight"]}--->{team}'))
                id=team.id
        self._view.update()





    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO