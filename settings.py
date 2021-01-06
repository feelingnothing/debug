import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_DEFAULT_PREFIXES = (
    '.', ','
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COGS_DIR = os.path.join(BASE_DIR, 'cogs')
