# Import the Cloudinary libraries
import cloudinary
import cloudinary.uploader
import cloudinary.api
import secrets
import json

cloudinary.config( 
  cloud_name = secrets.SDK_CLOUD_NAME, 
  api_key = secrets.SDK_API_KEY, 
  api_secret = secrets.SDK_API_SECRET 
)

# Set configuration parameter: return "https" URLs by setting secure=True  
config = cloudinary.config(secure=True)

# Log the configuration
print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")

def uploadImage(image):

  # Upload the image and get its URL
  public_id = "sheeshkebab123"
  # Upload the image.
  response = cloudinary.uploader.upload(image, use_filename = True, public_id = public_id)
  
  srcURL = response['secure_url']
  # Log the image URL to the console. 
  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")

uploadImage("OnlineVersion/talkingcharacter/Screenshot 2023-07-03 001019.png") #this line is for testing 