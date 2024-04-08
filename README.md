### Description

need help to setup feel free to contact me on discord @kasemsh

**Discord Media Bot**

This Discord bot streamlines the sharing of media files within Discord servers, providing users with a straightforward method to upload images or videos to designated channels using simple slash commands. It grants users flexibility by enabling them to specify the type of media (image or video) they are uploading and the target channel for delivery.

### Features

- **Media Upload:** Users can effortlessly upload media files (images or videos) directly to Discord channels using intuitive slash commands.
  
- **Media Type Verification:** The bot validates the type of media being uploaded (image or video) to ensure compatibility with Discord's requirements.
  
- **Channel Selection:** Users have the flexibility to designate the target channel where the media should be dispatched. If no channel is specified, the bot automatically selects a default channel.
  
- **Error Handling:** The bot gracefully manages various error scenarios, such as invalid media types, missing attachments, and inability to locate specified channels.
  
- **Usage Instructions:** Users can access clear usage instructions by invoking a dedicated slash command, providing guidance on leveraging the bot's functionalities.
  
- **Reliability:** The bot is engineered to be reliable and responsive, optimized to deliver timely responses to user interactions.


### New Added Features

- **Comments:** ability to add a comment on upload

https://github.com/kasem545/discord-media/assets/14138005/a46260e5-74f3-4935-9b5c-5769b505c15b


### Implementation

This bot is implemented in Python using the `nextcord` library, a modern Python library for interfacing with the Discord API. It utilizes the `nextcord.ext.commands` extension for defining slash commands and managing interactions. Sensitive information such as the bot token is securely accessed through environment variables stored in a `.env` file.

### Usage

To utilize the bot, users simply invoke the appropriate slash command (`/send_media`), specifying the desired media type (image or video) and, optionally, the target channel name. They can attach the media file to the command, and the bot will handle the rest, uploading the media to the specified channel.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kasem545/discord-media.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   TOKEN=your_bot_token_here
   ```

4. Run the bot:
   ```bash
   python Media-uploader.py
   ```

### Overall

This Discord bot simplifies the process of sharing media files within Discord servers, promoting collaboration and communication among users. With its user-friendly interface and robust functionality, it serves as a valuable asset for communities seeking to exchange media content seamlessly.

Feel free to customize and expand upon this description based on your specific bot functionalities and use cases!


https://github.com/kasem545/discord-media/assets/14138005/fb5d272c-004e-4408-8717-16b9f5763240


https://github.com/kasem545/discord-media/assets/14138005/631992de-f51f-4c7a-8aba-653aba6a64cb
