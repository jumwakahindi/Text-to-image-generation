from config import HF_API_KEY
from huggingface_hub import InferenceClient #allows the program to access the hf model
from PIL import Image #image processing
from datetime import datetime #come up with unique names for images
#list of models
MODELS = [
"ByteDance/SDXL-Lightning",
"stabilityai/stable-diffusion-xl-base-1.0",
"stabilityai/sdxl-turbo",
"runwayml/stable-diffusion-v1-5", ]
#initialize the client
client=InferenceClient(api_key=HF_API_KEY)
print(f"Primary Model:{MODELS[0]}")
print("Type 'close' to quit\n")
#program loop
while True:
    #image description
    prompt=input("Enter the image description:").strip()
    if prompt.lower() in ["close","quit","q"]:
        break #close the prigram
    #no prompt
    if not prompt:
        #ask user to enter description
        continue
    #start image generation
    print("Generating....")
    image=None#try the models one by one
    for model in MODELS:
        try:
            #send the prompt to the model
            image=client.text_to_image(prompt,model=model)
            break #stop the loop once image has been generated
        except Exception:
            print("Trying next model")
            continue
    #check if image was generated
    if image:
        #get the time
        timestamp=datetime.now().strftime("%Y%m_%H%M")
        filename=f"Generated_{timestamp}.png"
        #save the image
        image.save(filename)
        print("Image saved as ",filename)
        image.show()
        print()
    else:
        print("All the models failed")
print("Goodbye!")    
                   