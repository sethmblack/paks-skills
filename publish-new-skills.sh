#!/bin/bash
cd /Users/ziggs/Documents/InfiniteBackroom/paks-skills

# Read skills from file
while IFS= read -r skill; do
  echo "[START] $skill"
  
  # Check if repo already exists
  if gh repo view "sethmblack/skill-$skill" &>/dev/null; then
    echo "[SKIP] $skill - repo exists"
    continue
  fi
  
  # Create the repo
  echo "  Creating repo skill-$skill..."
  gh repo create "skill-$skill" --public --clone=false
  
  # Clone, copy files, push
  cd /tmp
  rm -rf "skill-$skill"
  git clone "https://github.com/sethmblack/skill-$skill.git"
  cd "skill-$skill"
  
  # Copy SKILL.md
  cp "/Users/ziggs/Documents/InfiniteBackroom/paks-skills/$skill/SKILL.md" .
  
  git add SKILL.md
  git commit -m "Add $skill skill"
  git push origin main
  
  # Publish to paks registry
  echo "  Publishing to paks registry..."
  paks publish
  
  if [ $? -eq 0 ]; then
    echo "[SUCCESS] $skill published!"
  else
    echo "[ERROR] $skill failed to publish"
  fi
  
  cd /Users/ziggs/Documents/InfiniteBackroom/paks-skills
  
  # Rate limit delay
  sleep 30
  
done < /tmp/new-skills-to-publish.txt

echo "Done publishing new skills!"
