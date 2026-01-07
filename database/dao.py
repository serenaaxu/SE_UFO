from database.DB_connect import DBConnect
from model.state import State


class DAO:
    @staticmethod
    def get_all_years():
        # restituisco tutto gli anni (1910-2014) per il menu
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(s_datetime) as year
                   FROM sighting s"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_shapes():
        # restituisce tutte le forme
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT shape
                   FROM sighting s"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_states():
        # restituisce gli stati, nodi del grafo
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                   FROM state"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row)) ###

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_neighbors():
        # recupera le coppie di stati confinanti, gli archi non pesati
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT state1, state2
                   FROM neighbor"""

        cursor.execute(query)

        for row in cursor:
            result.append((row['state1'], row['state2']))  ###

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_sightings_count(year, shape):
        """
        calcolo del PESO
        Conta quanti avvistamenti ci sono stati in ogni stato
        per quell'anno e quella forma
        restituisce dizionario: {'TX': 120, 'CA': 45, ...)
        """
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """SELECT state, COUNT(*) AS cnt
                   FROM sighting
                   WHERE YEAR(s_datetime) = %s AND shape = %s
                   GROUP BY state 
                """

        cursor.execute(query, (year, shape))

        for row in cursor:
            result[row['state'].upper()] = row['cnt']

        cursor.close()
        conn.close()
        return result


