# Deploy Discord Bot to Fly.io - Complete Guide

This guide will walk you through deploying your Discord bot to Fly.io, a platform that makes it easy to run your applications globally.

## 📋 Prerequisites

Before you begin, make sure you have:

1. ✅ A Discord bot token (from Discord Developer Portal)
2. ✅ A Fly.io account (sign up at https://fly.io)
3. ✅ Fly CLI installed on your computer
4. ✅ Git installed (optional but recommended)

---

## Step 1: Install Fly CLI

### Windows (PowerShell)
```powershell
# Download and install Fly CLI
iwr https://fly.io/install.ps1 -useb | iex
```

### macOS/Linux
```bash
curl -L https://fly.io/install.sh | sh
```

### Verify Installation
```bash
fly version
```

You should see the Fly CLI version number.

---

## Step 2: Login to Fly.io

```bash
fly auth login
```

This will open your browser to authenticate. After logging in, you'll be automatically logged into the CLI.

---

## Step 3: Prepare Your Project

### 3.1 Check Required Files

Make sure you have these files in your project root:
- ✅ `bot.py` - Your bot code
- ✅ `requirements.txt` - Python dependencies
- ✅ `Dockerfile` - Container configuration (already created)
- ✅ `fly.toml` - Fly.io configuration (already created)
- ✅ `.dockerignore` - Files to exclude from Docker build (already created)

### 3.2 Update fly.toml

Open `fly.toml` and change the app name:

```toml
app = "your-bot-name"  # Change this to a unique name (e.g., "my-discord-bot-123")
```

**Important:** The app name must be unique across all Fly.io apps. Use lowercase letters, numbers, and hyphens only.

### 3.3 Verify Dockerfile

The Dockerfile is already configured, but make sure it exists and looks correct.

---

## Step 4: Initialize Fly.io App

### 4.1 Create the App

```bash
fly launch
```

This will:
- Ask you to confirm the app name (or create a new one)
- Ask about regions (choose one close to you or your users)
- Ask about PostgreSQL/Redis (say **No** - we don't need them)
- Ask about deploying now (say **No** - we'll do it after setting secrets)

### 4.2 Alternative: Create App Manually

If you prefer to create the app manually:

```bash
fly apps create your-bot-name
```

---

## Step 5: Set Environment Variables (Secrets)

### 5.1 Set Discord Bot Token

**⚠️ IMPORTANT:** Never commit your bot token to Git! Use Fly.io secrets instead.

```bash
fly secrets set DISCORD_TOKEN=your_actual_bot_token_here
```

Replace `your_actual_bot_token_here` with your actual Discord bot token from the Discord Developer Portal.

**Example:**
```bash
fly secrets set DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE.ABCDEF.1234567890abcdefghijklmnopqrstuvwxyz
```

**⚠️ Note:** Replace `YOUR_BOT_TOKEN_HERE.ABCDEF.1234567890abcdefghijklmnopqrstuvwxyz` with your actual bot token from Discord Developer Portal.

### 5.2 Verify Secrets

```bash
fly secrets list
```

You should see `DISCORD_TOKEN` listed (the value will be hidden for security).

---

## Step 6: Deploy Your Bot

### 6.1 Build and Deploy

```bash
fly deploy
```

This will:
1. Build a Docker image from your Dockerfile
2. Push it to Fly.io
3. Deploy it to your app
4. Start your bot

### 6.2 Watch the Logs

While deploying, you can watch the logs:

```bash
fly logs
```

Or in a separate terminal:

```bash
fly logs -a your-bot-name
```

You should see:
```
YourBotName#1234 has logged in!
Bot is in X servers
```

---

## Step 7: Verify Deployment

### 7.1 Check App Status

```bash
fly status
```

### 7.2 Check Logs

```bash
fly logs
```

Look for:
- ✅ "has logged in!" message
- ✅ "Bot is in X servers" message
- ❌ Any error messages

### 7.3 Test in Discord

1. Go to your Discord server
2. Check if the bot is online (green status)
3. Try a command: `!help_bot`

---

## Step 8: Keep Bot Running (Important!)

### 8.1 Ensure Bot Stays Online

Fly.io apps can scale to zero if not configured properly. To keep your bot running:

**Option 1: Set Minimum Instances (Recommended)**

```bash
fly scale count 1
```

This ensures at least 1 instance is always running.

**Option 2: Update fly.toml**

Add this to your `fly.toml`:

```toml
[processes]
  app = "python bot.py"

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

### 8.2 Auto-Restart on Crash

Fly.io automatically restarts your app if it crashes. This is enabled by default.

---

## Step 9: Monitor Your Bot

### 9.1 View Logs

```bash
# Real-time logs
fly logs

# Last 100 lines
fly logs --limit 100

# Follow logs (like tail -f)
fly logs -f
```

### 9.2 Check Metrics

```bash
fly status
```

Or visit your app dashboard:
```
https://fly.io/apps/your-bot-name
```

### 9.3 View App Info

```bash
fly info
```

---

## Step 10: Update Your Bot

When you make changes to your bot:

### 10.1 Make Changes Locally

Edit your files (e.g., `bot.py`)

### 10.2 Deploy Updates

```bash
fly deploy
```

Fly.io will:
- Build a new Docker image
- Deploy the new version
- Automatically restart your bot

### 10.3 Rollback if Needed

If something goes wrong:

```bash
fly releases
fly releases rollback <release-id>
```

---

## Troubleshooting

### Bot Shows as Offline

**Problem:** Bot appears offline in Discord

**Solutions:**
1. Check logs: `fly logs`
2. Verify token is set: `fly secrets list`
3. Check if app is running: `fly status`
4. Restart the app: `fly apps restart your-bot-name`

### "Invalid Token" Error

**Problem:** Bot can't log in

**Solutions:**
1. Verify token is correct: `fly secrets list`
2. Reset token in Discord Developer Portal
3. Update secret: `fly secrets set DISCORD_TOKEN=new_token`

### Bot Keeps Restarting

**Problem:** Bot crashes and restarts repeatedly

**Solutions:**
1. Check logs: `fly logs` for error messages
2. Verify all dependencies are in `requirements.txt`
3. Check if `settings.json` exists and is valid
4. Ensure bot has proper error handling

### Out of Memory

**Problem:** App runs out of memory

**Solutions:**
1. Increase memory: `fly scale memory 512`
2. Check for memory leaks in your code
3. Review logs for memory-related errors

### Build Fails

**Problem:** `fly deploy` fails during build

**Solutions:**
1. Check Dockerfile syntax
2. Verify all files exist (bot.py, requirements.txt)
3. Test Docker build locally: `docker build -t test .`
4. Check Fly.io status page for service issues

### Can't Connect to Discord

**Problem:** Bot can't connect to Discord API

**Solutions:**
1. Check Discord status: https://discordstatus.com
2. Verify internet connectivity in logs
3. Check if Discord API is blocking your IP (unlikely on Fly.io)
4. Review firewall/network settings

---

## Advanced Configuration

### Custom Regions

To deploy in a specific region:

```bash
fly regions set iad  # Washington DC
fly regions set ord  # Chicago
fly regions set lhr  # London
fly regions set nrt  # Tokyo
```

### Scaling

```bash
# Scale to 2 instances
fly scale count 2

# Scale memory
fly scale memory 512

# Scale CPU
fly scale vm shared-cpu-2x
```

### Health Checks

The bot doesn't need HTTP health checks, but you can add them to `fly.toml`:

```toml
[[services.http_checks]]
  interval = "10s"
  timeout = "2s"
  grace_period = "5s"
  method = "GET"
  path = "/health"
```

### Persistent Storage

If you need persistent storage for `settings.json`:

```bash
# Create a volume
fly volumes create data --size 1 --region iad

# Mount it in fly.toml
[mounts]
  source = "data"
  destination = "/data"
```

Then update `bot.py` to use `/data/settings.json`.

---

## Cost Considerations

### Free Tier

Fly.io offers:
- **3 shared-cpu-1x VMs** with **256MB RAM** each
- **3GB persistent volume storage**
- **160GB outbound data transfer**

This is usually enough for a Discord bot!

### Pricing

If you exceed the free tier:
- **$1.94/month** per VM (shared-cpu-1x, 256MB)
- **$0.15/GB** for additional storage
- **$0.02/GB** for additional bandwidth

### Monitor Usage

```bash
fly dashboard
```

Visit your dashboard to see usage and costs.

---

## Security Best Practices

### 1. Never Commit Secrets

✅ **DO:**
- Use `fly secrets set` for sensitive data
- Keep `.env` in `.gitignore`

❌ **DON'T:**
- Commit `.env` files
- Hardcode tokens in code
- Share tokens publicly

### 2. Use Environment Variables

Always use environment variables for sensitive data:

```python
import os
TOKEN = os.getenv('DISCORD_TOKEN')
```

### 3. Regular Updates

Keep your dependencies updated:

```bash
pip install --upgrade discord.py python-dotenv
pip freeze > requirements.txt
fly deploy
```

### 4. Monitor Logs

Regularly check logs for suspicious activity:

```bash
fly logs | grep -i error
```

---

## Quick Reference Commands

```bash
# Deploy
fly deploy

# View logs
fly logs

# Check status
fly status

# Restart app
fly apps restart your-bot-name

# Set secret
fly secrets set KEY=value

# List secrets
fly secrets list

# Remove secret
fly secrets unset KEY

# Scale
fly scale count 1

# SSH into app
fly ssh console

# Open dashboard
fly dashboard
```

---

## Step-by-Step Checklist

- [ ] Install Fly CLI
- [ ] Login to Fly.io (`fly auth login`)
- [ ] Update `fly.toml` with unique app name
- [ ] Create Fly.io app (`fly launch` or `fly apps create`)
- [ ] Set Discord token secret (`fly secrets set DISCORD_TOKEN=...`)
- [ ] Deploy bot (`fly deploy`)
- [ ] Check logs (`fly logs`)
- [ ] Verify bot is online in Discord
- [ ] Test commands (`!help_bot`)
- [ ] Set minimum instances (`fly scale count 1`)
- [ ] Monitor bot for 24 hours

---

## Need Help?

### Fly.io Resources
- **Documentation:** https://fly.io/docs
- **Community:** https://community.fly.io
- **Status:** https://status.fly.io

### Discord Bot Resources
- **Discord Developer Portal:** https://discord.com/developers/applications
- **discord.py Documentation:** https://discordpy.readthedocs.io

### Common Issues
1. Check Fly.io status page
2. Review Fly.io community forums
3. Check Discord.py documentation
4. Review your logs: `fly logs`

---

## Example: Complete Deployment Session

```bash
# 1. Install Fly CLI (if not installed)
iwr https://fly.io/install.ps1 -useb | iex

# 2. Login
fly auth login

# 3. Create app
fly launch
# Answer prompts:
# - App name: my-discord-bot-123
# - Region: iad
# - PostgreSQL: No
# - Redis: No
# - Deploy now: No

# 4. Set token
fly secrets set DISCORD_TOKEN=your_token_here

# 5. Deploy
fly deploy

# 6. Watch logs
fly logs

# 7. Verify
fly status

# 8. Set to always run
fly scale count 1

# Done! Bot should be online in Discord
```

---

**🎉 Congratulations!** Your Discord bot is now running on Fly.io and will stay online 24/7!
