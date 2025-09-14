#!/usr/bin/env python3
"""
Test script to demonstrate the password configuration functionality
"""

import os
import sys
import subprocess
from pathlib import Path

def test_configuration():
    """Test different password configuration methods"""
    
    print("🎲 Testing Rummikub Web Password Configuration")
    print("=" * 50)
    
    # Test 1: Environment variable configuration
    print("\n📋 Test 1: Environment Variable Configuration")
    print("Setting RUMMIKUB_ADMIN_PASSWORD='secure_password_123'")
    
    env = os.environ.copy()
    env['RUMMIKUB_ADMIN_PASSWORD'] = 'secure_password_123'
    
    result = subprocess.run([
        'python3', 'config.py'
    ], env=env, capture_output=True, text=True, cwd=Path(__file__).parent)
    
    if result.returncode == 0:
        print("✅ Environment variable configuration: PASSED")
        print(f"   Output: {result.stdout.strip()}")
    else:
        print("❌ Environment variable configuration: FAILED")
        print(f"   Error: {result.stderr}")
    
    # Test 2: Check that hardcoded password is removed
    print("\n📋 Test 2: Verify No Hardcoded Passwords")
    
    with open('index.html', 'r') as f:
        content = f.read()
    
    if 'rummikub2024' in content:
        print("❌ Hardcoded password check: FAILED")
        print("   Found hardcoded 'rummikub2024' in index.html")
    else:
        print("✅ Hardcoded password check: PASSED")
        print("   No hardcoded passwords found")
    
    # Test 3: Check configuration methods are documented
    print("\n📋 Test 3: Configuration Methods Documentation")
    
    config_methods = [
        'URL parameter',
        'environment variable', 
        'localStorage',
        'configuration UI'
    ]
    
    all_documented = True
    for method in config_methods:
        if method.lower() not in content.lower():
            print(f"❌ {method} not documented in HTML")
            all_documented = False
    
    if all_documented:
        print("✅ Configuration methods documentation: PASSED")
        print("   All configuration methods are properly documented")
    else:
        print("❌ Configuration methods documentation: FAILED")
    
    # Test 4: Check if authentication uses configurable password
    print("\n📋 Test 4: Configurable Authentication")
    
    if 'getAdminCredentials()' in content and 'this.adminPassword' in content:
        print("✅ Configurable authentication: PASSED")
        print("   Authentication properly uses configurable password")
    else:
        print("❌ Configurable authentication: FAILED")
        print("   Authentication does not use configurable password")
    
    # Test 5: Check NPM scripts
    print("\n📋 Test 5: NPM Scripts Integration")
    
    try:
        with open('package.json', 'r') as f:
            package_content = f.read()
        
        if '"config"' in package_content and '"start"' in package_content:
            print("✅ NPM scripts integration: PASSED")
            print("   Package.json includes config and start scripts")
        else:
            print("❌ NPM scripts integration: FAILED")
    except Exception as e:
        print(f"❌ NPM scripts integration: FAILED - {e}")
    
    print("\n" + "=" * 50)
    print("🏁 Test Summary Complete!")
    print("\n💡 Usage Examples:")
    print("   1. npm run start  # Uses environment variables")
    print("   2. Visit: http://localhost:8080/?password=your_password")
    print("   3. Set password in the web interface")
    print("   4. export RUMMIKUB_ADMIN_PASSWORD='your_password'")

if __name__ == "__main__":
    test_configuration()