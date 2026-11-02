from database.pippo import Pippo


class Model:
    def __init__(self):
        pass

    # Funzione che è incaricata di fornire le trip
    def get_trips(self):
        print("Getting trips ...")
        pippo = Pippo()
