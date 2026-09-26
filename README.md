# KAL-Online-Admin-Panel
KAL Online admin panel for magaing palyers and databases


# KAL Online Admin Panel

A Python/PySide6 administration tool for KAL Online servers.

## About the Project

The **KAL Online Admin Panel** is a desktop administration tool for KAL Online server administrators.

The idea for this project goes back to my time as a KAL Online server administrator, where I used the admin name Admin JOKER.

Back then, another member of our administration team, Admin Klicker, developed a web-based PHP administration panel for our server. I always found the concept of having a dedicated administration interface for managing characters and server data extremely useful and interesting.

Years later, while working with a KAL Online server again and developing my own skills with Python, I decided to finally recreate that idea myself — this time as a Python/PySide6 desktop application.

The project is built around real KAL Online database structures rather than mock or demonstration data. The goal is to gradually develop a practical administration tool specifically designed around the needs of KAL Online server administrators.

---

## Current Version

v0.1

The first public version focuses on the basic foundation of the administration panel.

### Current Features

* Connect to a KAL Online SQL Server database
* Search for players by character name
* Display player information
* Edit selected player values
* SQL Server authentication
* Windows authentication
* Configuration through `config.ini`
* Custom KAL-themed graphical interface
* Player data based on the actual KAL Online database structure

### Player Information

The current version can display and edit various player values, including:

* Player ID
* Character name
* Level
* Class
* Specialty
* Experience
* Strength
* Health
* Intelligence
* Wisdom
* Dexterity
* HP / MP
* Contribution
* Skill points
* Guild information
* Map position
* Coordinates
* Other character-related database values

---

## Requirements

The current version requires:

* Windows
* Python 3.x
* PySide6
* pyodbc
* Microsoft SQL Server
* A suitable Microsoft ODBC driver
* A KAL Online database

The application is currently designed primarily for a locally accessible SQL Server installation.

Remote database access is planned for a future version.

---

## Installation

Clone or download the repository and install the required Python packages.

```bash
pip install PySide6 pyodbc
```

Create your local configuration file by copying:

```text
config.ini.example
```

to:

```text
config.ini
```

Then enter your own database connection settings.

Do not upload your personal `config.ini` or database credentials to GitHub.

The real `config.ini` file is excluded from version control through `.gitignore`.

---

## Configuration

The configuration file contains the database connection settings required by the application.

Example:

```ini
[Database]
Driver=YOUR_ODBC_DRIVER
Server=YOUR_SERVER
Database=KAL_DB
UID=
PWD=
TrustServerCertificate=Yes
TrustedConnection=Yes
```

The exact settings depend on your SQL Server installation and authentication method.

---

## Project Structure

The project is currently kept intentionally simple while the basic architecture is being developed.

```text
KAL Online Admin Panel/
│
├── GUI.py
├── database.py
├── player.py
├── config.ini.example
├── .gitignore
└── ...
```

The project structure will evolve as additional functionality is added.

---

## Roadmap

The long-term goal is to turn the project into a more complete KAL Online administration suite.

Planned features include:

* [ ] Inventory management
* [ ] Storage management
* [ ] Item search by Item ID
* [ ] Item search by Item Index
* [ ] Find all players who own a specific item
* [ ] Edit item amounts and properties
* [ ] Add and delete items
* [ ] Send items between characters
* [ ] Account management
* [ ] Skill management
* [ ] Character XP and level management
* [ ] Additional KAL Online database tools
* [ ] Item history and tracking
* [ ] Additional server administration tools
* [ ] Remote SQL Server support
* [ ] Standalone Windows executable
* [ ] Further GUI improvements

The roadmap is subject to change as development continues.

---

## Project Status

This project is currently in early development.

Version 0.1 is mainly intended as the foundation for the administration panel. More advanced functionality will be added gradually as the project develops.

The application is being developed and tested against real KAL Online server databases.

Always create a database backup before making changes to production data.

---

## Feedback and Contributions

KAL Online server administrators are welcome to test the project and provide:

* Bug reports
* Feature requests
* Suggestions
* Database structure information
* General feedback

If you have an idea for a useful KAL Online administration feature, feel free to open an issue or start a discussion.

---

## Disclaimer

This project is an independent community project and is not affiliated with or endorsed by the original KAL Online developers or publishers.

Use the software at your own risk and always maintain appropriate backups of your server databases.

---

## License

License information will be added in a future version.

