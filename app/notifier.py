def notify(payload):
    count = len(payload['payload'])
    return f'Observadores foram notificados sobre {count} caixas que precisam de atencao'