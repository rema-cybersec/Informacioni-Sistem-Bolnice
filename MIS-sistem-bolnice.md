# Sistem Bolnice
## by: Marko Rodic 102/23, http://www.dmi.pmf.uns.ac.rs/

# Intro
Application is written in python 3. It has general utilities designed for hospitals such as: 
- managing patient and doctor records, 
- doctor interfaces for management of checkups and diagnoses, 
- admin interfaces for managing staff and doctors. 
System is designed to follow both GDRP and HIPPA regulations by utilizing several encryption and hashing methods. 
Data storage is done locally with JSON files, however ideally storage would be done using a database. 
System's security depends on separate client and server, however even though the system's design is open for scalability over the network, it's mainly a standalone application. The focus is security, however efficiency, readability and scalability are a big part in system's design.

- Roles: 
	- SysadminUser
	- LekarUser

- Entities: 
	- Sysadmin, 
	- Lekar, 
	- Pacijent, 
	- Pregled, 
	- Dijagnoza, 
	- LogController (not implemented)

# Functionalities:
## Views, Interfaces and Roles:
== GUI == -> part of the GUI
== Functionality == -> part of the back-end

SysadminUser can manage Lekar & Sysadmin entities, but not with Patient, Pregled and Dijagnoza entities. Here's the SysadminUser view:
- `SysadminUser`: 
	- == GUI ==
	- Sysadmin:
		- CreateSysadmin()
		- SearchSysadmin() => ReadSysadmin() => (UpdateSysadmin() | DeleteSysadmin())
	- Lekar:
		- CreateLekar()
		- SearchLekar() => ReadLekar() => (UpdateLekar() | DeleteLekar())
	- == Functionality ==
	- Sysadmin:
		- CreateSysadmin() : requires SysadminUser
		- ReadSysadmin() : requires SysadminUser
		- UpdateSysadmin() : requires SysadminUser
		- DeleteSysadmin() : requires SysadminUser
	- Lekar:
		- CreateLekar() : requires SysadminUser
		- ReadLekar() : requires SysadminUser
		- UpdateLekar() : requires SysadminUser
		- DeleteLekar() : requires SysadminUser

LekarUser cannot manage Lekar entities, but can manage Patient, Pregled and Dijagnoza entities. Here's the LekarUser view:
- `LekarUser`: 
	- == GUI ==
	- Pacijent: 
		- CreatePacijent() 
		- SearchPacijent() => ReadPacijent() => (UpdatePacijent() | DeletePacijent())
	- Pregled: 
		- CreatePregled() : requires Pacijent
		- SearchPregled() => ReadPregled() => (DeletePregled() | UpdatePregled() => CRUD Dijagnoza (4)) 
	- == Functionality ==
	- Pacijent:
		- Create() : requires LekarUser
		- Read() : requires LekarUser
		- Update() : requires LekarUser
		- Delete() : requires LekarUser
	- Pregled:
		- Create() : requires Lekar, Pacijent, LekarUser
		- Read() : requires Lekar, Pacijent, LekarUser
		- Update() : requires Lekar, Pacijent, LekarUser
		- Delete() : requires Lekar, Pacijent, LekarUser
	- Dijagnoza:
		- CreateDijagnoza() : requires Pregled, LekarUser
		- ReadDijagnoza() : requires Pregled, LekarUser
		- UpdateDijagnoza() : requires Pregled, LekarUser
		- DeleteDijagnoza() : requires Pregled, LekarUser

# Login:
Because we have 2 different access levels there will be two views devided into roles
Views will be determined by a login page
Login will launch the application in either LekarView or SysadminView

# Storing
Ideally a DataBase would be used, but since i have no time files will be stored in either CSV file or JSON file.
Because we have to follow GDRP all data except the field `name` have to be encrypted or hashed if it's used as a key for encryption, but I will encrypt/hash everything just to be safe.
Diagnoses stored do not represent a collection of all diagnoses which Lekar can choose from, but their personal diagnoses written during a Pregled.

# Encryption
Usernames will remain unhashed. Passwords will be hashed via bcrypt for ease of access and security. All sensitive patient data will be encrypted with AES-GCM which will use a KDF from personal keys such as patient JMBG. For Key derivation (KDF), PBKDF2 will be used. KDF for Lekar records will be derived from the company key which is an enviroment variable only sysadmins can access. KDF for Pacijent records will be their own JMBG. Patient JMBG cannot be encrypted because all Lekari need to have potential access to their records, therefore Patient JMBG will be hashed via HMAC which will use the secret key enviroment variable available to only Lekar. Availability of enviroment variables should be the server's responsibility, but since this application isn't split into server-client enviroment variables are only gonna be base64 encoded somewhere on the system and loaded during login, after credentials have been confirmed. This will simulate client-server calls, but is definitely the weak-point of security on this system.

