# 🕶️ Workouts CLI - Vintage Spy Terminal 💾

> A retro-styled command line tool for analyzing workout data with ASCII charts and 1970s spy-film aesthetics

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Terminal](https://img.shields.io/badge/Interface-Terminal-black.svg)](https://github.com/ataxali/workouts-cli)

## 🎯 Features

- **🎨 Retro ASCII Art Banner** - Clean "WORKOUTS" display with vintage terminal styling
- **📊 Interactive Volume Charts** - ASCII bar charts showing workout volume by date
- **🔍 Interactive Session Mode** - Explore your data with spy-terminal commands
- **📈 Exercise Analysis** - Detailed breakdown of exercises and set counts
- **🏋️ Workout Statistics** - Total volume, workout frequency, and performance metrics
- **🚀 Global CLI Access** - Use from anywhere on your system

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- pandas
- rich

### Quick Install

```bash
# Clone the repository
git clone https://github.com/ataxali/workouts-cli.git
cd workouts-cli

# Install dependencies
pip install -r requirements.txt

# Install globally
pip install -e .

# You can now use 'workouts' from anywhere!
workouts --help
```

## 🎮 Usage

### Basic Usage

```bash
# Analyze your workout data
workouts --file data.csv

# Show detailed statistics
workouts --file data.csv --stats

# Enter interactive mode explicitly
workouts --file data.csv --interactive
```

### CSV Format

Your workout data should be in this format:

```csv
Date,Exercise,Sets,Reps per Set,Weight Used (lbs),Total Volume (lbs)
2025-08-10,Smith Machine Bench Press (Flat),5,9,135,6075
2025-08-10,Lat Pulldown,10,10,100,10000
2025-08-14,Smith Machine Deep Squats,10,9,135,12150
```

### Interactive Commands

Once in the spy terminal, use these classified commands:

- `chart` - Display volume chart
- `stats` - Show workout statistics
- `exercises` - List all exercises with set counts
- `help` - Show available commands
- `exit` - Terminate session

## 🎨 Screenshots

```
╭─────────────────────────────────── ⚡ MISSION CONTROL ⚡ ───────────────────────────────────╮
│     ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗███████╗              │
│     ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝              │
│     ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║   ██║██║   ██║   ██║   ███████╗              │
│     ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║   ██║██║   ██║   ██║   ╚════██║              │
│     ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗╚██████╔╝╚██████╔╝   ██║   ███████║              │
│      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝              │
│                                                                                         │
│                            🏋️‍♂️ CLASSIFIED DATA TERMINAL 🏋️‍♀️                              │
│                              💪 STRENGTH ANALYSIS SYSTEM 💪                            │
╰────────────────────────── 🔒 SECURE WORKOUT INTELLIGENCE v2.0 🔒 ──────────────────────╯

═══ VOLUME ANALYSIS ═══

Total Volume by Date (Max: 50,450 lbs)

08-10 │██████████████████████████████████████            │ 39,250 lbs ( 77.8%)
08-14 │██████████████████████████████████████████████████│ 50,450 lbs (100.0%)
08-15 │██████████                                        │ 10,350 lbs ( 20.5%)
08-16 │███████████████████████                           │ 24,024 lbs ( 47.6%)

CLASSIFIED > exercises

CLASSIFIED EXERCISE DATABASE (19 entries):
   1. Smith Machine Bench Press (Flat) (5 total sets)
   2. Lat Pulldown (20 total sets)
   3. Smith Machine Deep Squats (10 total sets)
   ...
```

## 🔧 Development

### Project Structure

```
workouts-cli/
├── workouts.py          # Main CLI application
├── setup.py            # Package configuration
├── requirements.txt    # Dependencies
├── data.csv           # Sample workout data
└── README.md          # This file
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🚀 Roadmap

- [ ] Exercise breakdown charts
- [ ] Muscle group analysis
- [ ] Personal record (PR) detection
- [ ] Animated chart effects
- [ ] Terminal sound effects
- [ ] Export to PNG/PDF
- [ ] Weekly/monthly trend analysis
- [ ] Workout intensity tracking

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎬 Inspiration

Built with the aesthetic of 1970s military computer terminals and spy films. Think *WarGames* meets modern fitness
tracking.

---

**"SHALL WE PLAY A GAME? HOW ABOUT A NICE WORKOUT ANALYSIS?"** 🎮💪

*Made with ❤️ and a love for vintage computing aesthetics*