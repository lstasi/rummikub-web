# Rummikub Web Frontend

A modern, mobile-optimized web frontend for the Rummikub tile game. Built as a single HTML file with embedded CSS and JavaScript for easy deployment and maximum compatibility.

## Features

✨ **Complete Rummikub Implementation**
- Full game logic with rule validation
- Support for 2-4 players
- Groups and runs detection
- Initial 30-point meld requirement
- Joker support

🎮 **Modern User Interface**
- Beautiful gradient design with tile animations
- Drag and drop functionality (desktop and mobile)
- Click-to-select tiles for mobile devices
- Visual feedback with magnet effects and highlights
- Responsive design optimized for all screen sizes

📱 **Mobile Optimized**
- Touch-friendly interface
- Responsive grid layouts
- Large touch targets for easy interaction
- Works great on phones and tablets

🔧 **Easy Setup & Configuration**
- Single HTML file - no build process required
- Works with any modern web browser
- **Configurable admin password via environment variables**
- **Multiple password configuration methods**
- Local storage for game session persistence

## Password Configuration

The admin password for creating games can be configured in multiple ways:

### Method 1: Environment Variable (Recommended for Production)
```bash
export RUMMIKUB_ADMIN_PASSWORD='your_secure_password'
npm run start
```

### Method 2: URL Parameter (Quick Testing)
```
http://localhost:8080/?password=your_password
```

### Method 3: Configuration UI (Interactive)
Set the password directly in the web interface - it will be saved in browser localStorage.

### Method 4: Environment File (Development)
```bash
cp .env.example .env.local
# Edit .env.local and set RUMMIKUB_ADMIN_PASSWORD
npm run config  # Apply configuration
npm run serve   # Start server
```

## Quick Start

1. **Start the backend server:**
   ```bash
   # Clone and start the rummikub-backend
   git clone https://github.com/lstasi/rummikub-backend
   cd rummikub-backend
   docker-compose up --build
   ```

2. **Configure and start the frontend:**
   ```bash
   # Set admin password
   export RUMMIKUB_ADMIN_PASSWORD='your_secure_password'
   
   # Start with automatic configuration
   npm run start
   
   # Or manually configure and serve
   npm run config
   npm run serve
   ```

3. **Play the game:**
   - Enter your name and the backend URL (default: `http://localhost:8000`)
   - Either join an existing game with an invite code or create a new one
   - Start playing! The game supports real-time multiplayer

## Game Interface

### Setup Screen
- **Backend URL**: Configure the API server address
- **Admin Password**: Set password for creating games (multiple configuration options)
- **Player Name**: Enter your display name
- **Invite Code**: Join existing games or get one when creating

### Game Screen
- **Game Info Panel**: Shows current player, game status, and players list
- **Game Board**: Drag tiles here or use "Place Selected Tiles"
- **Your Hand**: Your tiles - click to select, drag to move
- **Action Buttons**: Draw tiles or place selected tiles

## Controls

### Desktop
- **Drag & Drop**: Drag tiles from hand to board
- **Click**: Select/deselect tiles
- **Keyboard**: Press Enter to refresh game state

### Mobile/Touch
- **Tap**: Select tiles
- **Long Press & Drag**: Move tiles (with haptic feedback)
- **Touch-friendly buttons**: Large, easy-to-tap interface

## Security & Configuration

### Password Security
- **No hardcoded passwords**: All passwords are configurable
- **Multiple configuration methods**: Choose what works best for your deployment
- **Local storage**: Remembers configuration between sessions
- **Environment variable support**: Perfect for containerized deployments

### Deployment Options
```bash
# Docker with environment variable
docker run -e RUMMIKUB_ADMIN_PASSWORD='secure_pass' -p 8080:8080 rummikub-web

# Traditional server with config
export RUMMIKUB_ADMIN_PASSWORD='secure_pass'
python3 config.py && python3 serve.py

# Development with URL parameter
python3 serve.py
# Then visit: http://localhost:8080/?password=dev_password
```

## Files

- `index.html` - Complete Rummikub game (single file with configurable auth)
- `config.py` - Environment variable configuration loader
- `.env.example` - Example environment configuration
- `package.json` - NPM scripts for easy deployment
- `README.md` - This documentation

## Browser Compatibility

Works on all modern browsers (Chrome 70+, Firefox 65+, Safari 12+, Edge 79+)
