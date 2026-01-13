# What is `!allow <member>` Command?

## Quick Answer

The `!allow <member>` command gives a specific member permission to use mute/camera commands without being an admin.

---

## 🎯 What It Does

**Command:**
```
!allow @username
```

**What happens:**
- ✅ Adds the member to the "allowed list"
- ✅ They can now use mute/camera commands
- ✅ They can control other members' voice/camera
- ❌ They still CANNOT change bot settings

---

## 📋 Example

### Step 1: Admin Allows a Member

```
Admin: !allow @John
Bot: ✅ @John is now allowed to use mute/unmute and camera commands!
     They can now use: !mute, !unmute, !camon, !camoff
```

### Step 2: John Can Now Use Commands

```
John: !mute @Sarah
Bot: 🔇 Muted @Sarah

John: !unmute @Sarah
Bot: 🔊 Unmuted @Sarah

John: !camoff @Mike
Bot: ✅ Camera/audio disabled for @Mike
```

### Step 3: What John CANNOT Do

```
John: !settings
Bot: ❌ You do not have permission to use this command.

John: !toggle_automute
Bot: ❌ You do not have permission to use this command.
```

---

## 🔐 Permission Levels Explained

### Level 1: Discord Admin
- ✅ Can use **ALL** commands
- ✅ Can change settings
- ✅ Can assign admins
- ✅ Can allow/remove members

### Level 2: Assigned Admin
- ✅ Can use **ALL** admin commands
- ✅ Can change settings
- ✅ Can allow/remove members
- ❌ Cannot assign other admins

### Level 3: Allowed Member (from `!allow`)
- ✅ Can use **mute/camera commands only**
  - `!mute @member`
  - `!unmute @member`
  - `!camon @member`
  - `!camoff @member`
  - `!voiceonly @member`
  - `!videooff @member`
  - `!videoon @member`
- ❌ Cannot change settings
- ❌ Cannot manage allowed members
- ❌ Cannot enable/disable bot

### Level 4: Regular Member
- ❌ Cannot use any commands (except `!help_bot`)

---

## 💡 Why Use This Command?

### Use Case 1: Helper/Moderator
**Scenario:** You want someone to help manage voice channels, but not give them full admin.

```
Admin: !allow @Helper
Now Helper can:
- Mute/unmute people
- Control cameras
- Help manage voice channels
But cannot:
- Change bot settings
- Break anything important
```

### Use Case 2: Trusted Member
**Scenario:** You trust someone to control voice, but don't want them changing settings.

```
Admin: !allow @TrustedMember
TrustedMember can help with voice control without admin access.
```

### Use Case 3: Multiple Helpers
**Scenario:** You have several helpers who need to control voice.

```
Admin: !allow @Helper1
Admin: !allow @Helper2
Admin: !allow @Helper3

All three can now use mute/camera commands!
```

---

## 📊 Commands Allowed Members Can Use

Once added with `!allow`, they can use:

| Command | What It Does |
|---------|-------------|
| `!mute @member` | Mute someone |
| `!unmute @member` | Unmute someone |
| `!camon @member` | Turn camera/audio on |
| `!camoff @member` | Turn camera/audio off |
| `!voiceonly @member` | Enable voice, disable video |
| `!videooff @member` | Turn video off, keep voice |
| `!videoon @member` | Enable voice |

**They CANNOT use:**
- `!settings` ❌
- `!toggle_automute` ❌
- `!toggle_autocam` ❌
- `!enable` / `!disable` ❌
- `!allow` / `!remove` ❌
- `!assign_admin` ❌

---

## 🔄 How to Remove Someone

If you want to remove someone from the allowed list:

```
Admin: !remove @John
Bot: ❌ @John has been removed from the allowed list.
     They can no longer use mute/camera commands (unless they are admin).
```

---

## 📋 Complete Example

### Scenario: Setting Up a Helper

```
1. Admin: !allow @Helper
   Bot: ✅ @Helper is now allowed to use mute/unmute and camera commands!

2. Helper: !mute @NoisyMember
   Bot: 🔇 Muted @NoisyMember
   ✅ Works! Helper can use the command.

3. Helper: !settings
   Bot: ❌ You do not have permission to use this command.
   ❌ Helper cannot change settings.

4. Admin: !remove @Helper
   Bot: ❌ @Helper has been removed from the allowed list.
   ❌ Helper can no longer use commands.
```

---

## 🎯 Difference: `!allow` vs `!assign_admin`

### `!allow @member`
- ✅ Can use mute/camera commands
- ❌ Cannot change settings
- ❌ Cannot manage others
- **Use for:** Helpers, moderators

### `!assign_admin @member`
- ✅ Can use ALL admin commands
- ✅ Can change settings
- ✅ Can manage allowed members
- **Use for:** Trusted admins, server managers

---

## ✅ Quick Summary

**`!allow @member`** = Give limited permissions (mute/camera only)
**`!assign_admin @member`** = Give full admin permissions

---

## 💬 Quick Reference

```
Allow member:      !allow @username
Remove member:     !remove @username
Show allowed:      !allowed
Check settings:    !settings (shows allowed members)
```

---

**In Simple Terms:** `!allow` gives someone permission to control voice/camera, but not to change bot settings. Perfect for helpers who need to mute people but shouldn't have full admin access!
