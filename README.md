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

🔧 **Easy Setup**
- Single HTML file - no build process required
- Works with any modern web browser
- Configurable backend URL
- Local storage for game session persistence

## Quick Start

1. **Start the backend server:**
   ```bash
   # Clone and start the rummikub-backend
   git clone https://github.com/lstasi/rummikub-backend
   cd rummikub-backend
   docker-compose up --build
   ```

2. **Open the frontend:**
   - Open `index.html` in any modern web browser
   - Or serve it with a simple HTTP server:
   ```bash
   # Python 3
   python -m http.server 8080
   
   # Node.js (if you have http-server installed)
   npx http-server -p 8080
   ```

3. **Play the game:**
   - Enter your name and the backend URL (default: `http://localhost:8090`)
   - Either join an existing game with a Game ID or create a new one
   - Start playing! The game supports real-time multiplayer

## Game Interface

### Setup Screen
- **Backend URL**: Configure the API server address
- **Player Name**: Enter your display name
- **Game ID**: Join existing games using the unique game identifier

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

## Files

- `index.html` - Complete Rummikub game (single file)
- `rules.html` - Game rules reference page
- `README.md` - Documentation

## Backend Integration

This frontend is designed to work with the [rummikub-backend](https://github.com/lstasi/rummikub-backend) API server.

### Authentication
- **Game Creation**: Uses Basic Auth with admin credentials (`admin:rummikub2024`)
- **Game Play**: Uses JWT Bearer tokens obtained when joining a game
- **Session Management**: Automatic token-based authentication for all game actions

### API Endpoints Used
- `POST /game` - Create new games
- `POST /game/{game_id}/join` - Join games with Game ID
- `GET /game/{game_id}` - Get game state (requires Bearer token)
- `POST /game/{game_id}/action` - Perform game actions (requires Bearer token)

## Browser Compatibility

Works on all modern browsers (Chrome 70+, Firefox 65+, Safari 12+, Edge 79+)
