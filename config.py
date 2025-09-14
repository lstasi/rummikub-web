#!/usr/bin/env python3
"""
Configuration loader for Rummikub Web
Injects environment variables into the HTML file for deployment
"""

import os
import sys
from pathlib import Path

def inject_config():
    """Inject environment variables into index.html"""
    
    # Get current directory
    current_dir = Path(__file__).parent
    index_file = current_dir / 'index.html'
    
    if not index_file.exists():
        print("❌ index.html not found!")
        return False
    
    # Read the HTML file
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get environment variables
    admin_password = os.environ.get('RUMMIKUB_ADMIN_PASSWORD', '')
    backend_url = os.environ.get('RUMMIKUB_BACKEND_URL', 'http://localhost:8000')
    
    if admin_password:
        print(f"✅ Found admin password in environment")
        # Inject the password into the JavaScript
        # Look for the loadConfiguration method and add environment variable loading
        config_injection = f"""
            // Environment variable injection (server-side)
            if (!this.adminPassword) {{
                this.adminPassword = '{admin_password}';
                this.adminPasswordInput.value = this.adminPassword;
                console.log('Admin password loaded from environment variable');
            }}"""
        
        # Insert after the loadConfiguration method
        content = content.replace(
            "// Environment variables not available in browser context",
            f"{config_injection}\n                    // Environment variables not available in browser context"
        )
    
    if backend_url != 'http://localhost:8000':
        print(f"✅ Setting backend URL to: {backend_url}")
        content = content.replace(
            'value="http://localhost:8000"',
            f'value="{backend_url}"'
        )
    
    # Write the modified content back
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🎲 Configuration injected successfully!")
    return True

def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', 'help']:
        print("🎲 Rummikub Web Configuration Loader")
        print("Usage: python3 config.py")
        print()
        print("Environment Variables:")
        print("  RUMMIKUB_ADMIN_PASSWORD - Admin password for creating games")
        print("  RUMMIKUB_BACKEND_URL    - Backend server URL")
        print()
        print("Example:")
        print("  export RUMMIKUB_ADMIN_PASSWORD='your_secure_password'")
        print("  python3 config.py")
        return
    
    print("🎲 Rummikub Web Configuration Loader")
    print("Loading environment variables...")
    
    if inject_config():
        print("✅ Ready to serve!")
    else:
        print("❌ Configuration failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()