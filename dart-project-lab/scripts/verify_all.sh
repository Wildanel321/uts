#!/usr/bin/env bash
set -e
echo "====================================================="
echo "   DART PROJECT LAB — BASH VERIFICATION SCRIPT       "
echo "====================================================="

if ! command -v dart &> /dev/null; then
    echo "Error: Dart SDK is not installed or not in PATH."
    exit 1
fi

echo "Dart SDK Version:"
dart --version

echo ""
echo "Launching Dart Verification Runner..."
dart run tool/verify_all.dart
