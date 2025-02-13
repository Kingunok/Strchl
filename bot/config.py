from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 28693882))
    API_HASH = env.get("TELEGRAM_API_HASH", "bc1f4414271fdd69990edff73dc7adc9")
    OWNER_ID = int(env.get("OWNER_ID", 6940488721))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "TomenRenamerBot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7003249367:AAGHmAugXHy4vFF6fCeXWDMtiKa8WB8-fPo")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002050509771))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 24))
    MULTI_CLIENT = False

class Server:
    BASE_URL = env.get("BASE_URL", "https://slstreamapp.koyeb.app")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "slstreamapp.koyeb.app")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
