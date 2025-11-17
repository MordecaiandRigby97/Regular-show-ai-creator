# Regular Show Voice Actor Creator

This lightweight command-line app lets you quickly blueprint songs, movies, and fan videos starring the Regular Show voice cast. Sydney—our original singer with orange hair and green eyes—is included so you can give her both lead and background vocal moments.

## Features
- Build custom **song arrangements** with specific lead and background vocalists.
- Outline **fan videos** that highlight Sydney while keeping the park crew in the spotlight.
- Pitch **movie concepts** that end with a detailed finale song plan.
- Optional JSON export for song blueprints, perfect for plugging into other creative tools.

## Requirements
- Python 3.10+

## Usage
```bash
python app.py song "Star Chords" --lead Mordecai --background Rigby Skips Sydney --vibe "neon disco" --tempo 122 --json
python app.py fanvideo "Sydney's Sunset Solo" --theme "friendship encore" --setting "Park amphitheater"
python app.py movie "Battle of the Bands" --antagonist "Night Owl" --finale-lead Sydney --finale-background Mordecai Rigby Skips
```

Run `python app.py -h` to see all commands and options.
