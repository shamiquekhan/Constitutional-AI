#!/bin/bash

# Constitutional AI - Development Startup Script
# This script sets up and starts the development environment

set -e

echo "🚀 Starting Constitutional AI Development Environment..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "${YELLOW}⚠️  Docker is not running. Please start Docker first.${NC}"
    exit 1
fi

echo "${GREEN}✓ Docker is running${NC}"

# Check if .env files exist
if [ ! -f "backend/.env" ]; then
    echo "${YELLOW}⚠️  backend/.env not found. Creating from example...${NC}"
    cp backend/.env.example backend/.env
    echo "${YELLOW}⚠️  Please edit backend/.env and add your API keys${NC}"
fi

if [ ! -f "frontend/.env" ]; then
    echo "${YELLOW}⚠️  frontend/.env not found. Creating from example...${NC}"
    cp frontend/.env.example frontend/.env
fi

echo "${GREEN}✓ Environment files ready${NC}"

# Start Docker services
echo "📦 Starting Docker services..."
cd docker
docker-compose up -d

echo "${GREEN}✓ Docker services started${NC}"

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check service health
echo "🔍 Checking service health..."

# Check PostgreSQL
if docker-compose exec -T postgres pg_isready -U constitutional_user > /dev/null 2>&1; then
    echo "${GREEN}✓ PostgreSQL is ready${NC}"
else
    echo "${YELLOW}⚠️  PostgreSQL is not ready yet${NC}"
fi

# Check Redis
if docker-compose exec -T redis redis-cli ping > /dev/null 2>&1; then
    echo "${GREEN}✓ Redis is ready${NC}"
else
    echo "${YELLOW}⚠️  Redis is not ready yet${NC}"
fi

# Check Elasticsearch
if curl -s http://localhost:9200/_cluster/health > /dev/null 2>&1; then
    echo "${GREEN}✓ Elasticsearch is ready${NC}"
else
    echo "${YELLOW}⚠️  Elasticsearch is starting...${NC}"
fi

echo ""
echo "${GREEN}✅ Development environment is ready!${NC}"
echo ""
echo "📍 Access points:"
echo "   Frontend:  http://localhost:3000"
echo "   Backend:   http://localhost:8000"
echo "   API Docs:  http://localhost:8000/api/docs"
echo ""
echo "📝 Useful commands:"
echo "   View logs:        cd docker && docker-compose logs -f"
echo "   Stop services:    cd docker && docker-compose down"
echo "   Restart services: cd docker && docker-compose restart"
echo ""
echo "Happy coding! ⚖️"
