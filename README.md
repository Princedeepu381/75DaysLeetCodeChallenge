name: Update LeetCode README

on:
  push:
    branches:
      - master
  workflow_dispatch:

jobs:
  update-readme:
    runs-on: ubuntu-latest
    permissions:
      contents: write 
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetches all history so rebase works

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Run Python Script
        run: python update_readme.py

      - name: Commit and Push Changes
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          
          # Only commit if there are changes
          if git diff --staged --quiet; then
            echo "No changes to commit"
            exit 0
          fi
          
          git commit -m "Auto-update LeetCode progress table 🚀"
          
          # Pull with rebase to sync with any background LeetHub pushes, then push
          git pull origin master --rebase
          git push
