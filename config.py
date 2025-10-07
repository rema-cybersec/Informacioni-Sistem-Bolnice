import os

# Base Directory
BASE_DIR= os.path.dirname(os.path.abspath(__file__))

# Data Directory
DATA_DIR = os.path.join(BASE_DIR, 'data')
ADMINS_JSON_PATH = os.path.join(DATA_DIR, 'admins.json')
LEKARI_JSON_PATH = os.path.join(DATA_DIR, 'lekari.json')
PACIJENTI_JSON_PATH = os.path.join(DATA_DIR, 'pacijenti.json')
DIJAGNOZE_JSON_PATH = os.path.join(DATA_DIR, 'dijagnoze.json')

# Entities Directory
ENTITIES_DIR = os.path.join(BASE_DIR, 'entities')
LEKAR_CLASS_PATH = os.path.join(ENTITIES_DIR, 'Lekar.py')
PACIJENT_CLASS_PATH = os.path.join(ENTITIES_DIR, 'Pacijent.py')
PREGLED_CLASS_PATH = os.path.join(ENTITIES_DIR, 'Pregled.py')
SYSADMIN_CLASS_PATH = os.path.join(ENTITIES_DIR, 'Sysadmin.py')

# GUI Directory
GUI_DIR = os.path.join(BASE_DIR, 'gui')
LOGIN_PAGE_PATH = os.path.join(GUI_DIR, 'Login.py')
ADMINVIEW_RECORDS_PATH = os.path.join(GUI_DIR, 'AdminViewRecords.py')
ADD_USERS_PY_PATH = os.path.join(GUI_DIR, 'AddUser.py')

# GUI/Records Directory
GUI_RECORDS_DIR = os.path.join(GUI_DIR, 'records')
RECORDS_PY = os.path.join(GUI_RECORDS_DIR, 'Records.py')
ADMIN_RECORDS_PY = os.path.join(GUI_RECORDS_DIR, 'AdminRecords.py')
LEKAR_RECORDS_PY = os.path.join(GUI_RECORDS_DIR, 'LekarRecords.py')
PACIJENT_RECORDS_PY = os.path.join(GUI_RECORDS_DIR, 'PacijentRecords.py')
DIJAGNOZA_RECORDS_PY = os.path.join(GUI_RECORDS_DIR, 'DijagnozaRecords.py')

# GUI/Views Directory
VIEWS_DIR = os.path.join(GUI_DIR, 'views')
VIEW_PATH = os.path.join(VIEWS_DIR, 'View.py')
ADMINVIEW_PATH = os.path.join(VIEWS_DIR, 'AdminView.py')
LEKARVIEW_PATH = os.path.join(VIEWS_DIR, 'LekarView.py')


# Users Directory
USERS_DIR = os.path.join(BASE_DIR, 'users')
USER_CLASS_PATH = os.path.join(USERS_DIR, 'User.py')
LEKAR_USER_PATH = os.path.join(USERS_DIR, 'LekarUser.py')
SYSADMIN_USER_PATH = os.path.join(USERS_DIR, 'SysadminUser.py')

# Utilities Directory
UTILS_DIR = os.path.join(BASE_DIR, 'utils')
UTILS_PY_PATH = os.path.join(UTILS_DIR, 'Utils.py')
KEYS_DIR = os.path.join(UTILS_DIR, 'keys')
COMPANY_KEY_GPG_PATH = os.path.join(KEYS_DIR, 'company_key.gpg')
SECRET_KEY_GPG_PATH = os.path.join(KEYS_DIR, 'secret_key.gpg')
TEST_PY_PATH = os.path.join(UTILS_DIR, 'test.py')
