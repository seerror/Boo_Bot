# Discord Auto-Mute & Camera Control Bot

A Discord bot that automatically mutes members and disables camera/audio when they join a voice channel. Admins can control these settings and manually toggle camera/audio for members.

## Features

- 🤐 **Auto-mute**: Automatically mutes members when they join voice channels
- 📹 **Auto camera-off**: Automatically disables camera/audio for new members
- ⚙️ **Admin controls**: Admins can toggle camera on/off for any member
- 🎛️ **Auto-enabled**: Works automatically on any server - no setup needed!
- 📊 **Settings management**: View and modify bot settings per server

## Setup Instructions

### 1. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot" and confirm
5. Under "Privileged Gateway Intents", enable:
   - ✅ Server Members Intent
   - ✅ Message Content Intent
6. Copy the bot token (you'll need this later)
7. Go to "OAuth2" → "URL Generator"
8. Select scopes: `bot` and `applications.commands`
9. Select bot permissions:
   - ✅ Manage Channels
   - ✅ Mute Members
   - ✅ Deafen Members
   - ✅ Move Members
10. Copy the generated URL and open it in your browser to invite the bot to your server

### 2. Install Dependencies

Make sure you have Python 3.8 or higher installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Open `.env` and paste your bot token:
   ```
   DISCORD_TOKEN=your_actual_bot_token_here
   ```

### 4. Run the Bot

```bash
python bot.py
```

The bot should now be online! You'll see a confirmation message in the console.

**🎉 The bot automatically works on any server it's added to - no need to run `!enable`!**

## Commands

### Admin Commands

- `!enable` - Enable auto-mute and camera-off for this server
- `!disable` - Disable auto-mute and camera-off for this server
- `!camon [member]` - Turn camera/audio on for a member (defaults to yourself)
- `!camoff [member]` - Turn camera/audio off for a member (defaults to yourself)
- `!mute <member>` - Mute a specific member
- `!unmute <member>` - Unmute a specific member
- `!settings` - Show current bot settings
- `!toggle_automute` - Toggle auto-mute feature on/off
- `!toggle_autocam` - Toggle auto camera-off feature on/off
- `!help_bot` - Show all available commands

### Usage Examples

```
!help_bot                  # Show all commands
!camon @username           # Turn camera on for a user
!camoff @username          # Turn camera off for a user
!mute @username            # Mute a user
!unmute @username          # Unmute a user
!settings                  # Check current settings
!disable                   # Disable auto-mute (if needed)
!enable                    # Re-enable auto-mute
```

**Note:** The bot is automatically enabled when added to a server. You can use `!disable` if you want to turn it off temporarily.

## Important Notes

⚠️ **Discord API Limitations**: 
- Discord's API doesn't directly control video cameras, but we can control audio muting
- The bot uses muting as the closest equivalent to camera control
- Members can manually unmute themselves unless you have additional server permissions

⚠️ **Permissions Required**:
- The bot needs "Mute Members" permission in voice channels
- Make sure the bot role is placed above member roles in the server hierarchy
- The bot must have administrator permissions or specific voice channel permissions

## Troubleshooting

**Bot doesn't mute members:**
- Check that the bot has "Mute Members" permission
- Ensure the bot role is above member roles
- Verify the bot is enabled for your server with `!enable`

**Commands not working:**
- Make sure you have Administrator permissions
- Check that the bot has "Send Messages" permission
- Verify the command prefix is `!`

## File Structure

```
boo bot/
├── bot.py              # Main bot file
├── requirements.txt    # Python dependencies
├── .env               # Your bot token (create this)
├── .env.example       # Example environment file
├── settings.json      # Bot settings (auto-generated)
└── README.md          # This file
```

## License

This bot is provided as-is for educational and personal use.
