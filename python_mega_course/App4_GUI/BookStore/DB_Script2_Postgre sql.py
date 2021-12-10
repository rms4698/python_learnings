import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname = 'Muthu_First_DB' user='postgres' password='Muthu981156' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 5, 5.5)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname = 'Muthu_First_DB' user='postgres' password='Muthu981156' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)",
                (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname = 'Muthu_First_DB' user='postgres' password='Muthu981156' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(
        "dbname = 'Muthu_First_DB' user='postgres' password='Muthu981156' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item, ))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect(
        "dbname = 'Muthu_First_DB' user='postgres' password='Muthu981156' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
print(view())
# insert("Water Glass1", 6, 5.5)
# insert("Wine Glass", 6, 6.5)
# print(view())
# delete('Water Glass')
# print(view())
update('Water Glass1', 11, 9.5)
print(view())
