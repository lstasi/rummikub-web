#!/usr/bin/env python3
"""
Simple HTTP server for Rummikub Web Frontend
Usage: python serve.py [port]
Default port: 8080
"""

import http.server
import socketserver
import sys
import os
import webbrowser
from pathlib import Path

def main():
    # Get port from command line or use default
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    
    # Change to the directory containing this script
    os.chdir(Path(__file__).parent)
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    # Add CORS headers for API requests
    class CORSRequestHandler(handler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
            super().end_headers()
    
    with socketserver.TCPServer(("", port), CORSRequestHandler) as httpd:
        print(f"🎲 Rummikub Web Server")
        print(f"📡 Serving at: http://localhost:{port}")
        print(f"📱 Mobile-optimized Rummikub game ready!")
        print(f"💡 Make sure rummikub-backend is running on port 8000")
        print(f"🛑 Press Ctrl+C to stop")
        print()
        
        # Try to open browser
        try:
            webbrowser.open(f"http://localhost:{port}")
            print(f"🌐 Opened browser automatically")
        except:
            print(f"🌐 Open http://localhost:{port} in your browser")
        
        print()
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)