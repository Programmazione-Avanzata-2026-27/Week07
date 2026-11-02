import flet as ft

from ui import controller


class View:
    def __init__(self, page):
        self._page = page
        self._controller = None

    def set_controller(self, controller):
        self._controller = controller

    # Metodo che chiamo una volta per inizializzare la UI
    def initialize_ui(self):
        self._page.title = "Citibike"
        self._page.window.width = 600
        self._page.window.height = 400
        #self._page.window.resizable = False

        btn = ft.Button(content="Trips",
                        on_click = self._controller.handler_btn)

        row = ft.Row([btn],
                     alignment = ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row)

        #self.update_ui()


    # Metodo che può essere chiamato anche da fuori dalla
    # classe per aggiornare la UI quando necessario
    def update_ui(self):
        self._page.update()