For viewing encrypted files roles:
- LekarUser:
	1) must get get patient's consent by getting their JMBG and providing it to access patient's records
	2) must provide secret key to access Pregled records
- SysadminUser:
	1) must provide company key to access Lekar records.
	2) must two-factor authenticate with company key to alter (create/delete/update) Sysadmin records.

## GDRP compliance:
- Data Encryption - AES-GCM with KDF from JMBG or the company key using PBKDF2
- Access Control - (User password + {/, JMBG, secret key, company key} - F2A)
- Minimization of Exposure - LekarUser/SysadminUser only have access to records on-demand
- Right to be forgotten - Delete encrypted data and JMBG hash
- Data protection by design - Keys, hashes, MFA, multiple layers of encryption, limited access
- Audit Logs - logging all actions with timestamps (not implemented)

# Entities & Field Specifications:
- User
	- str: username
	- str: password (hashed with bcrypt)
- Sysadmin implements User:
	- str: username (implementation)
	- str: password (implementation)
- Lekar implements User:
	- str: username (implementation)
	- str: password (implementation)
	- str: ime (encryped with (AES-GCM using {PBKDF2 with company key & salt} as it's key))
	- str: jmbg (encryped with (AES-GCM using {PBKDF2 with company key & salt} as it's key))
	- str: prezime (encryped with (AES-GCM using {PBKDF2 with company key & salt} as it's key))
	- str: specijalizacija (encryped with (AES-GCM using {PBKDF2 with company key & salt} as it's key))
	- str: salt (base64 encrypted)
- Pacijent:
	- str: jmbg (hashed with HMAC using secret key)
	- str: ime (encryped with PBKDF with Pacijent JMBG & salt)
	- str: prezime (encryped with PBKDF with Pacijent JMBG & salt)
	- date: datrodj (encryped with PBKDF with Pacijent JMBG & salt)
	- str: salt (base64 encrypted)
- Pregled: 
	- str: lekar_jmbg (hashed with HMAC with Lekar JMBG & secret key)
	- str: pacijent_jmbg (hashed HMAC with Pacijent JMBG & secret key)
	- date: datum (encryped with AES-GCM using {PBKDF2 from Pacijent JMBG} as it's key)
	- Dijagnoza: dijagnoza
		- str: sifra (encryped with AES-GCM using {PBKDF2 from Pacijent JMBG} as it's key)
		- str: naziv (encryped with AES-GCM using {PBKDF2 from Pacijent JMBG} as it's key)
		- str: opis (encryped with AES-GCM using {PBKDF2 from Pacijent JMBG} as it's key)

# Env Variables: / This would go on the server, but client and server are kinda the same thing in this application
- str: company_key (base64 encoded)
- str: secret (base64 encoded)


# Specification
## Abstract Classes
```python
class AbstractUser(ABC)
```
## Classes
```python
class SysadminUser(AbstractUser)
class LekarUser(AbstractUser)
```
## DataClasses
```python
class Lekar()
class Pacijent()
class Pregled()
```
## General
```python
# STATIC METHODS
def Login(username: str, password: str) -> SysadminUser | LekarUser | None: # Standard Login Function opens either Sysadmin view or Lekar view of the application
def ValidatePassword(username: str, password: str, role: str) -> bool: # Checks {role}.json and validates user.
```
## AbstractUser / User
```python
@abstractmethod
def __init__(self, username: str, password: str)
@abstractmethod
def GetSecretKey(self) -> str
@abstractmethod
def LoadSecretKey(self) -> bool
@abstractmethod
def CheckSecretKey(self, key: str) -> bool
@abstractmethod
def ValidatePassword(self, password: str) -> bool # Validates password
```
## SysadminUser
```python
# Implementations - Sysadmin
def SearchSysadmins(self) -> list # Returns a list of all Sysadmins usernames
def FindSysadmin(self, username: str) -> bool # Returns if a Sysadmin exists
def EncryptSysadminDictionary(self, data: dict, key: str) -> dict
def DecryptSysadminDictionary(self, encrypted_data: dict, key: str) -> dict
# Implementations - Lekar
def SearchLekari(self) -> list # Returns a list of all Lekar usernames
def FindLekar(self, username: str) -> bool # Returns if a Lekar exists
def EncryptLekarDictionary(self, data: dict, key: str) -> dict
def DecryptLekarDictionary(self, encrypted_data: dict, key: str) -> dict
# CRUD - Sysadmin
def CreateSysadmin(self, admin: Sysadmin) -> bool # Encrypts Sysadmin and writes to file. Returns success
def ReadSysadmin(self, username: str, key: str) -> dict | None # Loads sysadmin from memory
def UpdateSysadmin(self, key: str) -> bool # Returns success
def DeleteSysadmin(self, username: str) -> bool # Returns success
# CRUD - Lekar
def CreateLekar(self, lekar: Lekar) -> bool # Encrypts Lekar and writes to file. Returns success
def ReadLekar(self, username: str, key: str) -> dict | None # Loads lekar from memory
def UpdateLekar(self, key: str) -> bool # Returns success
def DeleteLekar(self, username: str) -> bool # Returns success
```
## LekarUser
```python
# Implementations - Pacijent
def FindPacijent(self, username: str) -> bool # Returns if a Pacijent exists
def EncryptPacijentDictionary(self, data: dict, key: str) -> dict
def DecryptPacijentDictionary(self, encrypted_data: dict, key: str) -> dict
# Implementations - Pregled
def FindPregled(self, username: str) -> bool # Returns if a Pregled exists
def EncryptPregledDictionary(self, data: dict, key: str) -> dict
def DecryptPregledDictionary(self, encrypted_data: dict, key: str) -> dict
# Implementations - Dijagnoza
def FindDijagnoza(self, username: str) -> bool # Returns if a Dijagnoza exists
def EncryptDijagnozaDictionary(self, data: dict, key: str) -> dict
def DecryptDijagnozaDictionary(self, encrypted_data: dict, key: str) -> dict
# CRUD - Pacijent
def CreatePacijent(self, pacijent: Pacijent) -> bool # Encrypts Pacijent and writes to file. Returns success
def ReadPacijent(self, username: str, key: str) -> dict | None # Loads Pacijent from memory
def UpdatePacijent(self, key: str) -> bool # Returns success
def DeletePacijent(self, username: str) -> bool # Returns success
# CRUD - Pregled
def CreatePregled(self, pregled: Pregled) -> bool # Encrypts Pregled and writes to file. Returns success
def ReadPregled(self, username: str, key: str) -> dict | None # Loads pregled from memory
def UpdatePregled(self, key: str) -> bool # Returns success
def DeletePregled(self, username: str) -> bool # Returns success
# CRUD - Dijagnoza
def CreateDijagnoza(self, dijagnoza: Dijagnoza) -> bool # Encrypts Dijagnoza and writes to file. Returns success
def ReadDijagnoza(self, username: str, key: str) -> dict | None # Loads dijagnoza from memory
def UpdateDijagnoza(self, key: str) -> bool # Returns success
def DeleteDijagnoza(self, username: str) -> bool # Returns success
```

## Sysadmin
```python
# Constructors
def __init__(self, data: dict) # Sysadmin wrapper data is encrypted
def __init__(self, username: str, password: str) # Sysadmin wrapper data is unencrypted
```
## Lekar
```python
# Constructors
def __init__(self, data: dict) # . wrapper data is encrypted
def __init__(self, fields) # . wrapper data is unencrypted
```

## Pacijent
```python
def __init__(self, data: dict) # . wrapper data is encrypted
def __init__(self, fields) # . wrapper data is unencrypted
```

## Pregled
```python
def __init__(self, data: dict) # . wrapper data is encrypted
def __init__(self, fields) # . wrapper data is unencrypted
```

# GUI
Graphical Interface has been done with `customtkinter` library.

# Sources
- Python for everybody course by Dr. Chuck from freecodecamp.org (General Python Knowledge)
- Information Security course from freecodecamp.org (b-crypt, concept and usage in javascript)
- Python course from Udemy (General Python Knowledge, Working with JSON and CSV in Python)
- Script Languages course by Jovana Vidakovic from PMF (General Python Knowledge)
- YouTube videos by ArjanCodes (Python Dataclasses)
- Analysis and experimentation on `complex_example.py`, an example code provided in the python `customtkinter` library (Python customtkinter library)
- Encryption by Bart Prenel from IPICS2025 (SHA256, BASE64, AES, KDF)
- Googling/Stack Overflow (Python ABC, PBKDF2)
- Various courses from IPICS2025 (GDRP, CIA)
- Object-oriented programming course by Aleksandra Klasnja-Milicevic from PMF (Object-oriented programming and object-oriented approach to programing)
- Modeling of Informational System course by Danijela Boberic-Krsticev from PMF
- Self-research and projects in Unity/C# (Object-oriented approach to programing)