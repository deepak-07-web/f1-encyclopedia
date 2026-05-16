# F1 Encyclopedia 🏎️

A comprehensive Django-based Formula 1 Encyclopedia application with detailed information about drivers, teams, circuits, seasons, records, and more.

## Features

- **Drivers**: Complete database of F1 drivers with stats (races, wins, podiums, championships)
- **Teams**: Historical and current F1 teams with founding info and championship records
- **Circuits**: All F1 race venues with lap records and track specifications
- **Seasons**: Championship standings (driver & constructor) from 2010-2025
- **Records**: Historic F1 records and achievements
- **Glossary**: Technical F1 terminology and racing concepts
- **Hall of Fame**: Legendary F1 drivers
- **Tyres**: Pirelli tyre specifications and compounds

## Tech Stack

- **Backend**: Django 3.x+
- **Database**: SQLite3
- **Python**: 3.11+
- **Frontend**: HTML/CSS/Django Templates

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/deepak-07-web/f1-encyclopedia.git
cd f1-ency
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django pillow
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Populate Data (Optional)
```bash
python manage.py add_drivers
python manage.py add_more_data
python manage.py add_circuits
python manage.py add_comprehensive_data
python manage.py add_season_standings
python manage.py add_final_details
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
f1-ency/
├── manage.py
├── db.sqlite3
├── media/                          # User-uploaded images
│   ├── drivers/
│   ├── teams/
│   ├── circuits/
│   └── ...
├── f1_site/                        # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── drivers/                        # Driver app
│   ├── models.py
│   ├── views.py
│   ├── management/commands/
│   └── templates/
├── teams/                          # Teams app
├── circuits/                       # Circuits app
├── seasons/                        # Seasons app
├── records/                        # Records app
├── glossary/                       # Glossary app
├── halloffame/                     # Hall of Fame app
├── tyres/                          # Tyres app
└── ...
```

## Data Management Commands

All data operations use Django's `.get_or_create()` pattern - **safe, non-destructive additions**:

| Command | Purpose |
|---------|---------|
| `add_drivers` | Add modern F1 drivers |
| `add_more_data` | Add additional drivers, seasons, records, glossary |
| `add_circuits` | Add F1 circuits/venues |
| `add_comprehensive_data` | Add historic teams and drivers |
| `add_season_standings` | Add championship standings (2010-2025) |
| `add_final_details` | Add constructor standings, advanced records, tyres |

## Database Content

**Current Data:**
- ✅ 48 Drivers
- ✅ 21 Teams
- ✅ 25 Circuits
- ✅ 13 Seasons (2010, 2014-2025)
- ✅ 29 Records
- ✅ 62 Glossary Terms
- ✅ 10 Hall of Fame Legends
- ✅ 10 Tyre Types

## Admin Panel

Access Django admin at `http://127.0.0.1:8000/admin/` with your superuser credentials to:
- Add/edit drivers, teams, circuits
- Manage seasons and standings
- Upload images and media
- Edit records and glossary terms

## Adding Images

Images can be added through:
1. **Django Admin**: Upload directly in the admin interface
2. **Media Folder**: Add files to `media/` subdirectories
3. **Management Commands**: Reference images by filename

The project uses organized media directories:
- `media/drivers/` - Driver images
- `media/teams/` - Team logos, cars, garages
- `media/circuits/` - Circuit tracks and aerials
- `media/helmets/` - Driver helmets
- `media/records/` - Record images

## Important Notes

⚠️ **Database & Media Storage:**
- `db.sqlite3` stays local (not in GitHub)
- `media/` folder stays local (not in GitHub)
- These are ignored by `.gitignore`

✅ **After Cloning:**
You can still add more drivers, teams, images, and data without any issues. The database is local to your machine.

## Safe Data Additions

All management commands use Django's `.get_or_create()` method:
- ✅ Won't delete existing data
- ✅ Won't remove images
- ✅ Won't create duplicates if run multiple times
- ✅ Safe for repeated executions

## Data Verification

Run the verification script to check data integrity:
```bash
python verify_data.py
```

This generates a comprehensive report of all database entries without making any changes.

## Contributing

Feel free to:
- Add more drivers and their statistics
- Include additional circuits
- Expand glossary with more F1 terminology
- Add historical records and achievements
- Upload driver/team/circuit images

## License

This project is open-source and available under the MIT License.

## Author

**Deepak** - GitHub: [@deepak-07-web](https://github.com/deepak-07-web)

---

**Enjoy exploring Formula 1 data! 🏁**
