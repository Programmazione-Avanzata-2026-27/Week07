import flet as ft

from model.model import Model
from ui.controller import Controller
from ui.view import View

def main(page : ft.Page):

    model = Model()

    view = View(page)

    controller = Controller(model, view)
    view.set_controller(controller)

    view.initialize_ui()





#main()

ft.run(main) # se 0.28.3 ft.app(target=main)

