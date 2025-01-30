# run_sql.py
import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values=None):
    conn = None
    results = []
    
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="jewellery_shop",
            user="postgres",
            password="Nazar123",  
            host="localhost"
        )
        
        # Create a DictCursor to return results as dictionaries
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        
        # Execute the SQL command
        cur.execute(sql, values)
        
        # Commit the transaction
        conn.commit()
        
        # Fetch results if it's a SELECT query
        if cur.description:  # Only try to fetch if there are results
            results = cur.fetchall()
            
        # Close the cursor
        cur.close()
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
    finally:
        if conn is not None:
            conn.close()
    
    return results