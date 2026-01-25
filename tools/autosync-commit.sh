#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$repo_root" ]]; then
  echo "Not a git repository."
  exit 1
fi

cd "$repo_root"

if [[ -f .git/MERGE_HEAD || -d .git/rebase-apply || -d .git/rebase-merge ]]; then
  echo "Merge or rebase in progress; aborting autosync."
  exit 1
fi

threshold_seconds=$((4 * 60 * 60))
now_epoch="$(date +%s)"
last_commit_epoch="$(git log -1 --format=%ct 2>/dev/null || echo 0)"
age_seconds=$((now_epoch - last_commit_epoch))

should_commit=false
if (( age_seconds >= threshold_seconds )); then
  should_commit=true
fi

is_dirty=false
if ! git diff --quiet || ! git diff --cached --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; then
  is_dirty=true
fi

if [[ "$is_dirty" == "true" && "$should_commit" == "true" ]]; then
  git add -A
  if ! git diff --cached --quiet; then
    ts="$(date +"%Y-%m-%d %H:%M:%S")"
    git commit -m "autosave: $ts"
  fi
fi

if [[ "$is_dirty" == "true" && "$should_commit" == "false" ]]; then
  git stash push -u -m autosync-temp
  git pull --rebase
  git stash pop
else
  git pull --rebase
fi

git push
