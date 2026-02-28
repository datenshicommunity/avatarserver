#!/bin/sh
# Seed default avatar into the volume if it doesn't exist
if [ ! -f /app/avatars/-1.png ]; then
    cp /app/seed/-1.png /app/avatars/-1.png
fi

exec "$@"
