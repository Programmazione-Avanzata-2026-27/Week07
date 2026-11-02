

class Controller():
    def __init__(self, model, view):
        self._model = model
        self._view = view

    # Funzione handler del pulsante, riceve un evento e
    def handler_btn(self, e):
        print("Button clicked")
        self._model.get_trips()
