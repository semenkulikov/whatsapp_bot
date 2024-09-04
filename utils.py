def send_message(greenAPI, group_id, message):
    """
    Отправляет сообщение через WhatsApp API
    """
    result = greenAPI.sending.sendMessage(group_id, message)
    return result
