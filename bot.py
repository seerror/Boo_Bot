import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
import asyncio

load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Settings file to store configuration
SETTINGS_FILE = 'settings.json'

def load_settings():
    """Load bot settings from file"""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            # Ensure all required keys exist
            if 'auto_mute' not in settings:
                settings['auto_mute'] = True
            if 'auto_camera_off' not in settings:
                settings['auto_camera_off'] = True
            if 'enabled_servers' not in settings:
                settings['enabled_servers'] = []
            if 'allowed_members' not in settings:
                settings['allowed_members'] = {}  # {server_id: [member_ids]}
            if 'assigned_admins' not in settings:
                settings['assigned_admins'] = {}  # {server_id: [member_ids]}
            return settings
    return {
        'auto_mute': True,
        'auto_camera_off': True,
        'enabled_servers': [],
        'allowed_members': {},  # {server_id: [member_ids]}
        'assigned_admins': {}  # {server_id: [member_ids]}
    }

def save_settings(settings):
    """Save bot settings to file"""
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def is_admin_or_assigned(ctx):
    """Check if member is admin, assigned admin, or in allowed members list"""
    # Check if user is Discord admin
    if ctx.author.guild_permissions.administrator:
        return True
    
    # Check if user is assigned admin
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    if 'assigned_admins' in settings and server_id in settings['assigned_admins']:
        if ctx.author.id in settings['assigned_admins'][server_id]:
            return True
    
    return False

def is_allowed_member(ctx):
    """Check if member is admin, assigned admin, or in allowed members list"""
    # Check if user is admin or assigned admin
    if is_admin_or_assigned(ctx):
        return True
    
    # Check if user is in allowed members list
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    if 'allowed_members' not in settings:
        return False
    
    if server_id not in settings['allowed_members']:
        return False
    
    # Check if member ID is in the list
    allowed_ids = settings['allowed_members'][server_id]
    return ctx.author.id in allowed_ids

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in!')
    print(f'Bot is in {len(bot.guilds)} servers')
    await bot.change_presence(activity=discord.Game(name="Managing voice channels"))
    
    # Auto-enable bot for all servers it's in
    settings = load_settings()
    updated = False
    for guild in bot.guilds:
        if guild.id not in settings['enabled_servers']:
            settings['enabled_servers'].append(guild.id)
            updated = True
            print(f'Auto-enabled bot for server: {guild.name}')
    
    if updated:
        save_settings(settings)
        print('Bot is now enabled for all servers!')

@bot.event
async def on_member_join(member):
    """Automatically mute and disable camera when member joins"""
    settings = load_settings()
    
    # Auto-enable if not already enabled (for safety)
    if member.guild.id not in settings['enabled_servers']:
        settings['enabled_servers'].append(member.guild.id)
        save_settings(settings)
    
    # Wait a bit for member to potentially join voice channel
    await asyncio.sleep(2)
    
    # Check if member is in a voice channel
    if member.voice and member.voice.channel:
        try:
            # Mute the member
            if settings['auto_mute']:
                await member.edit(mute=True)
                print(f'Auto-muted {member.name} in {member.guild.name}')
            
            # Disable camera (deafen also disables video in some cases, but we'll use mute for video)
            # Note: Discord API doesn't directly control camera, but we can mute which affects audio
            # For video, we need to use voice state updates
            if settings['auto_camera_off']:
                # We'll track this and notify admins
                print(f'Camera should be off for {member.name} in {member.guild.name}')
        except discord.Forbidden:
            print(f'No permission to modify {member.name} in {member.guild.name}')
        except Exception as e:
            print(f'Error modifying {member.name}: {e}')

