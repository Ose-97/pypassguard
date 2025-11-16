#!/usr/bin/env python3
"""
PyPassGuard - Comprehensive Password Security Toolkit
"""

import argparse
import sys
import os

def setup_environment():
    """Add src directory to Python path"""
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

def main():
    setup_environment()
    
    parser = argparse.ArgumentParser(
        description="PyPassGuard - Password Security Toolkit",
        epilog="Example: python main.py validate 'MyP@ssw0rd'"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Hash command
    hash_parser = subparsers.add_parser('hash', help='Hash a password using SHA-256')
    hash_parser.add_argument('password', help='Password to hash')
    
    # Generate command
    gen_parser = subparsers.add_parser('generate', help='Generate random passwords')
    gen_parser.add_argument('-l', '--length', type=int, default=12, 
                          help='Password length (default: 12)')
    gen_parser.add_argument('-n', '--number', type=int, default=1,
                          help='Number of passwords to generate (default: 1)')
    gen_parser.add_argument('--no-special', action='store_true',
                          help='Exclude special characters')
    
    # Validate command
    val_parser = subparsers.add_parser('validate', help='Validate password against criteria')
    val_parser.add_argument('password', help='Password to validate')
    val_parser.add_argument('--verbose', '-v', action='store_true',
                          help='Show detailed validation results')
    
    args = parser.parse_args()
    
    if args.command == 'hash':
        try:
            from hasher import hash_password
            hashed_password = hash_password(args.password)
            print(f"Password: {args.password}")
            print(f"SHA-256 Hash: {hashed_password}")
        except ImportError:
            print("Error: Hasher module not available yet")
    
    elif args.command == 'generate':
        try:
            from generator import generate_password, generate_multiple_passwords
            
            if args.number == 1:
                # Generate single password
                password = generate_password(args.length, not args.no_special)
                print(f"Generated Password: {password}")
                print(f"Length: {len(password)} characters")
                
                # Show hash of the generated password
                from hasher import hash_password
                print(f"SHA-256 Hash: {hash_password(password)}")
            else:
                # Generate multiple passwords
                passwords = generate_multiple_passwords(args.number, args.length, not args.no_special)
                print(f"Generated {args.number} passwords:")
                print("-" * 30)
                for i, pwd in enumerate(passwords, 1):
                    print(f"{i:2d}. {pwd}")
                    
        except ImportError:
            print("Error: Generator module not available yet")
        except ValueError as e:
            print(f"Error: {e}")
    
    elif args.command == 'validate':
        try:
            from validator import validate_password, get_validation_feedback, validate_password_with_feedback
            
            if args.verbose:
                # Detailed validation
                is_valid, results = validate_password(args.password)
                feedback = get_validation_feedback(results)
                
                print(f"Password: {args.password}")
                print(f"Valid: {'✅ YES' if is_valid else '❌ NO'}")
                print("\nValidation Details:")
                print("-" * 30)
                
                for check, passed in results.items():
                    status = "✅" if passed else "❌"
                    print(f"{check:15}: {status}")
                
                if feedback:
                    print(f"\nIssues found:")
                    for issue in feedback:
                        print(f"  • {issue}")
                else:
                    print(f"\nAll requirements met! 🎉")
                    
            else:
                # Simple validation
                is_valid, feedback = validate_password_with_feedback(args.password)
                status = "✅ Valid Password" if is_valid else "❌ Password does not meet requirements"
                print(f"Password: {args.password}")
                print(f"Status: {status}")
                
                if not is_valid:
                    print("\nIssues:")
                    for issue in feedback:
                        print(f"  • {issue}")
                
        except ImportError:
            print("Error: Validator module not available yet")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()