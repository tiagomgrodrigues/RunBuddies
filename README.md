# RunBuddies

RunBuddies is a social running app that helps users find running partners, track their progress, and stay motivated through community-driven challenges and achievements.

Think of it as a community-driven Strava for runners who want not just to run, but to run together.

---

## 🌟 Features

### 🧍 Find a Running Buddy

- Match with runners based on pace, location, and availability
- Send and receive buddy requests
- Track joint runs and group achievements

### 📊 Track Your Runs

- Log distance, duration, pace, and route (optionally via GPS)
- Review personal stats and running history
- Filter by time period, distance, or buddy runs

### 🏆 Community Challenges

- Join weekly/monthly running challenges
- Earn badges and personal achievements
- Leaderboards and team participation

### 💬 Social Engagement

- Like and comment on runs
- Follow your buddies' progress
- Activity feed with real-time updates

### 🔐 Secure & Smooth Experience

- JWT-based authentication and protected routes
- Responsive design (optimized for mobile)
- Progressive Web App (PWA) support (coming soon)

---

## 🛠️ Tech Stack

| Layer        | Technology                              |
| ------------ | --------------------------------------- |
| **Frontend** | Angular + TypeScript                    |
| **Backend**  | FastAPI (Python)                        |
| **Database** | PostgreSQL (optionally PostGIS for GPS) |
| **Auth**     | JWT                                     |
| **DevOps**   | Docker, Docker Compose                  |
| **Testing**  | Jest, Pytest                            |

---

## 📦 Project Structure

```bash
runbuddies/
├── backend/
│   ├── app/
│   │   ├── api/               # API routes
│   │   ├── core/              # App configs, JWT utils
│   │   ├── db/                # DB models and session
│   │   └── main.py            # FastAPI entry point
├── frontend/
│   └── src/                   # Angular app code
├── docker-compose.yml
└── README.md
```

---

## 🧪 Local Development

### 🧰 Requirements

- Node.js (v18+)
- Python 3.10+
- Docker & Docker Compose
- Poetry (for Python dependency management)

### 🚀 Run with Docker (recommended)

```bash
# Run both frontend and backend
docker-compose up --build
```

### 🧱 Manual Setup

#### 1. Backend (FastAPI)

```bash
cd backend
poetry install
alembic upgrade head  # Apply DB migrations
uvicorn app.main:app --reload
```

#### 2. Frontend (Angular)

```bash
cd frontend
npm install
ng serve --open
```

---

## 📚 API Overview

- `POST /auth/register` – Create a new user
- `POST /auth/login` – Get JWT token
- `GET /users/me` – Get current user info
- `POST /runs/` – Log a run
- `GET /runs/` – List all runs
- `POST /buddies/request` – Send a buddy request
- `GET /challenges/` – Get active challenges

(Detailed API docs available at `/docs` when backend is running)

---

## 🧑‍💻 Contributing

We welcome contributions! To get started:

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to your branch: `git push origin feature/your-feature`
5. Create a pull request

Before submitting a PR, please:

- Write tests for new functionality
- Follow existing code style
- Check for linting errors

---

## 📈 Roadmap

- [x] Project scaffolding
- [ ] User authentication
- [ ] Run logging and profile dashboards
- [ ] Buddy system and feed
- [ ] Community challenges
- [ ] PWA & mobile optimization
- [ ] Full test coverage
- [ ] Deployment (Railway/Fly.io/Render)

---

## 🧾 License

---

## 📬 Contact

Created by [Tiago Rodrigues](https://github.com/tiagomgrodrigues) and [André Pinto](https://github.com/pinto-andre).

Have feedback or ideas? Open an issue or reach out!
