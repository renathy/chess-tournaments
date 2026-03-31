from database.db import get_connection

class TournamentRepository:

    def find_existing(self, name, tournament_date):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, source
            FROM tournaments
            WHERE name = %s AND tournament_date = %s
        """, (name, tournament_date))

        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result

    def insert(self, tournament):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tournaments (name, tournament_date, source, creation_date, update_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            tournament.name,
            tournament.tournament_date,
            tournament.source,
            tournament.creation_date,
            tournament.update_date
        ))

        conn.commit()
        cursor.close()
        conn.close()

    def update(self, tournament_id, tournament):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tournaments
            SET source = %s,
                update_date = %s
            WHERE id = %s
        """, (
            tournament.source,
            tournament.update_date,
            tournament_id
        ))

        conn.commit()
        cursor.close()
        conn.close()
