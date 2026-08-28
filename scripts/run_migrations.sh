#!/usr/bin/env bash
set -e

if [ "$RUN_MIGRATIONS" = "true" ]; then
    echo "Running database migrations..."
    uv run --no-dev alembic -c app/alembic.ini upgrade head
    echo "Migrations applied successfully!"
else
    echo "Skipping database migrations..."
fi

exec "$@"
