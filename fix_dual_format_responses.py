#!/usr/bin/env python3
"""
Automatic fix for dual-format responses (JSON and plain text).

This script automatically patches the generated code to handle both
application/json and text/plain responses based on Content-Type header.

This should be run after OpenAPI code generation.
"""

import os
import sys
import re

def apply_api_client_dual_format_fix():
    """Apply the dual-format response fix to ApiClient."""
    
    target_file = "speechall/api_client.py"
    
    if not os.path.exists(target_file):
        print(f"❌ File not found: {target_file}")
        return False
    
    print(f"🔧 Applying dual-format response fix to {target_file}")
    
    # Read the current file
    with open(target_file, 'r') as f:
        content = f.read()
    
    # Check if the fix is already applied
    if "# Check for dual-format responses (JSON or plain text)" in content:
        print("✅ Dual-format response fix already applied to ApiClient - skipping")
        return True
    
    # Pattern to match the original response handling code in __call_api method
    old_pattern = r'''          # deserialize response data
          if response_type == "bytearray":
              return_data = response_data\.data
          elif response_type:
              return_data = self\.deserialize\(response_data, response_type\)
          else:
              return_data = None'''

    new_pattern = '''          # deserialize response data
          if response_type == "bytearray":
              return_data = response_data.data
          elif response_type:
              # Check for dual-format responses (JSON or plain text)
              content_type = response_data.getheader('content-type')
              if content_type and 'text/plain' in content_type.lower():
                  # For text/plain responses, return the raw string data
                  return_data = response_data.data
              else:
                  # For JSON responses, deserialize normally
                  return_data = self.deserialize(response_data, response_type)
          else:
              return_data = None'''

    # Apply the replacement
    try:
        content = re.sub(old_pattern, new_pattern, content, flags=re.DOTALL)
        
        # Check if replacement was successful
        if "# Check for dual-format responses (JSON or plain text)" not in content:
            print("❌ Failed to apply replacement - method pattern may have changed")
            return False
        
        # Write the fixed content back
        with open(target_file, 'w') as f:
            f.write(content)
        
        print("✅ Dual-format response fix applied successfully to ApiClient!")
        return True
        
    except Exception as e:
        print(f"❌ Error applying fix to ApiClient: {e}")
        return False

def apply_speech_to_text_api_type_annotations_fix():
    """Apply return type annotation fixes to SpeechToTextApi."""
    
    target_file = "speechall/api/speech_to_text_api.py"
    
    if not os.path.exists(target_file):
        print(f"❌ File not found: {target_file}")
        return False
    
    print(f"🔧 Applying return type annotation fixes to {target_file}")
    
    # Read the current file
    with open(target_file, 'r') as f:
        content = f.read()
    
    # Check if the fix is already applied
    if "-> Union[TranscriptionResponse, str]:" in content:
        print("✅ Return type annotation fix already applied to SpeechToTextApi - skipping")
        return True
    
    try:
        # Fix 1: Update transcribe method return type
        content = re.sub(
            r'(\s+def transcribe\([^)]+\)) -> TranscriptionResponse:',
            r'\1 -> Union[TranscriptionResponse, str]:',
            content
        )
        
        # Fix 2: Update transcribe_remote method return type
        content = re.sub(
            r'(\s+def transcribe_remote\([^)]+\)) -> TranscriptionResponse:',
            r'\1 -> Union[TranscriptionResponse, str]:',
            content
        )
        
        # Fix 3: Update docstring return types for transcribe method
        content = re.sub(
            r'(\s+:rtype: )TranscriptionResponse(\s*""")',
            r'\1Union[TranscriptionResponse, str]\2',
            content
        )
        
        # Check if at least one replacement was successful
        if "-> Union[TranscriptionResponse, str]:" not in content:
            print("❌ Failed to apply return type annotations - method signatures may have changed")
            return False
        
        # Write the fixed content back
        with open(target_file, 'w') as f:
            f.write(content)
        
        print("✅ Return type annotation fixes applied successfully to SpeechToTextApi!")
        return True
        
    except Exception as e:
        print(f"❌ Error applying return type annotation fixes: {e}")
        return False

def main():
    """Main function."""
    print("🔧 Starting dual-format response automatic fixes...")
    
    success = True
    
    # Apply the API client fix
    if not apply_api_client_dual_format_fix():
        success = False
    
    # Apply the return type annotation fixes
    if not apply_speech_to_text_api_type_annotations_fix():
        success = False
    
    if success:
        print("✅ All dual-format response fixes applied successfully!")
        sys.exit(0)
    else:
        print("❌ Some dual-format response fixes failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 