# Quick Start Guide - For Other Servers

This bot works **automatically** on any Discord server you add it to! No setup needed!

## For Server Owners (Adding the Bot)

### Step 1: Get the Bot Invite Link

Ask the bot owner for the invite link, or if you're setting it up:

1. Go to https://discord.com/developers/applications
2. Select your bot application
3. Go to **OAuth2** → **URL Generator**
4. Select: `bot` and `applications.commands`
5. Select permissions:
   - ✅ Mute Members
   - ✅ Deafen Members
   - ✅ Manage Channels
   - ✅ Send Messages
6. Copy the URL and share it

### Step 2: Add Bot to Your Server

1. Click the invite link
2. Select your server
3. Click **Authorize**
4. Complete CAPTCHA if needed

### Step 3: Set Bot Permissions

1. Go to **Server Settings** → **Roles**
2. Find your bot's role
3. Make sure it's **above** regular member roles
4. The bot needs to be higher to mute members

### Step 4: Done! 🎉

**The bot is now active!** It will automatically:
- ✅ Mute members when they join voice channels
- ✅ Work immediately - no commands needed!

## For Bot Owners (Sharing the Bot)

### What You Need to Share:

1. **The invite link** (from OAuth2 URL Generator)
2. **Instructions** to set bot role above members
3. **Command list** (optional - `!help_bot` works in-server)

### Bot Features:

- ✅ **Auto-works** - No `!enable` needed
- ✅ **Per-server settings** - Each server can configure independently
- ✅ **Admin controls** - Server admins can customize

## Commands (For Server Admins)

Once the bot is added, server admins can use:

- `!help_bot` - Show all commands
- `!settings` - View current settings
- `!disable` - Turn off auto-mute
- `!enable` - Turn on auto-mute
- `!camon @user` - Turn camera/audio on
- `!camoff @user` - Turn camera/audio off
- `!mute @user` - Mute someone
- `!unmute @user` - Unmute someone

## How It Works

1. **Bot joins server** → Automatically enabled ✅
2. **Member joins voice** → Automatically muted ✅
3. **Admin can control** → Use commands to customize ✅

## Troubleshooting

**Bot not muting?**
- Check bot role is above member roles
- Verify bot has "Mute Members" permission
- Check console for error messages

**Want to disable?**
- Use `!disable` command (admin only)
- Use `!enable` to turn it back on

**Bot offline?**
- Make sure the bot code is running
- Check the `.env` file has correct token
- Verify token is valid in Discord Developer Portal
