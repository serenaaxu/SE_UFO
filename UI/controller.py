import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def populate_dd(self):
        """ Metodo per popolare i dropdown """

        years = self._model.get_years()
        self._view.dd_year.options = [ft.dropdown.Option(y) for y in years]

        shapes = self._model.get_shapes()
        self._view.dd_shape.options = [ft.dropdown.Option(s) for s in shapes]

        self._view.update()

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """
        year = self._view.dd_year.value
        shape = self._view.dd_shape.value

        # controllo input
        if not year or not shape:
            self._view.show_alert("Selezionare Anno e Forma!")
            return

        # 1. Costruisco il grafo tramite il modello
        self._model.build_graph(year, shape)

        # 2. Recupero i dettagli (Nodi e Archi)
        n_nodes, n_edges = self._model.get_graph_details()

        # 3. Output base
        self._view.lista_visualizzazione_1.controls.clear()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici: {n_nodes}"
                                                      f" Numero archi : {n_edges}"))
        # 4. Recupero e stampo la somma dei pesi adiacenti
        # -> lista di tuple
        node_data = self._model.get_node_weights_sum()

        for state_id, w_sum in node_data:
            self._view.lista_visualizzazione_1.controls.append(
                ft.Text(f"Nodo {state_id}: somma pesi su achi {w_sum}")
            )

        self._view.update()



    def handle_path(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """
        # chiamo la funzione ricorsiva del modello
        # restituisce il percorso (lista di nodi) e la distanza totale
        # path, max_dist = self._model.get
        return None
