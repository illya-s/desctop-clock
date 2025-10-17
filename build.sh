#!/usr/bin/env bash
set -e

PROJECT_NAME=$(grep '^name\s*=' pyproject.toml | sed 's/name\s*=\s*"\(.*\)"/\1/')
PROJECT_VERSION=$(grep '^version\s*=' pyproject.toml | sed 's/version\s*=\s*"\(.*\)"/\1/')

echo "Сборка проекта: $PROJECT_NAME, версия: $PROJECT_VERSION"

rm -rf build
rm -rf dist
rm main.spec

echo "--- Сборка PyInstaller ---"
pyinstaller --noconfirm --onefile --windowed \
	--add-data "assets:assets" \
	--icon "assets/icon.png" \
	main.py

echo "--- Сборка .deb через fpm ---"
fpm -s dir -t deb -n "$PROJECT_NAME" -v "$PROJECT_VERSION" \
	dist/main=/usr/bin/"$PROJECT_NAME"-clock \
	assets/=/usr/share/"$PROJECT_NAME"/assets \
	desctop-clock.desktop=/usr/share/applications/"$PROJECT_NAME".desktop


echo "--- Готово! ---"
echo "Файл ${PROJECT_NAME}_${PROJECT_VERSION}_amd64.deb создан."
echo "Для установки используйте: sudo apt install ./${PROJECT_NAME}_${PROJECT_VERSION}_amd64.deb"