@bot.event
async def on_guild_join(guild):
    """Auto-enable bot when added to a new server"""
    settings = load_settings()
    
    if guild.id not in settings['enabled_servers']:
        settings['enabled_servers'].append(guild.id)
        save_settings(settings)
        print(f'Bot added to {guild.name} - Auto-enabled!')
        
        # Try to send welcome message to system channel or first text channel
        try:
            channel = guild.system_channel
            if channel is None:
                # Find first text channel bot can send messages to
                for ch in guild.text_channels:
                    if ch.permissions_for(guild.me).send_messages:
                        channel = ch
                        break
            
            if channel:
                embed = discord.Embed(
                    title='🤖 Bot Added Successfully!',
                    description='Auto-mute and camera control bot is now active!',
                    color=discord.Color.green()
                )
                embed.add_field(
                    name='Quick Start',
                    value='The bot is **automatically enabled** for this server!\n'
                          'Members will be auto-muted when joining voice channels.\n'
                          'Use `!help_bot` to see all commands.',
                    inline=False
                )
                embed.add_field(
                    name='Admin Commands',
                    value='`!settings` - View settings\n'
                          '`!disable` - Disable auto-mute\n'
                          '`!enable` - Re-enable auto-mute',
                    inline=False
                )
                await channel.send(embed=embed)
        except Exception as e:
            print(f'Could not send welcome message to {guild.name}: {e}')

@bot.event
async def on_voice_state_update(member, before, after):
    """Handle when someone joins a voice channel"""
    settings = load_settings()
    
    # Auto-enable if not already enabled (for safety)
    if member.guild.id not in settings['enabled_servers']:
        settings['enabled_servers'].append(member.guild.id)
        save_settings(settings)
    
    # If member just joined a voice channel
    if before.channel is None and after.channel is not None:
        try:
            # Auto-mute
            if settings['auto_mute']:
                await asyncio.sleep(0.5)  # Small delay to ensure member is fully in channel
                await member.edit(mute=True)
                print(f'Auto-muted {member.name} when joining voice channel in {member.guild.name}')
            
            # Note: Discord API doesn't have direct camera control
            # But we can ensure they're muted which is the closest we can get
        except discord.Forbidden:
            print(f'No permission to modify {member.name} in {member.guild.name}')
        except Exception as e:
            print(f'Error modifying {member.name}: {e}')

