# How to Test Your Discord Bot

Follow these steps to verify your bot is working correctly:

## Step 1: Check Bot is Online

1. **Run the bot:**
   ```bash
   python bot.py
   ```

2. **Look for this message in the console:**
   ```
   YourBotName#1234 has logged in!
   Bot is in X servers
   ```
   ✅ If you see this, the bot is online!

3. **Check Discord:**
   - Go to your Discord server
   - Look at the member list - your bot should appear with a green "Online" status
   - The bot's status should say "Managing voice channels"

## Step 2: Test Basic Commands

1. **In any text channel, type:**
   ```
   !help_bot
   ```
   ✅ You should see a message with all available commands

2. **Check settings:**
   ```
   !settings
   ```
   ✅ You should see the current bot settings

## Step 3: Enable the Bot for Your Server

1. **Type in a text channel (you must be an admin):**
   ```
   !enable
   ```
   ✅ Bot should reply: "✅ Auto-mute and camera-off enabled for this server!"

## Step 4: Test Auto-Mute Feature

1. **Join a voice channel** (use your own account or ask a friend)
2. **Wait 2-3 seconds**
3. ✅ **You should be automatically muted** (your microphone icon should be crossed out)

## Step 5: Test Admin Commands

### Test Mute/Unmute:
1. **Make sure you're in a voice channel**
2. **Type:**
   ```
   !mute @YourUsername
   ```
   ✅ You should be muted and see a confirmation message

3. **Type:**
   ```
   !unmute @YourUsername
   ```
   ✅ You should be unmuted and see a confirmation message

### Test Camera On/Off:
1. **While in a voice channel, type:**
   ```
   !camoff @YourUsername
   ```
   ✅ You should be muted (camera/audio off) and see a confirmation

2. **Type:**
   ```
   !camon @YourUsername
   ```
   ✅ You should be unmuted (camera/audio on) and see a confirmation

## Step 6: Test Settings Toggle

1. **Toggle auto-mute:**
   ```
   !toggle_automute
   ```
   ✅ Should show "✅ Auto-mute enabled/disabled."

2. **Toggle auto camera-off:**
   ```
   !toggle_autocam
   ```
   ✅ Should show "✅ Auto camera-off enabled/disabled."

3. **Check settings again:**
   ```
   !settings
   ```
   ✅ Should show updated settings

## Troubleshooting Checklist

### Bot Not Responding?
- [ ] Is the bot online? (Check member list)
- [ ] Did you use the correct prefix `!`?
- [ ] Do you have admin permissions?
- [ ] Check console for error messages

### Auto-Mute Not Working?
- [ ] Did you run `!enable` first?
- [ ] Is the bot role above member roles in server settings?
- [ ] Does the bot have "Mute Members" permission?
- [ ] Check console for permission errors

### Commands Not Working?
- [ ] Are you typing in a text channel (not voice)?
- [ ] Do you have Administrator role?
- [ ] Is the bot online and connected?
- [ ] Check for typos in command names

## Quick Test Script

Run these commands in order in your Discord server:

```
1. !help_bot          → Should show command list
2. !settings          → Should show current settings
3. !enable            → Should enable bot
4. [Join voice channel] → Should auto-mute you
5. !unmute @Yourself  → Should unmute you
6. !camoff @Yourself  → Should mute you again
7. !camon @Yourself   → Should unmute you
8. !settings          → Should show enabled status
```

## Expected Console Output

When everything works, you should see messages like:
```
YourBotName#1234 has logged in!
Bot is in 1 servers
Auto-muted YourName in ServerName
```

If you see errors, they'll appear in the console and help identify the issue.
