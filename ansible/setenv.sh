#!/usr/bin/env bash
# utility script to set environment variables for the current shell
# Usage: source setenv.sh
# Note: This script should be sourced!!!, not executed

# Show env vars
grep -v '^#' app.env

# Export env vars
export $(grep -v '^#' app.env | xargs)
