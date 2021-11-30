import mysql.connector

class conector:
    try:        
        def executar(query):#INSERT. UPDATE. DELETE
            try:
                con = mysql.connector.connect(user='user', password='user', host='127.0.0.1', database='atacadao') # Recebe os dados de acesso ao banco e faz a conexão
                cursor = con.cursor()
                cursor.execute(query)
                cursor.close()
                con.commit()
                con.close()
            except Exception as e:
                print(e)

        def buscar(query):#SELECT
            try:
                con = mysql.connector.connect(user='user', password='user', host='127.0.0.1', database='atacadao')
                cursor = con.cursor()
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                con.close()

    except Exception as e:
        print(str(e))