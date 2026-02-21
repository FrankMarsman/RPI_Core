def log_message(message):
    import datetime
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

log_message('This is a test log message.')