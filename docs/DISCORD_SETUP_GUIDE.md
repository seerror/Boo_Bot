# How to Add Bot to Discord - Step by Step Guide

Follow these steps to create and add your bot to Discord:

## Step 1: Create a Discord Application

1. **Go to Discord Developer Portal:**
   - Open your browser and visit: https://discord.com/developers/applications
   - **Log in** with your Discord account

2. **Create New Application:**
   - Click the **"New Application"** button (top right)
   - Give it a name (e.g., "Auto Mute Bot")
   - Click **"Create"**

## Step 2: Create the Bot

1. **Go to Bot Section:**
   - In the left sidebar, click **"Bot"**
   - Click **"Add Bot"** button
   - Click **"Yes, do it!"** to confirm

2. **Enable Privileged Gateway Intents:**
   - Scroll down to **"Privileged Gateway Intents"**
   - Enable these two options:
     - ✅ **SERVER MEMBERS INTENT** (Required to see members)
     - ✅ **MESSAGE CONTENT INTENT** (Required to read commands)
   - Click **"Save Changes"**

3. **Copy Your Bot Token:**
   - Under **"Token"** section, click **"Reset Token"** or **"Copy"**
   - ⚠️ **IMPORTANT:** Save this token somewhere safe! You'll need it in Step 4
   - ⚠️ **NEVER share this token publicly!**

## Step 3: Invite Bot to Your Server

1. **Go to OAuth2 Section:**
   - Click **"OAuth2"** in the left sidebar
   - Click **"URL Generator"** (under OAuth2)

2. **Select Scopes:**
   - Check these boxes:
     - ✅ **bot**
     - ✅ **applications.commands** (optional, for slash commands)

3. **Select Bot Permissions:**
   - Scroll down to **"Bot Permissions"**
   - Check these permissions:
     - ✅ **Manage Channels**
     - ✅ **Mute Members**
     - ✅ **Deafen Members**
     - ✅ **Move Members**
     - ✅ **Send Messages**
     - ✅ **Read Message History**
     - ✅ **Use External Emojis** (optional)

4. **Copy and Use the Invite URL:**
   - Scroll to the bottom
   - You'll see a **"Generated URL"**
   - **Copy this URL**
   - **Open it in a new browser tab**
   - Select the Discord server where you want to add the bot
   - Click **"Authorize"**
   - Complete any CAPTCHA if prompted

5. **Verify Bot is Added:**
   - Go to your Discord server
   - Check the member list - your bot should appear (but might be offline)

## Step 4: Configure Bot Token in Your Code

1. **Create .env file:**
   - In your project folder (`boo bot`), create a new file named `.env`
   - **OR** copy `env_example.txt` and rename it to `.env`

2. **Add your token:**
   - Open the `.env` file
   - Add this line (replace with your actual token):
   ```
   DISCORD_TOKEN=your_actual_bot_token_here
   ```
   - Example:
   ```
   DISCORD_TOKEN=MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.GaBcDe.FgHiJkLmNoPqRsTuVwXyZaBcDeFgHiJkLmNoPqRsTu
   ```
   - **Save the file**

## Step 5: Set Bot Role Permissions

1. **In Discord Server:**
   - Go to **Server Settings** → **Roles**
   - Find your bot's role (usually named after your bot)
   - Make sure the bot role is **above** regular member roles
   - The bot needs to be higher in the hierarchy to mute members

2. **Check Channel Permissions:**
   - Go to any voice channel
   - Right-click → **Edit Channel** → **Permissions**
   - Make sure the bot role has:
     - ✅ **Connect** permission
     - ✅ **Mute Members** permission
     - ✅ **Deafen Members** permission

## Step 6: Run the Bot

1. **Install dependencies** (if not done already):
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the bot:**
   ```bash
   python bot.py
   ```

3. **Check for success:**
   - You should see in the console:
     ```
     YourBotName#1234 has logged in!
     Bot is in 1 servers
     ```
   - In Discord, the bot should now show as **"Online"** (green status)

## Step 7: Test the Bot

1. **In any text channel, type:**
   ```
   !help_bot
   ```
   - You should see a list of commands

2. **Enable the bot:**
   ```
   !enable
   ```
   - You should see: "✅ Auto-mute and camera-off enabled for this server!"

3. **Test auto-mute:**
   - Join a voice channel
   - Wait 2-3 seconds
   - You should be automatically muted!

## Troubleshooting

### Bot shows as offline?
- Check if `python bot.py` is running
- Check console for error messages
- Verify your token is correct in `.env` file

### "Invalid token" error?
- Make sure there are no extra spaces in your `.env` file
- Token should be on one line: `DISCORD_TOKEN=your_token`
- Try resetting the token in Discord Developer Portal

### Bot can't mute members?
- Make sure bot role is above member roles
- Check that bot has "Mute Members" permission
- Verify you ran `!enable` command first

### Commands not working?
- Make sure you have Administrator permissions
- Check that bot has "Send Messages" permission
- Verify the command prefix is `!`

## Quick Checklist

- [ ] Created Discord application
- [ ] Created bot and enabled intents
- [ ] Copied bot token
- [ ] Invited bot to server with correct permissions
- [ ] Created `.env` file with token
- [ ] Set bot role above member roles
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Ran the bot (`python bot.py`)
- [ ] Bot shows as online in Discord
- [ ] Tested `!help_bot` command
- [ ] Ran `!enable` command
- [ ] Tested auto-mute by joining voice channel

## Need Help?

If you encounter issues:
1. Check the console output for error messages
2. Verify all permissions are set correctly
3. Make sure the bot token is correct
4. Ensure Python and all dependencies are installed
