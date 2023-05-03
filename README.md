```
git clone
poetry update
git rm -r --cached "telegram_bot_template\databases"
git rm -r --cached ".env"
git add -A
git commit -m "init commit"
git push
```
don't forget to change name and packages in .toml file
