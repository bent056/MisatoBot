# MisatoBot
### epic discord bot
Just a simple project for myself and friends to use in various servers  
Pretty limited capabilities at least as of now, but want to include more in the future.  

## Current Capabilities

### Announcement Stealer
- Can copy messages from one server/channel and paste them into another server/channel  
- Best used for stealing announcements from a specific channel in order to filter out any unnecessary messages
#### Limitations
- Limited to the channels I can manually add, no way to select original and target servers from Discord itself
#### Goals
- [ ] Create command that allows user to select channels as original and copy channels without needing to edit souce code
- [ ] Fix error: `400 Bad Request (error code: 50006): Cannot send an empty message` whenever an image or video file is sent

### Chat Logger
- Pretty similar to announcement stealer, except it sends messages to a read only channel and includes the user who sent each message.
- Basically just to stop someone from sending something, deleting it, and then claiming to never have sent it.  
#### Limitations
- Looks a little bit clunky and cluttered
- Also limited to manually added channels, no support for selecting channels in Discord
#### Goals
- [ ] Clean up how the copies messages look, maybe format them differently
- [ ] Include the channel name from which the message came from, in case one wanted to log an entire server as opposed to a single channel
- [ ] Create command that allows user to select channels as original and copy channels without needing to edit souce code 
- [ ] Fix error: `400 Bad Request (error code: 50006): Cannot send an empty message` whenever an image or video file is sent

### MisatoCop
- Kind of a gag function, basically if a certain user mentions specific keywords in a message, the bot will send an embed claiming to have
detected suspicious activity, and that authorities have been notified
- Also DMs the user a message and gif
#### Limitations
- Not really useful for anything, really just a joke
#### Goals
- [ ] It would be nice to give it some sort of purpose, maybe pull from a list of suspicious words that could potentially hint to a dangerous individual

