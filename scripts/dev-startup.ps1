# Constitutional AI - Development Startup Script (Windows PowerShell)
# This script sets up and starts the development environment

Write-Host "🚀 Starting Constitutional AI Development Environment..." -ForegroundColor Cyan

# Check if Docker is running
try {
    docker info | Out-Null
    Write-Host "✓ Docker is running" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Docker is not running. Please start Docker first." -ForegroundColor Yellow
    exit 1
}

# Check if .env files exist
if (-not (Test-Path "backend\.env")) {
    Write-Host "⚠️  backend\.env not found. Creating from example..." -ForegroundColor Yellow
    Copy-Item "backend\.env.example" "backend\.env"
    Write-Host "⚠️  Please edit backend\.env and add your API keys" -ForegroundColor Yellow
}

if (-not (Test-Path "frontend\.env")) {
    Write-Host "⚠️  frontend\.env not found. Creating from example..." -ForegroundColor Yellow
    Copy-Item "frontend\.env.example" "frontend\.env"
}

Write-Host "✓ Environment files ready" -ForegroundColor Green

# Start Docker services
Write-Host "📦 Starting Docker services..." -ForegroundColor Cyan
Set-Location docker
docker-compose up -d

Write-Host "✓ Docker services started" -ForegroundColor Green

# Wait for services to be ready
Write-Host "⏳ Waiting for services to be ready..." -ForegroundColor Cyan
Start-Sleep -Seconds 10

# Check service health
Write-Host "🔍 Checking service health..." -ForegroundColor Cyan

# Check PostgreSQL
try {
    docker-compose exec -T postgres pg_isready -U constitutional_user | Out-Null
    Write-Host "✓ PostgreSQL is ready" -ForegroundColor Green
} catch {
    Write-Host "⚠️  PostgreSQL is not ready yet" -ForegroundColor Yellow
}

# Check Redis
try {
    docker-compose exec -T redis redis-cli ping | Out-Null
    Write-Host "✓ Redis is ready" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Redis is not ready yet" -ForegroundColor Yellow
}

# Check Elasticsearch
try {
    Invoke-WebRequest -Uri "http://localhost:9200/_cluster/health" -UseBasicParsing | Out-Null
    Write-Host "✓ Elasticsearch is ready" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Elasticsearch is starting..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Development environment is ready!" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Access points:" -ForegroundColor Cyan
Write-Host "   Frontend:  http://localhost:3000"
Write-Host "   Backend:   http://localhost:8000"
Write-Host "   API Docs:  http://localhost:8000/api/docs"
Write-Host ""
Write-Host "📝 Useful commands:" -ForegroundColor Cyan
Write-Host "   View logs:        cd docker; docker-compose logs -f"
Write-Host "   Stop services:    cd docker; docker-compose down"
Write-Host "   Restart services: cd docker; docker-compose restart"
Write-Host ""
Write-Host "Happy coding! ⚖️" -ForegroundColor Cyan

Set-Location ..
