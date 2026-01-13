# How to Assign Admin Permissions - Complete Guide

Admins can now assign admin permissions to other members! This is perfect when you give the bot to someone on another server - they can assign themselves or others as admins.

## 🎯 Quick Start

### Step 1: Assign Admin to Someone

Type in Discord (as Discord admin):
```
!assign_admin @username
```

**Example:**
```
!assign_admin @John
```
Bot will reply: ✅ **@John is now an assigned admin!**

### Step 2: Check Assigned Admins

Type:
```
!assigned_admins
```

This shows all members with admin permissions.

### Step 3: Remove Admin Permissions

Type:
```
!unassign_admin @username
```

**Example:**
```
!unassign_admin @John
```
Bot will reply: ❌ **@John has been removed from assigned admins.**

---

## 📋 All Commands

### Discord Admin Commands (Only Discord Admins Can Use)

| Command | What It Does |
|---------|--------------|
| `!assign_admin @member` | Give admin permissions to member |
| `!unassign_admin @member` | Remove admin permissions from member |
| `!assigned_admins` | Show all assigned admins |

### Commands That Assigned Admins Can Use

Once assigned, they can use **ALL admin commands**:

| Command | What It Does |
|---------|--------------|
| `!settings` | View bot settings |
| `!toggle_automute` | Turn auto-mute on/off |
| `!toggle_autocam` | Turn auto camera-off on/off |
| `!enable` | Enable bot |
| `!disable` | Disable bot |
| `!allow @member` | Allow member to use mute/camera commands |
| `!remove @member` | Remove member from allowed list |
| `!allowed` | Show all allowed members |
| `!mute @member` | Mute someone |
| `!unmute @member` | Unmute someone |
| `!camon @member` | Turn camera on |
| `!camoff @member` | Turn camera off |

---

## 💡 Examples

### Example 1: Assign Admin to Someone on Another Server

**Scenario:** You give the bot to someone on their server, and they want to use admin commands.

```
Discord Admin: !assign_admin @ServerOwner
Bot: ✅ @ServerOwner is now an assigned admin!
     They can now use all admin commands:
     • !settings - View settings
     • !toggle_automute - Toggle auto-mute
     • !toggle_autocam - Toggle auto camera-off
     • !enable / !disable - Enable/disable bot
     • !allow / !remove - Manage allowed members
     • All mute/camera commands

ServerOwner can now:
- Use !settings to configure the bot
- Use !toggle_automute to customize
- Use !allow to give permissions to others
- Everything an admin can do!
```

### Example 2: Assign Multiple Admins

```
Discord Admin: !assign_admin @John
Discord Admin: !assign_admin @Sarah
Discord Admin: !assign_admin @Mike

Discord Admin: !assigned_admins
Bot: Shows list of all assigned admins
```

### Example 3: Remove Admin Permissions

```
Discord Admin: !unassign_admin @John
Bot: ❌ @John has been removed from assigned admins.
     They can no longer use admin commands (unless they are Discord admin).
```

---

## ✅ How It Works

### Permission Levels:

1. **Discord Admins** - Always have full access (can assign others)
2. **Assigned Admins** - Have full admin access (can't assign others)
3. **Allowed Members** - Can only use mute/camera commands
4. **Regular Members** - Cannot use any commands

### Who Can Do What?

| User Type | Can Assign Admins? | Can Use Admin Commands? | Can Use Mute/Camera? |
|-----------|-------------------|------------------------|---------------------|
| Discord Admin | ✅ Yes | ✅ Yes | ✅ Yes |
| Assigned Admin | ❌ No | ✅ Yes | ✅ Yes |
| Allowed Member | ❌ No | ❌ No | ✅ Yes |
| Regular Member | ❌ No | ❌ No | ❌ No |

---

## 🎮 Step-by-Step Example

### Scenario: Give Bot to Someone on Another Server

1. **They add the bot to their server**

2. **They assign themselves as admin:**
   ```
   !assign_admin @Themselves
   ```

3. **Now they can:**
   - Type `!settings` to configure
   - Type `!toggle_automute` to customize
   - Type `!allow @someone` to give permissions
   - Use all admin commands!

4. **They can assign others too:**
   ```
   !assign_admin @Helper
   ```

5. **To check who has admin:**
   ```
   !assigned_admins
   ```

---

## 📊 View Assigned Admins in Settings

Type:
```
!settings
```

This shows:
- Current bot settings
- List of assigned admins
- List of allowed members
- How to manage them

---

## 🔄 Difference: Assigned Admin vs Allowed Member

### Assigned Admin:
- ✅ Can use **ALL** admin commands
- ✅ Can change settings
- ✅ Can manage allowed members
- ✅ Can enable/disable bot
- ❌ Cannot assign other admins (only Discord admins can)

### Allowed Member:
- ✅ Can use mute/camera commands only
- ❌ Cannot change settings
- ❌ Cannot manage others
- ❌ Cannot enable/disable bot

---

## ❓ Troubleshooting

### "Only Discord administrators can assign admin permissions"
- You need to be a Discord server administrator
- Check your role permissions
- Only Discord admins can assign others

### "Member not found"
- Make sure you're using `@username` or mention them
- Check the member is in the server
- Try typing their name without @ first

### "Already an assigned admin"
- Member is already in the assigned admins list
- Use `!assigned_admins` to see the list
- Use `!unassign_admin` first if you want to re-add them

### "Command not working for assigned admin"
- Check they're actually in the assigned admins list with `!assigned_admins`
- Make sure they're typing the command correctly
- Verify bot has permissions

---

## 💬 Quick Reference

```
Assign admin:        !assign_admin @username
Remove admin:         !unassign_admin @username
Show assigned:       !assigned_admins
View settings:        !settings
```

---

## 🎯 Use Cases

### Use Case 1: Bot on Multiple Servers
**Problem:** You give bot to someone on another server, they need admin access.

**Solution:**
```
They: !assign_admin @Themselves
Now: They can manage the bot on their server!
```

### Use Case 2: Delegate Admin Tasks
**Problem:** You want someone to help manage the bot but not make them Discord admin.

**Solution:**
```
You: !assign_admin @Helper
Now: Helper can use all admin commands without being Discord admin!
```

### Use Case 3: Temporary Admin Access
**Problem:** Someone needs admin access temporarily.

**Solution:**
```
You: !assign_admin @TemporaryAdmin
[They do their work]
You: !unassign_admin @TemporaryAdmin
Done!
```

---

## 🎯 Tips

1. **Only Discord admins can assign others** - This prevents abuse
2. **Assigned admins can't assign others** - Only Discord admins can
3. **Check `!assigned_admins` regularly** to see who has access
4. **Use `!settings`** to see both assigned admins and allowed members
5. **Each server has its own list** - Settings are per-server
