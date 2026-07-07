# Word Counter Telegram Bot (@wordcounter67bot)

A simple Telegram bot that counts words, characters, and sentences, and estimates reading time for any text you send it.

## Features
- `/start` – welcome message
- `/help` – usage instructions
- Send any text message → get word/character/sentence count + reading time

---

## 1. Get your bot token

1. Open Telegram and message **@BotFather**
2. Send `/newbot` (or use your existing `@wordcounter67bot`)
3. Copy the token BotFather gives you — looks like:
   `123456789:AAExampleTokenStringHere`

Keep this token secret — treat it like a password.

---

## 2. Push this project to GitHub

```bash
cd wordcounter-bot
git init
git add .
git commit -m "Initial commit - word counter bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/wordcounter-bot.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username, and make sure you've created an empty repo on GitHub first (no README/license, so there's no merge conflict).

---

## 3. Deploy on Railway

1. Go to https://railway.app and log in (GitHub login is easiest)
2. Click **New Project → Deploy from GitHub repo**
3. Select your `wordcounter-bot` repo
4. Once it's created, go to your project's **Variables** tab and add:
   - `BOT_TOKEN` = the token you got from BotFather
5. Railway will detect the `Procfile` and run the bot as a **worker** process
6. Check the **Deployments → Logs** tab — you should see `Bot is starting...`

That's it. Your bot is now live 24/7. Go to Telegram, open `@wordcounter67bot`, and send it some text.

---

## Local testing (optional)

```bash
pip install -r requirements.txt
export BOT_TOKEN="your-token-here"   # On Windows: set BOT_TOKEN=your-token-here
python bot.py
```

---

## Notes
- This bot uses **long polling** (`run_polling()`), which is the simplest setup and works fine on Railway's worker dynos — no public URL/webhook needed.
- If you later want to add more tools (plagiarism checker, currency converter, etc.) to the same bot, add new handlers in `bot.py` following the same pattern as `count_words`.
