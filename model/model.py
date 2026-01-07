import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {} # ??

    def get_years(self):
        return DAO.get_all_years()

    def get_shapes(self):
        return DAO.get_all_shapes()

    def build_graph(self, year, shape):
        self._graph.clear()

        # 1. Aggiungo i Nodi (tutti gli stati)
        self._nodes = DAO.get_all_states()
        self._graph.add_nodes_from(self._nodes)

        # creare una mappa per accesso veloce: "TX" -> Oggetto State(TX, Texas,...)
        self._idMap = {s.id: s for s in self._nodes} # ???

        # 2. Recupero gli Archi (chu confina con chi)
        edges = DAO.get_all_neighbors()

        # 3. Recupero i conteggi (pesi)
        # count_map sarà : {'CA': 100, 'NV': 20, ...}
        count_map = DAO.get_sightings_count(year, shape)

        for s1_id, s2_id in edges: # ??
            if s1_id in self._idMap and s2_id in self._idMap:
                u = self._idMap[s1_id]
                v = self._idMap[s2_id]

                # Calcolo del peso: somma degli avvistamenti nei due stati
                # .get(id, 0) restituisce 0 se non ci sono avvistamenti in quello stato
                weight = count_map.get(u.id, 0) + count_map.get(v.id, 0)

                # aggiungo l'arco pesato
                self._graph.add_edge(u, v, weight=weight)

    def get_graph_details(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_node_weights_sum(self):
        """ per ogni stato calcola la somma dei pesi degli archi adiacenti"""

        results = []
        for node in self._graph.nodes:
            sum_weights = 0

            # scorro tutti i vicini del nodo
            for neighbor in self._graph.neighbors(node):
                # prendo il peso dell'arco tra nodo e vicino
                sum_weights += self._graph[node][neighbor]['weight']

            results.append((node.id, sum_weights))
        return results





