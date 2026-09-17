import sqlite3

def login(username, password):
    connection = sqlite3.connect("users.db")
    
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    
    result = connection.execute(query)
    
    return result.fetchall()

print(login("admin", "123456"))
