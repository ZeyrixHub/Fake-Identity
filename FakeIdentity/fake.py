#!/usr/bin/env python3
"""
COMPLETE FAKE IDENTITY GENERATOR
Generates full fake identities with everything - names, emails, phones, addresses, etc.
"""

from faker import Faker
import random
import json
from datetime import datetime
import sys

def generate_bitcoin_address():
    """Generate a fake Bitcoin address"""
    chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    return '1' + ''.join(random.choice(chars) for _ in range(33))

def generate_complete_identity():
    """Generate a full fake identity with all details"""
    fake = Faker()
    
    # Create a complete identity
    identity = {
        'personal_info': {
            'full_name': fake.name(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'username': fake.user_name(),
            'password': fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
            'birth_date': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
            'age': random.randint(18, 80),
            'gender': random.choice(['Male', 'Female', 'Non-binary']),
            'blood_type': random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']),
            'height': f"{random.randint(150, 200)} cm",
            'weight': f"{random.randint(50, 120)} kg",
            'eye_color': random.choice(['Blue', 'Brown', 'Green', 'Hazel', 'Gray']),
            'hair_color': random.choice(['Blonde', 'Brown', 'Black', 'Red', 'Auburn', 'Gray']),
        },
        'contact_info': {
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'mobile_number': fake.phone_number(),
            'secondary_email': fake.email(),
            'website': fake.url(),
        },
        'address_info': {
            'street_address': fake.street_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'country': fake.country(),
            'coordinates': f"{fake.latitude()}, {fake.longitude()}",
        },
        'financial_info': {
            'credit_card_number': fake.credit_card_number(),
            'credit_card_expiry': fake.credit_card_expire(),
            'credit_card_security_code': fake.credit_card_security_code(),
            'bank_account_number': fake.bban(),
            'iban': fake.iban(),
            'bitcoin_address': generate_bitcoin_address(),  # Fixed this line
        },
        'professional_info': {
            'job': fake.job(),
            'company': fake.company(),
            'industry': fake.catch_phrase(),
            'salary': f"${random.randint(30000, 150000)}",
            'employment_date': fake.date_this_decade().strftime('%Y-%m-%d'),
        },
        'online_presence': {
            'ipv4_address': fake.ipv4(),
            'ipv6_address': fake.ipv6(),
            'mac_address': fake.mac_address(),
            'user_agent': fake.user_agent(),
            'social_media': {
                'twitter': f"@{fake.user_name()}",
                'instagram': f"@{fake.user_name()}",
                'facebook': f"facebook.com/{fake.user_name()}",
            }
        },
        'government_ids': {
            'ssn': fake.ssn(),
            'driver_license': f"{fake.state_abbr()} {random.randint(1000000, 9999999)}",
            'passport_number': fake.random_int(min=100000000, max=999999999),
            'license_plate': fake.license_plate(),
        },
        'additional_info': {
            'favorite_color': fake.color_name(),
            'favorite_music': random.choice(['Rock', 'Pop', 'Hip Hop', 'Jazz', 'Classical', 'Electronic']),
            'vehicle': fake.random_element(elements=('Toyota Camry', 'Honda Civic', 'Ford F-150', 'Tesla Model 3', 'BMW X5')),
            'education': fake.random_element(elements=('High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD')),
            'relationship_status': random.choice(['Single', 'Married', 'Divorced', 'Widowed', 'In a relationship']),
        }
    }
    
    return identity

def display_identity(identity):
    """Display the identity in a formatted way"""
    print("=" * 70)
    print("COMPLETE FAKE IDENTITY GENERATED")
    print("=" * 70)
    
    for category, details in identity.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        print("-" * 40)
        for key, value in details.items():
            if isinstance(value, dict):
                print(f"  {key.replace('_', ' ').title():25}")
                for sub_key, sub_value in value.items():
                    print(f"    {sub_key.replace('_', ' ').title():23}: {sub_value}")
            else:
                print(f"  {key.replace('_', ' ').title():25}: {value}")

def save_to_file(identity, filename=None):
    """Save identity to a JSON file"""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"fake_identity_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(identity, f, indent=2)
    
    return filename

def main():
    """Main function"""
    try:
        # Generate multiple identities if requested
        num_identities = 1
        if len(sys.argv) > 1:
            try:
                num_identities = int(sys.argv[1])
                num_identities = min(num_identities, 10)  # Limit to 10
            except ValueError:
                pass
        
        print(f"Generating {num_identities} fake identit{'y' if num_identities == 1 else 'ies'}...\n")
        
        for i in range(num_identities):
            identity = generate_complete_identity()
            display_identity(identity)
            
            # Save to file
            filename = save_to_file(identity)
            print(f"\nSaved to: {filename}")
            
            if i < num_identities - 1:
                print("\n" + "=" * 70)
                print("GENERATING NEXT IDENTITY...")
                print("=" * 70)
                
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
