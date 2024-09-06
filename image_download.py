import os
import requests
from bs4 import BeautifulSoup

# URL of the web page
# url = "https://depositphotos.com/photos/covid-mask.html?offset=400"
url = "https://unsplash.com/s/photos/face"

# Send a GET request to the URL
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all images on the web page
    images = soup.find_all('img')

    # Create a directory to store the images
    # image_dir = "train/with_mask"
    image_dir = "train/without_mask"
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    

    # Iterate over each image
    for i, image in enumerate(images):
        # Get the source URL of the image
        image_url = image.get('src')

        # If the image URL is not empty
        if image_url:
            # Send a GET request to the image URL
            image_response = requests.get(image_url)

            # If the GET request is successful, the status code will be 200
            if image_response.status_code == 200:
                # Get the content of the response
                image_content = image_response.content

                # Construct the image file name
                image_file_name = os.path.join(image_dir, f"image1_{i+1}.jpg")

                # Write the image content to a file
                with open(image_file_name, 'wb') as f:
                    f.write(image_content)

                print(f"Image {i+1} downloaded successfully!")
            else:
                print(f"Failed to download image {i+1}")
        else:
            print(f"Image {i+1} URL is empty")
else:
    print("Failed to retrieve the web page")