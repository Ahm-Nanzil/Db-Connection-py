import mysql.connector

def dbConnect():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='test'
        )
        print("✅ Database connected successfully.")
        return conn
    except Exception as ex:
        print("❌ Database connection failed:", ex)
        return None

def SQLExecution(SQLString):
    Conn = None
    try:
        Conn = dbConnect()
        if Conn is None:
            raise Exception("Connection is None")

        cursor = Conn.cursor()
        cursor.execute(SQLString)
        Conn.commit()
        print("✅ SQL executed successfully.")
    except Exception as E:
        print("❌ Error during SQL execution:", E)
        if Conn:
            Conn.rollback()
    finally:
        if Conn:
            Conn.close()
            print("🔒 Connection closed.")

# 👇 Add this to trigger execution
if __name__ == "__main__":
    SQLExecution("INSERT INTO my_table (name) VALUES ('Test')")
