# keyboards.py
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_subscribe_keyboard():
    """Возвращает клавиатуру для начального предложения о подписке."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔔 Включить напоминания", callback_data="subscribe")
    builder.button(text="🚫 Не хочу напоминаний", callback_data="unsubscribe")
    builder.adjust(1)
    return builder.as_markup()

def get_time_selection_keyboard():
    """Возвращает клавиатуру для выбора времени напоминаний."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🌅 Утро (09:00) МСК", callback_data="set_time_09:00")
    builder.button(text="☀️ День (14:00) МСК", callback_data="set_time_14:00")
    builder.button(text="🌙 Вечер (20:00) МСК", callback_data="set_time_20:00")
    builder.adjust(1)
    return builder.as_markup()

def get_settings_keyboard(subscription):
    """Возвращает клавиатуру для меню настроек."""
    builder = InlineKeyboardBuilder()
    if subscription and subscription[0]:  # Если subscribed == True
        builder.button(text="✏️ Изменить время", callback_data="change_time")
        builder.button(text="🚫 Отключить напоминания", callback_data="unsubscribe")
    else:
        builder.button(text="🔔 Включить напоминания", callback_data="subscribe")
    builder.adjust(1)
    return builder.as_markup()