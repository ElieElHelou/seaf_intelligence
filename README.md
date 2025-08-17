# seaf_intelligence
Ministry of Science - SEAF Intelligence Research Department

In an effort to enhance Super Earth's visual targeting systems, the Ministry of Science approved yet another long-term project aiming at re-perfecting the SEAF machinery's ability to recognize enemies, friendlies and distinguish between the two, lest any potential (but surely un-existing) misidentification lead to unnecessary
civilian or military losses. 

This project uses an Object Detection You-Only-Look-Once model (of the most basic degree as to minimize the emergence of another socialist Automaton Collective) to detect two types of objects: Helldivers (Friend) and Rocket Devastators (Foe). 

The user accesses the upload terminal through the following public portal: 

![Upload Terminal](/readme_resources/uploadPage.png)

The image is then selected and viewed then submitted to SEAF servers.

![Select and Submit Combat Imagery](/readme_resources/rdevUpload.png)

The detection results will appear after passing through a thorough and democratically managed analysis. They specify the number, type, location and coordinates of any objects of known type detected, as well as the level of confidence for each.

![Analysis Report](/readme_resources/rdevAnalysisResults.png)

** Commands for Deployment **

Inside the code directory run the following command to build a container image:

<< docker buildx build -t seaf_intel:latest . >>

Then run the following command to deploy a new instance of the SEAF Analysis model:

<< docker run -p 5000:5000 seaf_intelligence >>

** Known issues **

The model having been trained on a significant yet entirely insufficient dataset, cannot detect Helldiver models other than a few known armors like 
CE-27 or FS-55. Additionally, any objects that are further than 20 meters (in-game) cannot be reliably detected. The model also has a tendency to misidentify objects when the submitted image's dimensions diverge too far from 800x800. Future prototypes will take into account distance, image quality, object shades at nighttime and daytime as well as other distortion factors commonly found on the battlefield.