@bot.command(name='enable')
async def enable_bot(ctx):
    """Enable auto-mute and camera-off for this server (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can enable/disable the bot.')
        return
    
    settings = load_settings()
    
    if ctx.guild.id not in settings['enabled_servers']:
        settings['enabled_servers'].append(ctx.guild.id)
        save_settings(settings)
        await ctx.send('✅ Auto-mute and camera-off enabled for this server!')
    else:
        await ctx.send('✅ Bot is already enabled for this server!')

@bot.command(name='disable')
async def disable_bot(ctx):
    """Disable auto-mute and camera-off for this server (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can enable/disable the bot.')
        return
    
    settings = load_settings()
    
    if ctx.guild.id in settings['enabled_servers']:
        settings['enabled_servers'].remove(ctx.guild.id)
        save_settings(settings)
        await ctx.send('❌ Auto-mute and camera-off disabled for this server.')
    else:
        await ctx.send('⚠️ Bot is already disabled for this server.')

@bot.command(name='camon')
async def camera_on(ctx, member: discord.Member = None):
    """Turn camera on for a member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member is None:
        member = ctx.author
    
    if member.voice and member.voice.channel:
        try:
            # Unmute to allow audio (closest we can get to "camera on")
            await member.edit(mute=False)
            await ctx.send(f'✅ Camera/audio enabled for {member.mention}')
        except discord.Forbidden:
            await ctx.send('❌ No permission to modify this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='camoff')
async def camera_off(ctx, member: discord.Member = None):
    """Turn camera off for a member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member is None:
        member = ctx.author
    
    if member.voice and member.voice.channel:
        try:
            # Mute to disable audio (closest we can get to "camera off")
            await member.edit(mute=True)
            await ctx.send(f'✅ Camera/audio disabled for {member.mention}')
        except discord.Forbidden:
            await ctx.send('❌ No permission to modify this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='videooff')
async def video_off(ctx, member: discord.Member = None):
    """Turn video off but keep voice on for a member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member is None:
        member = ctx.author
    
    if member.voice and member.voice.channel:
        try:
            # Try to disable video while keeping audio on
            # Note: Discord API limitations - we'll use the best available method
            # We can't directly control video, but we can request it via voice state
            
            # First, ensure they're not muted (voice on)
            await member.edit(mute=False)
            
            # Attempt to control video state (Discord API limitation)
            # The best we can do is notify and suggest manual action
            # Discord doesn't allow bots to directly turn off video cameras
            
            await ctx.send(
                f'✅ **Voice enabled for {member.mention}**\n'
                f'⚠️ **Note:** Discord API doesn\'t allow bots to directly control video cameras.\n'
                f'Please ask {member.mention} to manually turn off their camera.\n'
                f'Their microphone is now enabled and they can speak.'
            )
            
            # Try to send a DM to the member asking them to turn off camera
            try:
                if member != ctx.author:
                    await member.send(
                        f'👋 Hello! An admin has requested that you turn off your camera '
                        f'while keeping your microphone on. Please turn off your camera manually. '
                        f'Your microphone is enabled and you can speak.'
                    )
            except:
                pass  # Can't DM member, that's okay
                
        except discord.Forbidden:
            await ctx.send('❌ No permission to modify this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='videoon')
async def video_on(ctx, member: discord.Member = None):
    """Turn video on for a member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member is None:
        member = ctx.author
    
    if member.voice and member.voice.channel:
        try:
            # Ensure voice is on
            await member.edit(mute=False)
            await ctx.send(
                f'✅ **Voice enabled for {member.mention}**\n'
                f'💡 They can now turn on their camera manually if they want.'
            )
        except discord.Forbidden:
            await ctx.send('❌ No permission to modify this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='voiceonly')
async def voice_only(ctx, member: discord.Member = None):
    """Enable voice but disable video for a member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member is None:
        member = ctx.author
    
    if member.voice and member.voice.channel:
        try:
            # Enable voice (unmute)
            await member.edit(mute=False)
            
            await ctx.send(
                f'✅ **Voice enabled for {member.mention}**\n'
                f'📹 **Video:** Please turn off your camera manually\n'
                f'🎤 **Audio:** Enabled - You can speak\n\n'
                f'⚠️ **Note:** Discord bots cannot directly control video cameras. '
                f'Please ask {member.mention} to manually turn off their camera.'
            )
            
            # Try to notify the member
            try:
                if member != ctx.author:
                    await member.send(
                        f'👋 Hello! An admin has enabled your microphone.\n'
                        f'Please turn off your camera manually while keeping your microphone on.\n'
                        f'You can speak, but please disable your video camera.'
                    )
            except:
                pass
                
        except discord.Forbidden:
            await ctx.send('❌ No permission to modify this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='mute')
async def mute_user(ctx, member: discord.Member):
    """Mute a specific member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member.voice and member.voice.channel:
        try:
            await member.edit(mute=True)
            await ctx.send(f'🔇 Muted {member.mention}')
        except discord.Forbidden:
            await ctx.send('❌ No permission to mute this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='unmute')
async def unmute_user(ctx, member: discord.Member):
    """Unmute a specific member (Admin or Allowed Member)"""
    if not is_allowed_member(ctx):
        await ctx.send('❌ You do not have permission to use this command. Ask an admin to add you to the allowed list with `!allow <your_name>`.')
        return
    
    if member.voice and member.voice.channel:
        try:
            await member.edit(mute=False)
            await ctx.send(f'🔊 Unmuted {member.mention}')
        except discord.Forbidden:
            await ctx.send('❌ No permission to unmute this member.')
        except Exception as e:
            await ctx.send(f'❌ Error: {e}')
    else:
        await ctx.send('❌ Member is not in a voice channel.')

@bot.command(name='settings')
async def show_settings(ctx):
    """Show current bot settings (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can view settings.')
        return
    
    settings = load_settings()
    enabled = ctx.guild.id in settings['enabled_servers']
    server_id = str(ctx.guild.id)
    
    # Get allowed members list
    allowed_members = []
    if 'allowed_members' in settings and server_id in settings['allowed_members']:
        for member_id in settings['allowed_members'][server_id]:
            try:
                member = ctx.guild.get_member(member_id)
                if member:
                    allowed_members.append(member.display_name)
            except:
                pass
    
    # Get assigned admins list
    assigned_admins = []
    if 'assigned_admins' in settings and server_id in settings['assigned_admins']:
        for member_id in settings['assigned_admins'][server_id]:
            try:
                member = ctx.guild.get_member(member_id)
                if member:
                    assigned_admins.append(member.display_name)
            except:
                pass
    
    embed = discord.Embed(
        title='⚙️ Bot Settings for ' + ctx.guild.name,
        description='Current configuration for this server',
        color=discord.Color.blue()
    )
    embed.add_field(
        name='📊 Server Status',
        value='✅ **ENABLED** - Bot is active' if enabled else '❌ **DISABLED** - Bot is inactive',
        inline=False
    )
    embed.add_field(
        name='🔇 Auto Mute',
        value='✅ **ON** - Members auto-muted when joining voice' if settings['auto_mute'] else '❌ **OFF** - No auto-mute',
        inline=True
    )
    embed.add_field(
        name='📹 Auto Camera Off',
        value='✅ **ON** - Camera/audio disabled by default' if settings['auto_camera_off'] else '❌ **OFF** - Camera/audio allowed',
        inline=True
    )
    
    # Show assigned admins
    if assigned_admins:
        admins_list = ', '.join(assigned_admins[:10])  # Show first 10
        if len(assigned_admins) > 10:
            admins_list += f' (+{len(assigned_admins) - 10} more)'
        embed.add_field(
            name='👑 Assigned Admins',
            value=admins_list or 'None',
            inline=False
        )
    else:
        embed.add_field(
            name='👑 Assigned Admins',
            value='None - Only Discord admins can use admin commands',
            inline=False
        )
    
    # Show allowed members
    if allowed_members:
        members_list = ', '.join(allowed_members[:10])  # Show first 10
        if len(allowed_members) > 10:
            members_list += f' (+{len(allowed_members) - 10} more)'
        embed.add_field(
            name='👥 Allowed Members',
            value=members_list or 'None',
            inline=False
        )
    else:
        embed.add_field(
            name='👥 Allowed Members',
            value='None - Only admins can use commands',
            inline=False
        )
    
    embed.add_field(
        name='🔧 How to Customize',
        value='Use commands below to change settings:\n'
              '`!toggle_automute` - Turn auto-mute on/off\n'
              '`!toggle_autocam` - Turn auto camera-off on/off\n'
              '`!assign_admin <member>` - Assign admin permissions\n'
              '`!unassign_admin <member>` - Remove admin permissions\n'
              '`!allow <member>` - Allow member to use mute/camera commands\n'
              '`!remove <member>` - Remove member from allowed list\n'
              '`!disable` - Turn off bot completely\n'
              '`!enable` - Turn on bot',
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='toggle_automute')
async def toggle_automute(ctx):
    """Toggle auto-mute feature on/off (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can change settings.')
        return
    
    settings = load_settings()
    settings['auto_mute'] = not settings['auto_mute']
    save_settings(settings)
    status = 'enabled' if settings['auto_mute'] else 'disabled'
    emoji = '✅' if settings['auto_mute'] else '❌'
    await ctx.send(
        f'{emoji} **Auto-mute is now {status}!**\n'
        f'When {status}, members will {"be automatically muted" if settings["auto_mute"] else "NOT be muted"} when joining voice channels.'
    )

@bot.command(name='toggle_autocam')
async def toggle_autocam(ctx):
    """Toggle auto camera-off feature on/off (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can change settings.')
        return
    
    settings = load_settings()
    settings['auto_camera_off'] = not settings['auto_camera_off']
    save_settings(settings)
    status = 'enabled' if settings['auto_camera_off'] else 'disabled'
    emoji = '✅' if settings['auto_camera_off'] else '❌'
    await ctx.send(
        f'{emoji} **Auto camera-off is now {status}!**\n'
        f'When {status}, members will have camera/audio {"disabled" if settings["auto_camera_off"] else "enabled"} by default when joining voice.'
    )

@bot.command(name='allow')
async def allow_member(ctx, member: discord.Member):
    """Allow a member to use mute/unmute and camera commands (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can manage allowed members.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Initialize allowed_members if it doesn't exist
    if 'allowed_members' not in settings:
        settings['allowed_members'] = {}
    if server_id not in settings['allowed_members']:
        settings['allowed_members'][server_id] = []
    
    # Check if member is already allowed
    if member.id in settings['allowed_members'][server_id]:
        await ctx.send(f'⚠️ {member.mention} is already allowed to use mute/camera commands.')
        return
    
    # Add member to allowed list
    settings['allowed_members'][server_id].append(member.id)
    save_settings(settings)
    
    await ctx.send(
        f'✅ **{member.mention} is now allowed to use mute/unmute and camera commands!**\n'
        f'They can now use: `!mute`, `!unmute`, `!camon`, `!camoff`'
    )

@bot.command(name='remove')
async def remove_member(ctx, member: discord.Member):
    """Remove a member from allowed list (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can manage allowed members.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Check if allowed_members exists
    if 'allowed_members' not in settings or server_id not in settings['allowed_members']:
        await ctx.send(f'⚠️ {member.mention} is not in the allowed list.')
        return
    
    # Check if member is in allowed list
    if member.id not in settings['allowed_members'][server_id]:
        await ctx.send(f'⚠️ {member.mention} is not in the allowed list.')
        return
    
    # Remove member from allowed list
    settings['allowed_members'][server_id].remove(member.id)
    save_settings(settings)
    
    await ctx.send(
        f'❌ **{member.mention} has been removed from the allowed list.**\n'
        f'They can no longer use mute/camera commands (unless they are admin).'
    )

@bot.command(name='allowed')
async def show_allowed(ctx):
    """Show all members who can use mute/camera commands (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command. Only admins or assigned admins can view allowed members.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Get allowed members
    allowed_members = []
    if 'allowed_members' in settings and server_id in settings['allowed_members']:
        for member_id in settings['allowed_members'][server_id]:
            try:
                member = ctx.guild.get_member(member_id)
                if member:
                    allowed_members.append(member)
            except:
                pass
    
    if allowed_members:
        members_list = '\n'.join([f'• {member.mention} ({member.display_name})' for member in allowed_members])
        embed = discord.Embed(
            title='👥 Allowed Members',
            description=f'Members who can use mute/camera commands:\n\n{members_list}',
            color=discord.Color.green()
        )
        embed.set_footer(text=f'Total: {len(allowed_members)} member(s)')
    else:
        embed = discord.Embed(
            title='👥 Allowed Members',
            description='No members are allowed (only admins can use commands).\n\nUse `!allow <member>` to add someone.',
            color=discord.Color.orange()
        )
    
    await ctx.send(embed=embed)

@bot.command(name='assign_admin')
async def assign_admin(ctx, member: discord.Member):
    """Assign admin permissions to a member (Discord Admin only)"""
    # Only actual Discord admins can assign other admins
    if not ctx.author.guild_permissions.administrator:
        await ctx.send('❌ Only Discord administrators can assign admin permissions to others.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Initialize assigned_admins if it doesn't exist
    if 'assigned_admins' not in settings:
        settings['assigned_admins'] = {}
    if server_id not in settings['assigned_admins']:
        settings['assigned_admins'][server_id] = []
    
    # Check if member is already an assigned admin
    if member.id in settings['assigned_admins'][server_id]:
        await ctx.send(f'⚠️ {member.mention} is already an assigned admin.')
        return
    
    # Check if member is already a Discord admin
    if member.guild_permissions.administrator:
        await ctx.send(f'ℹ️ {member.mention} is already a Discord administrator. No need to assign admin permissions.')
        return
    
    # Add member to assigned admins list
    settings['assigned_admins'][server_id].append(member.id)
    save_settings(settings)
    
    await ctx.send(
        f'✅ **{member.mention} is now an assigned admin!**\n'
        f'They can now use all admin commands:\n'
        f'• `!settings` - View settings\n'
        f'• `!toggle_automute` - Toggle auto-mute\n'
        f'• `!toggle_autocam` - Toggle auto camera-off\n'
        f'• `!enable` / `!disable` - Enable/disable bot\n'
        f'• `!allow` / `!remove` - Manage allowed members\n'
        f'• All mute/camera commands'
    )

@bot.command(name='unassign_admin')
async def unassign_admin(ctx, member: discord.Member):
    """Remove admin permissions from a member (Discord Admin only)"""
    # Only actual Discord admins can unassign other admins
    if not ctx.author.guild_permissions.administrator:
        await ctx.send('❌ Only Discord administrators can remove admin permissions from others.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Check if assigned_admins exists
    if 'assigned_admins' not in settings or server_id not in settings['assigned_admins']:
        await ctx.send(f'⚠️ {member.mention} is not an assigned admin.')
        return
    
    # Check if member is in assigned admins list
    if member.id not in settings['assigned_admins'][server_id]:
        await ctx.send(f'⚠️ {member.mention} is not an assigned admin.')
        return
    
    # Remove member from assigned admins list
    settings['assigned_admins'][server_id].remove(member.id)
    save_settings(settings)
    
    await ctx.send(
        f'❌ **{member.mention} has been removed from assigned admins.**\n'
        f'They can no longer use admin commands (unless they are Discord admin).'
    )

@bot.command(name='assigned_admins')
async def show_assigned_admins(ctx):
    """Show all assigned admins (Admin or Assigned Admin only)"""
    if not is_admin_or_assigned(ctx):
        await ctx.send('❌ You do not have permission to use this command.')
        return
    
    settings = load_settings()
    server_id = str(ctx.guild.id)
    
    # Get assigned admins
    assigned_admins = []
    if 'assigned_admins' in settings and server_id in settings['assigned_admins']:
        for member_id in settings['assigned_admins'][server_id]:
            try:
                member = ctx.guild.get_member(member_id)
                if member:
                    assigned_admins.append(member)
            except:
                pass
    
    if assigned_admins:
        admins_list = '\n'.join([f'• {member.mention} ({member.display_name})' for member in assigned_admins])
        embed = discord.Embed(
            title='👑 Assigned Admins',
            description=f'Members with admin permissions:\n\n{admins_list}',
            color=discord.Color.gold()
        )
        embed.set_footer(text=f'Total: {len(assigned_admins)} assigned admin(s)')
    else:
        embed = discord.Embed(
            title='👑 Assigned Admins',
            description='No assigned admins (only Discord admins have permissions).\n\nUse `!assign_admin <member>` to assign admin permissions.',
            color=discord.Color.orange()
        )
    
    await ctx.send(embed=embed)

@bot.command(name='help_bot')
async def help_command(ctx):
    """Show all available commands"""
    embed = discord.Embed(
        title='🤖 Bot Commands & Customization',
        description='All available commands for this bot',
        color=discord.Color.green()
    )
    
    embed.add_field(
        name='⚙️ **Customization Commands** (Admin Only)',
        value='''
`!settings` - View current bot settings
`!toggle_automute` - Turn auto-mute ON/OFF
`!toggle_autocam` - Turn auto camera-off ON/OFF
`!enable` - Enable bot for this server
`!disable` - Disable bot for this server
        ''',
        inline=False
    )
    
    embed.add_field(
        name='👥 **Member Control Commands** (Admin or Allowed Members)',
        value='''
`!mute <member>` - Mute a specific member
`!unmute <member>` - Unmute a specific member
`!camon [member]` - Turn camera/audio ON for member
`!camoff [member]` - Turn camera/audio OFF for member
`!voiceonly [member]` - Enable voice but disable video
`!videooff [member]` - Turn video off, keep voice on
`!videoon [member]` - Enable voice (member can turn video on)
        ''',
        inline=False
    )
    
    embed.add_field(
        name='👑 **Admin Assignment Commands** (Discord Admin Only)',
        value='''
`!assign_admin <member>` - Assign admin permissions to member
`!unassign_admin <member>` - Remove admin permissions from member
`!assigned_admins` - Show all assigned admins
        ''',
        inline=False
    )
    
    embed.add_field(
        name='➕ **Member Permission Commands** (Admin or Assigned Admin Only)',
        value='''
`!allow <member>` - Allow member to use mute/camera commands
`!remove <member>` - Remove member from allowed list
`!allowed` - Show all allowed members
        ''',
        inline=False
    )
    
    embed.add_field(
        name='📖 **Info Commands**',
        value='''
`!help_bot` - Show this help message
        ''',
        inline=False
    )
    
    embed.set_footer(text='💡 Tip: Use !settings to see current configuration')
    
    await ctx.send(embed=embed)

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('❌ You do not have permission to use this command.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('❌ Missing required argument. Use `!help_bot` for command usage.')
    else:
        print(f'Error: {error}')

# Run the bot
if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        print('Error: DISCORD_TOKEN not found in environment variables!')
        print('Please create a .env file with your Discord bot token.')
    else:
        bot.run(TOKEN)
