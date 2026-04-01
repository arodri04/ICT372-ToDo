import sqlite3
import hashlib

def connectDB():
    try:
        conn = sqlite3.connect('./instance/db.sqlite')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database {e}")
        return None
    
def validateLogin(username, password):
    try:
        conn = connectDB()

        if not conn:
            return False
        
        cursor = conn.cursor()

        query = "SELECT salt, password FROM users WHERE username = ?"
        cursor.execute(query,(username,))
        result = cursor.fetchone()

        if result:
            salt, passHash = result
            combinePass = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()


            if combinePass == passHash:
                return True
            
        return False
    
    except sqlite3.Error as e:
        print(f"Database Error {e}")
        return False
    
    finally:
        if conn:
            conn.close()

def getUserId(username):
    try:
        conn = connectDB()

        if not conn:
            return False
        
        cursor = conn.cursor()

        query = "SELECT userId FROM users WHERE username = ?"
        cursor.execute(query,(username,))
        result = cursor.fetchone()

        if result:
            return result
            
        return False
    
    except sqlite3.Error as e:
        print(f"Database Error {e}")
        return False
    
    finally:
        if conn:
            conn.close()

def getUserTodos(userId):
    try:
        conn = connectDB()

        if not conn:
            return False
        
        cursor = conn.cursor()

        query = "SELECT * FROM todo WHERE userId = ?"
        cursor.execute(query,(userId,))
        result = cursor.fetchall()
        print(result)

        if result:
            return result
            
        return False
    
    except sqlite3.Error as e:
        print(f"Database Error {e}")
        return False
    
    finally:
        if conn:
            conn.close()