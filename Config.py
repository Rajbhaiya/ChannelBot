import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', True)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', '13675555'))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', 'c0da9c346d2c45dbc7ec49a05da9b2b6')
    OWNER_ID = os.environ.get('OWNER_ID', '5591954930')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '6680969743:AAHpx2FWxrJDDBZTasyyUk05h7a0zG6aeMc')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://apfieuka:ADzi89DykPp6i99R-GvnH_1nxsWjVLSQ@stampy.db.elephantsql.com/apfieuka')
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', 'Wizard_Bots')
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ... # api id here
    OWNER_ID = ...
    API_HASH = "Hash Here"
    BOT_TOKEN = "TOKEN here"
    DATABASE_URL = "Url here"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "OldLostFriends" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
