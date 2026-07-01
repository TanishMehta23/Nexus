from database.connection import get_connection


def save_memory(memory_key: str, memory_value: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memories (memory_key, memory_value)
        VALUES (%s, %s)

        ON CONFLICT (memory_key)
        DO UPDATE

        SET
            memory_value = EXCLUDED.memory_value,
            updated_at = CURRENT_TIMESTAMP;
        """,
        (memory_key, memory_value),
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_memory(memory_key: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT memory_value
        FROM memories

        WHERE memory_key = %s;
        """,
        (memory_key,),
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]

    return None


def get_all_memories():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT memory_key, memory_value
        FROM memories
        ORDER BY memory_key;
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows