# DevDungeon Backend

A gamified learning API where players are backend devs exploring a dungeon of coding challenges.

---

## Features (planned)

- Player profiles (Username, Avatar, XP, Level, Region)
- Regions & region-specific questions
- Items & inventory management
- Game sessions (track XP earned, rewards, time played)
- Global & region-specific leaderboards
- Rewards & achievements system

---

## Current Week-2 Status

- Basic Flask API running successfully
- Routes implemented:
  - `GET /api/players`
  - `POST /api/players`
  - `GET /api/regions`
- Dockerfile for containerizing the backend
- `docker-compose.yml` with a Postgres service defined (database integration planned for Week 3+)
- Project is pushed to a public GitHub repository

---

## API Endpoints (Current)

| Method | Endpoint     | Description         |
| ------ | ------------ | ------------------- |
| GET    | /api/players | List all players    |
| POST   | /api/players | Create a new player |
| GET    | /api/regions | List all regions    |

---

## Run locally (no Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

- Visit API:

http://localhost:5000/api/regions

http://localhost:5000/api/players

## Run with Docker

```bash
docker build -t devdungeon-backend .
docker run -p 5000:5000 devdungeon-backend
```

- Visit API:

http://localhost:5000/api/regions

http://localhost:5000/api/players
