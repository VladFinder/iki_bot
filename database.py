import sqlite3

def init_db():
    """Инициализирует базу данных и создает таблицу, если она не существует."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            subscribed BOOLEAN NOT NULL CHECK (subscribed IN (0, 1)),
            notification_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_or_update_user(user_id, subscribed=False, notification_time=None):
    """Добавляет нового пользователя или обновляет существующего."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (user_id, subscribed, notification_time)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
        subscribed = excluded.subscribed,
        notification_time = excluded.notification_time;
    ''', (user_id, subscribed, notification_time))
    conn.commit()
    conn.close()

def get_user_subscription(user_id):
    """Получает статус подписки пользователя."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT subscribed, notification_time FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_subscribed_users_by_time(time_str):
    """Получает всех пользователей, подписанных на определенное время."""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE subscribed = 1 AND notification_time = ?', (time_str,))
    users = cursor.fetchall()
    conn.close()
    return [user[0] for user in users]