# CMMS Starter (FastAPI + Next.js)
Run backend:
  cd backend && docker compose up --build
Seed:
  docker compose exec api python -m app.scripts.seed
Run frontend:
  cd frontend && npm install && npm run dev