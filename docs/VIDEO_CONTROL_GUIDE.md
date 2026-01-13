# 📹 Video Control Guide - Camera Off, Voice On

## Can I Turn Off Camera But Keep Voice On?

**Short Answer:** Yes, but with a limitation.

**Discord API Limitation:** Discord bots cannot directly control video cameras. However, the bot can:
- ✅ Enable voice (unmute the member)
- ✅ Send a notification asking them to turn off their camera
- ❌ Cannot force the camera off automatically

---

## 🎯 Commands Available

### Command 1: `!voiceonly`
**Enable voice but disable video**

```
!voiceonly @username
```

**What it does:**
- ✅ Unmutes the member (voice enabled)
- ✅ Sends them a DM asking to turn off camera
- ✅ Notifies you in the channel

**Example:**
```
You: !voiceonly @John
Bot: ✅ Voice enabled for @John
     📹 Video: Please turn off your camera manually
     🎤 Audio: Enabled - You can speak
     
     Note: Discord bots cannot directly control video cameras.
     Please ask @John to manually turn off their camera.
```

---

### Command 2: `!videooff`
**Turn video off, keep voice on**

```
!videooff @username
```

**What it does:**
- ✅ Enables voice (unmutes)
- ✅ Sends notification to member
- ✅ Same as `!voiceonly`

---

### Command 3: `!videoon`
**Enable voice (member can turn video on)**

```
!videoon @username
```

**What it does:**
- ✅ Enables voice (unmutes)
- ✅ Member can manually turn on video if they want

---

## 💡 How It Works

### Step 1: Admin Uses Command
```
Admin: !voiceonly @John
```

### Step 2: Bot Actions
1. Bot unmutes John (voice enabled)
2. Bot sends DM to John: "Please turn off your camera"
3. Bot confirms in channel

### Step 3: Member Action
- John receives DM notification
- John manually turns off their camera
- John can now speak (voice on) but camera is off

---

## 📋 Complete Example

### Scenario: Meeting with Voice Only

```
Admin: !voiceonly @Sarah
Bot: ✅ Voice enabled for @Sarah
     📹 Video: Please turn off your camera manually
     🎤 Audio: Enabled - You can speak
     
     Note: Discord bots cannot directly control video cameras.
     Please ask @Sarah to manually turn off their camera.

Sarah receives DM:
👋 Hello! An admin has enabled your microphone.
Please turn off your camera manually while keeping your microphone on.
You can speak, but please disable your video camera.

Sarah: [Turns off camera manually]
Result: ✅ Voice ON, Camera OFF
```

---

## ⚠️ Important Notes

### What the Bot CAN Do:
- ✅ Enable/disable voice (mute/unmute)
- ✅ Send notifications to members
- ✅ Request members to turn off camera

### What the Bot CANNOT Do:
- ❌ Force camera off automatically
- ❌ Directly control video cameras
- ❌ Turn camera on/off without member action

### Why?
Discord's API doesn't allow bots to directly control video cameras. This is a Discord limitation, not a bot limitation.

---

## 🎯 Use Cases

### Use Case 1: Meeting with Voice Only
**Goal:** Everyone can speak, but no cameras

```
1. !voiceonly @Member1
2. !voiceonly @Member2
3. !voiceonly @Member3
```

Each member gets notified to turn off their camera.

---

### Use Case 2: Presentation Mode
**Goal:** Presenter has camera, audience has voice only

```
1. !camon @Presenter        # Presenter has camera
2. !voiceonly @Audience1    # Audience voice only
3. !voiceonly @Audience2    # Audience voice only
```

---

### Use Case 3: Privacy Mode
**Goal:** Some members want voice but not video

```
1. !voiceonly @PrivateMember
```

They get notified and can choose to turn off camera.

---

## 🔄 Alternative: Manual Control

If you want more control, you can:

1. **Use `!unmute`** to enable voice
2. **Manually ask** members to turn off camera
3. **Use server rules** to enforce camera-off policy

---

## ❓ FAQ

### Q: Can the bot force camera off?
**A:** No, Discord API doesn't allow this. Members must turn it off manually.

### Q: Will members be notified?
**A:** Yes, the bot sends a DM asking them to turn off their camera.

### Q: What if member doesn't turn off camera?
**A:** You'll need to remind them manually. The bot cannot enforce it.

### Q: Can I use this for multiple members?
**A:** Yes, use the command for each member:
```
!voiceonly @Member1
!voiceonly @Member2
!voiceonly @Member3
```

### Q: Does this work automatically?
**A:** Voice is enabled automatically, but camera must be turned off manually by the member.

---

## 💬 Quick Reference

```
Enable voice, disable video:  !voiceonly @username
Turn video off, keep voice:   !videooff @username
Enable voice (can use video): !videoon @username
```

---

## 🎯 Best Practices

1. **Use `!voiceonly`** when you want voice but not video
2. **Send reminder** if member doesn't turn off camera
3. **Set server rules** about camera usage
4. **Use `!unmute`** if you just want voice without video request

---

**Remember:** Discord bots cannot directly control video cameras. The bot will enable voice and notify members, but they must manually turn off their camera.
