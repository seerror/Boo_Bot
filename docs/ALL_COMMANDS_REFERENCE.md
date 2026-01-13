# Complete Commands Reference

This document contains all available commands for the Discord Auto-Mute & Camera Control Bot.

**Command Prefix:** `!` (exclamation mark)

---

## 📋 Table of Contents

1. [Bot Control Commands](#bot-control-commands)
2. [Member Control Commands](#member-control-commands)
3. [Camera & Video Commands](#camera--video-commands)
4. [Admin Management Commands](#admin-management-commands)
5. [Permission Management Commands](#permission-management-commands)
6. [Information Commands](#information-commands)

---

## Bot Control Commands

### `!enable`
**Permission:** Admin or Assigned Admin only

**Description:** Enable auto-mute and camera-off features for this server.

**Usage:**
```
!enable
```

**What it does:**
- Enables the bot for the current server
- Members will be automatically muted when joining voice channels
- Camera/audio will be disabled by default

**Example Response:**
```
✅ Auto-mute and camera-off enabled for this server!
```

---

### `!disable`
**Permission:** Admin or Assigned Admin only

**Description:** Disable auto-mute and camera-off features for this server.

**Usage:**
```
!disable
```

**What it does:**
- Disables the bot for the current server
- Auto-mute and auto camera-off will stop working
- Manual commands will still work if you have permissions

**Example Response:**
```
❌ Auto-mute and camera-off disabled for this server.
```

---

### `!settings`
**Permission:** Admin or Assigned Admin only

**Description:** View current bot settings and configuration for this server.

**Usage:**
```
!settings
```

**What it shows:**
- Server status (enabled/disabled)
- Auto-mute status (on/off)
- Auto camera-off status (on/off)
- List of assigned admins
- List of allowed members
- Quick reference for customization commands

**Example Response:**
An embed showing all current settings with status indicators.

---

### `!toggle_automute`
**Permission:** Admin or Assigned Admin only

**Description:** Toggle the auto-mute feature on or off globally.

**Usage:**
```
!toggle_automute
```

**What it does:**
- Turns auto-mute ON if it's currently OFF
- Turns auto-mute OFF if it's currently ON
- Affects all servers where the bot is enabled

**Example Response:**
```
✅ Auto-mute is now enabled!
When enabled, members will be automatically muted when joining voice channels.
```

---

### `!toggle_autocam`
**Permission:** Admin or Assigned Admin only

**Description:** Toggle the auto camera-off feature on or off globally.

**Usage:**
```
!toggle_autocam
```

**What it does:**
- Turns auto camera-off ON if it's currently OFF
- Turns auto camera-off OFF if it's currently ON
- Affects all servers where the bot is enabled

**Example Response:**
```
✅ Auto camera-off is now enabled!
When enabled, members will have camera/audio disabled by default when joining voice.
```

---

## Member Control Commands

### `!mute <member>`
**Permission:** Admin or Allowed Member

**Description:** Mute a specific member in a voice channel.

**Usage:**
```
!mute @username
!mute @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to mute (e.g., `@username`)

**What it does:**
- Mutes the specified member if they're in a voice channel
- Member will not be able to speak until unmuted

**Example Response:**
```
🔇 Muted @JohnDoe
```

**Error Messages:**
- `❌ Member is not in a voice channel.` - The member must be in a voice channel
- `❌ No permission to mute this member.` - Bot lacks permissions
- `❌ You do not have permission to use this command.` - You need to be added with `!allow`

---

### `!unmute <member>`
**Permission:** Admin or Allowed Member

**Description:** Unmute a specific member in a voice channel.

**Usage:**
```
!unmute @username
!unmute @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to unmute (e.g., `@username`)

**What it does:**
- Unmutes the specified member if they're in a voice channel
- Member will be able to speak again

**Example Response:**
```
🔊 Unmuted @JohnDoe
```

**Error Messages:**
- `❌ Member is not in a voice channel.` - The member must be in a voice channel
- `❌ No permission to unmute this member.` - Bot lacks permissions
- `❌ You do not have permission to use this command.` - You need to be added with `!allow`

---

## Camera & Video Commands

### `!camon [member]`
**Permission:** Admin or Allowed Member

**Description:** Turn camera/audio on for yourself or a member.

**Usage:**
```
!camon              # Enable for yourself
!camon @username    # Enable for another member
```

**Parameters:**
- `[member]` - Optional. Mention a member (defaults to yourself if omitted)

**What it does:**
- Unmutes the member (enables audio)
- Enables camera/audio functionality
- If no member is specified, affects the command user

**Example Response:**
```
✅ Camera/audio enabled for @JohnDoe
```

**Error Messages:**
- `❌ Member is not in a voice channel.` - The member must be in a voice channel
- `❌ No permission to modify this member.` - Bot lacks permissions

---

### `!camoff [member]`
**Permission:** Admin or Allowed Member

**Description:** Turn camera/audio off for yourself or a member.

**Usage:**
```
!camoff             # Disable for yourself
!camoff @username   # Disable for another member
```

**Parameters:**
- `[member]` - Optional. Mention a member (defaults to yourself if omitted)

**What it does:**
- Mutes the member (disables audio)
- Disables camera/audio functionality
- If no member is specified, affects the command user

**Example Response:**
```
✅ Camera/audio disabled for @JohnDoe
```

**Error Messages:**
- `❌ Member is not in a voice channel.` - The member must be in a voice channel
- `❌ No permission to modify this member.` - Bot lacks permissions

---

### `!videoon [member]`
**Permission:** Admin or Allowed Member

**Description:** Enable voice for a member (they can manually turn on video if they want).

**Usage:**
```
!videoon            # Enable for yourself
!videoon @username  # Enable for another member
```

**Parameters:**
- `[member]` - Optional. Mention a member (defaults to yourself if omitted)

**What it does:**
- Unmutes the member (enables microphone)
- Allows the member to manually turn on their camera
- If no member is specified, affects the command user

**Example Response:**
```
✅ Voice enabled for @JohnDoe
💡 They can now turn on their camera manually if they want.
```

**Note:** Discord bots cannot directly control video cameras. This command enables voice, and the member can manually enable their camera.

---

### `!videooff [member]`
**Permission:** Admin or Allowed Member

**Description:** Turn video off but keep voice on for a member.

**Usage:**
```
!videooff            # Enable voice, disable video for yourself
!videooff @username  # Enable voice, disable video for another member
```

**Parameters:**
- `[member]` - Optional. Mention a member (defaults to yourself if omitted)

**What it does:**
- Unmutes the member (enables microphone)
- Requests the member to manually turn off their camera
- Sends a DM to the member asking them to turn off their camera
- If no member is specified, affects the command user

**Example Response:**
```
✅ Voice enabled for @JohnDoe
⚠️ Note: Discord API doesn't allow bots to directly control video cameras.
Please ask @JohnDoe to manually turn off their camera.
Their microphone is now enabled and they can speak.
```

**Note:** Discord bots cannot directly control video cameras. The bot will enable voice and request the member to manually turn off their camera.

---

### `!voiceonly [member]`
**Permission:** Admin or Allowed Member

**Description:** Enable voice but disable video for a member.

**Usage:**
```
!voiceonly            # Enable voice only for yourself
!voiceonly @username  # Enable voice only for another member
```

**Parameters:**
- `[member]` - Optional. Mention a member (defaults to yourself if omitted)

**What it does:**
- Unmutes the member (enables microphone)
- Requests the member to manually turn off their camera
- Sends a DM to the member with instructions
- If no member is specified, affects the command user

**Example Response:**
```
✅ Voice enabled for @JohnDoe
📹 Video: Please turn off your camera manually
🎤 Audio: Enabled - You can speak

⚠️ Note: Discord bots cannot directly control video cameras. 
Please ask @JohnDoe to manually turn off their camera.
```

**Note:** Discord bots cannot directly control video cameras. The bot will enable voice and request the member to manually turn off their camera.

---

## Admin Management Commands

### `!assign_admin <member>`
**Permission:** Discord Administrator only

**Description:** Assign admin permissions to a member (gives them access to all admin commands).

**Usage:**
```
!assign_admin @username
!assign_admin @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to make an assigned admin

**What it does:**
- Gives the member access to all admin commands
- They can use: `!settings`, `!toggle_automute`, `!toggle_autocam`, `!enable`, `!disable`, `!allow`, `!remove`
- They can also use all mute/camera commands
- Only Discord administrators can assign other admins

**Example Response:**
```
✅ @JohnDoe is now an assigned admin!
They can now use all admin commands:
• !settings - View settings
• !toggle_automute - Toggle auto-mute
• !toggle_autocam - Toggle auto camera-off
• !enable / !disable - Enable/disable bot
• !allow / !remove - Manage allowed members
• All mute/camera commands
```

**Error Messages:**
- `⚠️ @JohnDoe is already an assigned admin.` - Member already has admin permissions
- `ℹ️ @JohnDoe is already a Discord administrator.` - Member is already a Discord admin
- `❌ Only Discord administrators can assign admin permissions to others.` - You need Discord admin permissions

---

### `!unassign_admin <member>`
**Permission:** Discord Administrator only

**Description:** Remove admin permissions from an assigned admin.

**Usage:**
```
!unassign_admin @username
!unassign_admin @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to remove admin permissions from

**What it does:**
- Removes assigned admin permissions from the member
- They can no longer use admin commands (unless they're a Discord admin)
- They can still use commands if they're in the allowed members list

**Example Response:**
```
❌ @JohnDoe has been removed from assigned admins.
They can no longer use admin commands (unless they are Discord admin).
```

**Error Messages:**
- `⚠️ @JohnDoe is not an assigned admin.` - Member is not an assigned admin
- `❌ Only Discord administrators can remove admin permissions from others.` - You need Discord admin permissions

---

### `!assigned_admins`
**Permission:** Admin or Assigned Admin only

**Description:** Show all members who have been assigned admin permissions.

**Usage:**
```
!assigned_admins
```

**What it shows:**
- List of all assigned admins (members with admin permissions)
- Shows their mentions and display names
- Total count of assigned admins

**Example Response:**
An embed showing:
```
👑 Assigned Admins
Members with admin permissions:

• @JohnDoe (John Doe)
• @JaneSmith (Jane Smith)

Total: 2 assigned admin(s)
```

---

## Permission Management Commands

### `!allow <member>`
**Permission:** Admin or Assigned Admin only

**Description:** Allow a member to use mute/unmute and camera commands.

**Usage:**
```
!allow @username
!allow @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to allow

**What it does:**
- Adds the member to the allowed members list
- They can now use: `!mute`, `!unmute`, `!camon`, `!camoff`, `!videoon`, `!videooff`, `!voiceonly`
- They cannot use admin commands (unless they're admin or assigned admin)

**Example Response:**
```
✅ @JohnDoe is now allowed to use mute/unmute and camera commands!
They can now use: !mute, !unmute, !camon, !camoff
```

**Error Messages:**
- `⚠️ @JohnDoe is already allowed to use mute/camera commands.` - Member is already in the allowed list

---

### `!remove <member>`
**Permission:** Admin or Assigned Admin only

**Description:** Remove a member from the allowed list.

**Usage:**
```
!remove @username
!remove @JohnDoe
```

**Parameters:**
- `<member>` - Required. Mention the member you want to remove

**What it does:**
- Removes the member from the allowed members list
- They can no longer use mute/camera commands (unless they're admin or assigned admin)

**Example Response:**
```
❌ @JohnDoe has been removed from the allowed list.
They can no longer use mute/camera commands (unless they are admin).
```

**Error Messages:**
- `⚠️ @JohnDoe is not in the allowed list.` - Member is not in the allowed list

---

### `!allowed`
**Permission:** Admin or Assigned Admin only

**Description:** Show all members who are allowed to use mute/camera commands.

**Usage:**
```
!allowed
```

**What it shows:**
- List of all allowed members
- Shows their mentions and display names
- Total count of allowed members

**Example Response:**
An embed showing:
```
👥 Allowed Members
Members who can use mute/camera commands:

• @JohnDoe (John Doe)
• @JaneSmith (Jane Smith)

Total: 2 member(s)
```

---

## Information Commands

### `!help_bot`
**Permission:** Everyone

**Description:** Show all available commands and their categories.

**Usage:**
```
!help_bot
```

**What it shows:**
- Complete list of all commands organized by category
- Command descriptions
- Permission requirements for each category

**Example Response:**
An embed showing all commands grouped by:
- ⚙️ Customization Commands (Admin Only)
- 👥 Member Control Commands (Admin or Allowed Members)
- 👑 Admin Assignment Commands (Discord Admin Only)
- ➕ Member Permission Commands (Admin or Assigned Admin Only)
- 📖 Info Commands

---

## Permission Levels Summary

### 🔴 Discord Administrator
- Highest permission level
- Can use ALL commands
- Can assign/unassign admins
- Has full control over bot settings

### 🟡 Assigned Admin
- Assigned by Discord administrators using `!assign_admin`
- Can use all admin commands except assigning other admins
- Can manage allowed members
- Can control bot settings

### 🟢 Allowed Member
- Added by admins using `!allow`
- Can use mute/unmute and camera commands
- Cannot change bot settings
- Cannot manage permissions

### ⚪ Regular Member
- No special permissions
- Can only use `!help_bot`
- Cannot use any control commands

---

## Command Syntax Guide

### Required Parameters
- `<member>` - Must include a member mention (e.g., `@username`)
- Example: `!mute @JohnDoe`

### Optional Parameters
- `[member]` - Member mention is optional (defaults to yourself if omitted)
- Example: `!camon` (affects you) or `!camon @JohnDoe` (affects JohnDoe)

### Command Prefix
- All commands start with `!` (exclamation mark)
- Commands are case-insensitive
- Example: `!HELP_BOT` works the same as `!help_bot`

---

## Common Error Messages

### Permission Errors
- `❌ You do not have permission to use this command.` - You need admin/assigned admin permissions
- `❌ Only Discord administrators can...` - Only Discord admins can perform this action
- `❌ Ask an admin to add you to the allowed list with !allow <your_name>.` - You need to be added to allowed members

### Member Errors
- `❌ Member is not in a voice channel.` - The member must be in a voice channel
- `⚠️ @username is already...` - Member already has this permission/status

### Bot Permission Errors
- `❌ No permission to modify this member.` - Bot lacks Discord permissions
- `❌ No permission to mute this member.` - Bot cannot mute this member (check role hierarchy)

---

## Quick Reference

| Command | Permission | Description |
|---------|-----------|-------------|
| `!enable` | Admin/Assigned Admin | Enable bot for server |
| `!disable` | Admin/Assigned Admin | Disable bot for server |
| `!settings` | Admin/Assigned Admin | View bot settings |
| `!toggle_automute` | Admin/Assigned Admin | Toggle auto-mute on/off |
| `!toggle_autocam` | Admin/Assigned Admin | Toggle auto camera-off on/off |
| `!mute <member>` | Admin/Allowed | Mute a member |
| `!unmute <member>` | Admin/Allowed | Unmute a member |
| `!camon [member]` | Admin/Allowed | Enable camera/audio |
| `!camoff [member]` | Admin/Allowed | Disable camera/audio |
| `!videoon [member]` | Admin/Allowed | Enable voice |
| `!videooff [member]` | Admin/Allowed | Voice on, video off |
| `!voiceonly [member]` | Admin/Allowed | Voice only mode |
| `!assign_admin <member>` | Discord Admin | Assign admin permissions |
| `!unassign_admin <member>` | Discord Admin | Remove admin permissions |
| `!assigned_admins` | Admin/Assigned Admin | Show assigned admins |
| `!allow <member>` | Admin/Assigned Admin | Allow member to use commands |
| `!remove <member>` | Admin/Assigned Admin | Remove member from allowed list |
| `!allowed` | Admin/Assigned Admin | Show allowed members |
| `!help_bot` | Everyone | Show all commands |

---

## Notes

- **Bot must be online:** The bot must be running (`python bot.py`) for commands to work
- **Role hierarchy:** Bot role must be above member roles to mute members
- **Video limitations:** Discord bots cannot directly control video cameras. Video commands request manual action from members.
- **Auto-enable:** Bot automatically enables itself when added to a new server
- **Per-server settings:** Each server has independent settings and permissions

---

## Need Help?

- Use `!help_bot` in Discord for a quick command list
- Use `!settings` to view current configuration
- Check other documentation files in the `docs` folder for more detailed guides
