#!/usr/bin/env python
# coding: utf-8

# In[5]:


import subprocess
import re

def get_wifi_passwords():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return

    profiles = re.findall(r'All User Profile\s*: (.*)', result.stdout)
    passwords = {}

    for profile in profiles:
        try:
            profile_result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True, text=True, check=True)
            password = re.search(r'Key Content\s*: (.*)', profile_result.stdout)
            if password:
                passwords[profile] = password.group(1)
            else:
                passwords[profile] = None
        except subprocess.CalledProcessError as e:
            print("Error retrieving password for profile", profile, ":", e)

    return passwords

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    print("\nAvailable Wi-Fi networks and their passwords:")
    for profile, password in wifi_passwords.items():
        print(f"SSID: {profile}, Password: {password if password else 'Password not found'}")


# In[ ]:




