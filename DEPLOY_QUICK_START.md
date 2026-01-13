# Quick Start: Deploy to Fly.io

## 🚀 Fast Deployment (5 minutes)

### 1. Install Fly CLI
```powershell
# Windows
iwr https://fly.io/install.ps1 -useb | iex

# macOS/Linux
curl -L https://fly.io/install.sh | sh
```

### 2. Login
```bash
fly auth login
```

### 3. Create App
```bash
fly launch
# Choose a unique app name (e.g., my-discord-bot-123)
# Choose a region (e.g., iad for Washington DC)
# Say No to PostgreSQL and Redis
# Say No to deploying now
```

### 4. Set Bot Token
```bash
fly secrets set DISCORD_TOKEN=your_actual_bot_token_here
```

### 5. Deploy
```bash
fly deploy
```

### 6. Keep It Running
```bash
fly scale count 1
```

### 7. Check Logs
```bash
fly logs
```

You should see: `YourBotName#1234 has logged in!`

## ✅ Done!

Your bot is now running 24/7 on Fly.io!

## 📖 Full Guide

See `docs/FLY_IO_DEPLOYMENT_GUIDE.md` for detailed instructions, troubleshooting, and advanced configuration.

## 🔧 Common Commands

```bash
fly logs              # View logs
fly status            # Check status
fly deploy            # Deploy updates
fly secrets list      # List secrets
fly apps restart      # Restart bot
```
