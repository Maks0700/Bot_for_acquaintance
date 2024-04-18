import sqlite3 as sq




async def create_first_db():
    db=sq.connect("Telegram_bo.db")
    cur=db.cursor()
    
    
    cur.execute("CREATE TABLES IF NOT EXISTS user('name TEXT')")
    
    
    
    db.commit()