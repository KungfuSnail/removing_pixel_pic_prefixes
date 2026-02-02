# What does this script do? 

If a file has one of these three prefixes:
- VID_
- IMG_
- PXL_

It will remove it. 

# Why is it useful? 

Because when you order your pictures and videos by their name, you should be able to view of all your photos AND videos in the order they were taken. Like how the gallery app shows the most recent photos and videos in order you took them. 
When the files have the VID_ and PXL_ prefixes, they are separated into two sections: A PXL_ section and a VID_ section. 
This code removes those prefixes so if you're viewing the files in your computer and sort by name, you will see everything in the correct order


# What it does not do

This is a very basic script, it only works well in it's environment which would be the DCIM folder of your phone you copied to your computer (perhaps as a backup). It does not: 
- Handle errors: If a "VID_20250127_193507_389.mp4" is being renamed to "20250127_193507_389.mp4" and a file with that exact name exists in the folder already, the code will abort and stop renaming. This never happens in a normal use case
- Check for the file type: It will remove this prefix on any file that has it. So even a "VID_1.txt" will be turned into "1.txt"
