import os
import sys
import re

def load_env_file(env_file):
    """Load environment variables from a .env file."""
    if not os.path.exists(env_file):
        print(f"Error: {env_file} not found")
        return False
    
    print(f"Loading environment variables from {env_file}")
    with open(env_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Find the first occurrence of = (ignoring = in values)
            match = re.match(r'([^=]+)=(.*)$', line)
            if match:
                key, value = match.groups()
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                
                os.environ[key] = value
                print(f"Set {key}={value}")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python load_env.py <env_file>")
        sys.exit(1)
    
    env_file = sys.argv[1]
    if load_env_file(env_file):
        print("Environment variables loaded successfully")
        sys.exit(0)
    else:
        sys.exit(1) 