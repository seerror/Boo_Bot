# How to Customize the Bot - Complete Guide

This guide shows you exactly how to customize how the bot works on your server.

## 🎯 Quick Customization

### Step 1: Check Current Settings

Type in any text channel:
```
!settings
```

This shows you:
- ✅ If bot is enabled/disabled
- ✅ If auto-mute is on/off
- ✅ If auto camera-off is on/off

### Step 2: Customize Features

#### Turn Auto-Mute ON or OFF:
```
!toggle_automute
```
- **First time:** Turns auto-mute OFF (members won't be auto-muted)
- **Second time:** Turns auto-mute ON (members will be auto-muted)

#### Turn Auto Camera-Off ON or OFF:
```
!toggle_autocam
```
- **First time:** Turns auto camera-off OFF (camera/audio allowed)
- **Second time:** Turns auto camera-off ON (camera/audio disabled)

#### Turn Bot Completely OFF:
```
!disable
```
- Bot stops working completely
- No auto-muting, no commands work

#### Turn Bot Back ON:
```
!enable
```
- Bot starts working again
- Auto-mute and camera-off resume

## 📋 All Customization Options

### Option 1: Auto-Mute ON, Camera-Off ON (Default)
**What happens:** Members are muted and camera is off when joining voice
```
!toggle_automute    (if off, turn on)
!toggle_autocam     (if off, turn on)
```

### Option 2: Auto-Mute ON, Camera-Off OFF
**What happens:** Members are muted but can use camera/audio
```
!toggle_automute    (if off, turn on)
!toggle_autocam     (if on, turn off)
```

### Option 3: Auto-Mute OFF, Camera-Off ON
**What happens:** Members can speak but camera is off
```
!toggle_automute    (if on, turn off)
!toggle_autocam     (if off, turn on)
```

### Option 4: Everything OFF
**What happens:** Bot doesn't auto-mute or disable camera
```
!toggle_automute    (if on, turn off)
!toggle_autocam     (if on, turn off)
```

### Option 5: Bot Completely Disabled
**What happens:** Bot doesn't work at all
```
!disable
```

## 🎮 Examples

### Example 1: "I want members to join muted, but they can turn on camera"
```
!settings              (check current)
!toggle_automute       (make sure it's ON)
!toggle_autocam        (turn it OFF)
```

### Example 2: "I don't want auto-mute, but keep camera off"
```
!toggle_automute       (turn it OFF)
!toggle_autocam        (make sure it's ON)
```

### Example 3: "I want to disable the bot temporarily"
```
!disable
```
Then later:
```
!enable
```

## 🔍 How to Check Your Settings

After making changes, always check:
```
!settings
```

This shows you exactly what's enabled/disabled.

## 💡 Common Customization Scenarios

### Scenario 1: Meeting Server
**Goal:** Everyone joins muted, camera off
```
!toggle_automute    (ON)
!toggle_autocam     (ON)
```

### Scenario 2: Casual Voice Chat
**Goal:** People can join and talk, but camera off by default
```
!toggle_automute    (OFF)
!toggle_autocam     (ON)
```

### Scenario 3: Free Voice Chat
**Goal:** No restrictions, people can join and do whatever
```
!toggle_automute    (OFF)
!toggle_autocam     (OFF)
```

### Scenario 4: Strict Control
**Goal:** Everyone muted, camera off, admins control everything
```
!toggle_automute    (ON)
!toggle_autocam     (ON)
!disable            (if you want to stop it completely)
```

## 🛠️ Manual Control Commands

Even with auto-features, admins can manually control members:

### Mute/Unmute Specific People:
```
!mute @username
!unmute @username
```

### Turn Camera On/Off for Specific People:
```
!camoff @username    (turn camera off)
!camon @username     (turn camera on)
```

### Control Yourself:
```
!camoff              (no @username needed)
!camon               (no @username needed)
```

## ❓ Troubleshooting Customization

### "Commands not working?"
- Make sure you have **Administrator** permissions
- Check that bot is online (green status)
- Make sure you're typing in a text channel

### "Settings not saving?"
- Check console for errors
- Make sure bot has permission to write files
- Try `!settings` to verify

### "Auto-mute not working after I enabled it?"
- Check `!settings` to confirm it's ON
- Make sure bot role is above member roles
- Verify bot has "Mute Members" permission

### "I want to reset everything to default"
```
!enable
!toggle_automute    (make sure ON)
!toggle_autocam     (make sure ON)
```

## 📊 Settings Reference

| Setting | What It Does | Default |
|---------|--------------|---------|
| Auto Mute | Mutes members when joining voice | ✅ ON |
| Auto Camera Off | Disables camera/audio by default | ✅ ON |
| Server Status | Bot enabled for this server | ✅ ON |

## 🎯 Quick Reference Card

```
View Settings:     !settings
Toggle Auto-Mute:  !toggle_automute
Toggle Auto-Cam:   !toggle_autocam
Enable Bot:        !enable
Disable Bot:       !disable
Help:              !help_bot
```

## 💬 Need More Help?

1. Type `!help_bot` in Discord for command list
2. Type `!settings` to see current configuration
3. Check console output for error messages
