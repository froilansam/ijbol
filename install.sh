#!/bin/sh
# Personal install: symlink each skill into ~/.claude/skills so they run
# un-prefixed (/ijbol, /ijbol-lean, ...) and edits in this repo apply immediately.
# Same-named skills and the pre-IJBOL names are moved to
# ~/.claude/skills-backup-<date>, never deleted.
set -eu
src="$(cd "$(dirname "$0")/skills" && pwd)"
dest="$HOME/.claude/skills"
backup="$HOME/.claude/skills-backup-$(date +%Y%m%d-%H%M%S)"
legacy="ulti ponytail clean-code-implementation ui-ux-frontend-review refactoring-ui"

move_aside() {
  if [ -L "$1" ]; then
    rm "$1"
  elif [ -e "$1" ]; then
    mkdir -p "$backup"
    mv "$1" "$backup/"
    echo "backed up $(basename "$1") -> $backup/"
  fi
}

mkdir -p "$dest"
for name in $legacy; do move_aside "$dest/$name"; done
for dir in "$src"/*/; do
  name="$(basename "$dir")"
  move_aside "$dest/$name"
  ln -s "${dir%/}" "$dest/$name"
  echo "linked $name"
done
