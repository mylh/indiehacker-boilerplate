#!/usr/bin/env bash
# utility script to set environment variables for the current shell

# Show env vars
grep -v '^#' app.env

# Export env vars
export $(grep -v '^#' app.env | xargs)
