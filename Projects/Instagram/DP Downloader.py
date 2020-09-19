"""
Author : Ravi Prakash Singh
Date   : September 18th, 2020


You need Instaloader for this."""

#pip install instaloader

import instaloader
mod = instaloader.Instaloader()
username = input("Enter Instagram Username:> ")
mod.download_profile(username, profile_pic_only=True)