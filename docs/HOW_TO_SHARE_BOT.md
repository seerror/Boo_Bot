# How to Share Your Bot with Others

This guide explains how to create a shareable invite link so anyone can add your bot to their Discord server.

## Step 1: Create the Invite Link

1. **Go to Discord Developer Portal:**
   - Visit: https://discord.com/developers/applications
   - Log in with your Discord account

2. **Select Your Bot Application:**
   - Click on your bot application (the one you created)

3. **Go to OAuth2 Settings:**
   - In the left sidebar, click **"OAuth2"**
   - Click **"URL Generator"** (under OAuth2 section)

4. **Select Scopes:**
   - Check these boxes:
     - ✅ **bot** (Required)
     - ✅ **applications.commands** (Optional, for slash commands)

5. **Select Bot Permissions:**
   - Scroll down to **"Bot Permissions"**
   - Check these permissions:
     - ✅ **Manage Channels**
     - ✅ **Mute Members**
     - ✅ **Deafen Members**
     - ✅ **Move Members**
     - ✅ **Send Messages**
     - ✅ **Read Message History**
     - ✅ **Use External Emojis** (Optional)

6. **Copy the Generated URL:**
   - Scroll to the bottom of the page
   - You'll see a **"Generated URL"** that looks like:
     ```
     https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_ID&permissions=PERMISSIONS&scope=bot%20applications.commands
     ```
   - **Copy this entire URL** - this is your shareable invite link!

## Step 2: Share the Link

You can share this link in several ways:

### Option 1: Direct Link
- Share the URL directly with anyone
- They can click it to add the bot to their server

### Option 2: Create a Simple Website
- Create a simple HTML page with the invite link
- Host it on GitHub Pages, Netlify, or similar

### Option 3: Share in Discord
- Post the link in a Discord channel
- Anyone with the link can add the bot to their server

### Option 4: Create a QR Code
- Use a QR code generator to create a QR code from the URL
- People can scan it with their phone to add the bot

## Step 3: What Others Need to Do

When someone clicks your invite link:

1. **They'll see a Discord authorization page**
2. **They select their Discord server** from a dropdown
3. **They click "Authorize"**
4. **They complete any CAPTCHA** if prompted
5. **The bot is added to their server!**

## Important Notes

### ⚠️ Bot Must Be Running
- The bot must be running (`python bot.py`) for it to appear online
- If the bot is offline, it won't work even if added to the server

### ⚠️ Server Admin Requirements
- The person adding the bot must have **"Manage Server"** permission
- Regular members cannot add bots to servers

### ⚠️ Bot Role Position
After adding the bot, server admins should:
1. Go to **Server Settings** → **Roles**
2. Find the bot's role
3. Drag it **above** regular member roles
4. This is required for the bot to mute members

## Example Invite Link Format

Your invite link will look something like this:
```
https://discord.com/api/oauth2/authorize?client_id=123456789012345678&permissions=36703232&scope=bot%20applications.commands
```

## Quick Share Template

You can copy and customize this message to share with others:

```
🤖 Invite [Your Bot Name] to Your Server!

Click this link to add the bot:
[PASTE YOUR INVITE URL HERE]

Features:
✅ Auto-mutes members when they join voice channels
✅ Admin controls for camera/audio
✅ Easy to use commands

After adding:
1. Make sure bot role is above member roles (Server Settings → Roles)
2. Bot works automatically - no setup needed!
3. Use !help_bot to see all commands

The bot must be online for it to work. If it's offline, contact the bot owner.
```

## Troubleshooting

### "Invalid Invite" Error?
- Make sure your bot application exists in Discord Developer Portal
- Verify the bot token is correct
- Check that the bot hasn't been deleted

### Bot Appears Offline?
- The bot must be running on your computer/server
- Check if `python bot.py` is running
- Verify the bot token in `.env` file is correct

### Bot Can't Mute Members?
- Server admin needs to move bot role above member roles
- Bot needs "Mute Members" permission (should be in invite link)
- Check server permissions in Server Settings

## Security Note

⚠️ **Never share your bot token!** Only share the invite link (OAuth2 URL). The token is secret and should only be in your `.env` file.
