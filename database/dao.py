from database.DB_connect import DBConnect
from model.team import Team
class DAO:
    @staticmethod
    def get_year():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT(year) FROM team
         where year>1980"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def search_team(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t.id,t.team_code,t.name,sum(salary) as total
            from team t,salary s
            where t.year=%s and s.year= %s and t.id=s.team_id
            group by t.id,t.team_code,t.name
            order by name asc"""
        cursor.execute(query, (year,year))
        for row in cursor:
            result.append(Team(row['id'], row['team_code'], row['name'], row['total']))
        print(result)
        return result

