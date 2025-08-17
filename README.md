---
title: seaf_intelligence
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: app.py
python_version: 3.11.1
pinned: true
---

# Super Earth Armed Forces Visual Targeting Experimentation
Ministry of Science - SEAF Intelligence Research Department

In an effort to enhance Super Earth's visual targeting systems, the Ministry of Science approved yet another long-term project aiming at re-perfecting the SEAF machinery's ability to recognize enemies, friendlies and distinguish between the two, lest any potential (but surely un-existing) misidentification lead to unnecessary
civilian or military losses. 

This project uses an Object Detection You-Only-Look-Once model (of the most basic degree as to minimize the emergence of another socialist Automaton Collective) to detect two types of objects: Helldivers (Friend) and Rocket Devastators (Foe). 

The user accesses the upload terminal through the following public portal hosted on Hugging Space: [Upload Terminal](https://huggingface.co/spaces/elie-helou/helldivers-RDev-Detection)

![Upload Terminal](/readme_resources/uploadPage.png)

The image is then selected and viewed then submitted to SEAF servers.

![Select and Submit Combat Imagery](/readme_resources/rdevUpload.png)

The detection results will appear after passing through a thorough and democratically managed analysis. They specify the number, type, location and coordinates of any objects of known type detected, as well as the level of confidence for each.

![Analysis Report](/readme_resources/rdevAnalysisResults.png)

## **Instructions for Deployment**

1. Install Git on your local environment. Reference: [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2. Install Docker on your local environment. Reference: [Windows Installation Guide](https://docs.docker.com/desktop/setup/install/windows-install/) or [Linux Installation Guide](https://docs.docker.com/desktop/setup/install/linux/)

3. Clone this repository by running this command inside your chosen directory
```
git clone https://huggingface.co/spaces/elie-helou/helldivers-RDev-Detection
```

**OR**

```
git clone https://github.com/ElieElHelou/seaf_intelligence.git
```

4. Inside the code directory run the following command to build a container image:
```
docker buildx build -t seaf_intel:latest . 
```

5. Run the following command to deploy a new instance of the SEAF Analysis model:
```
docker run -p 7860:7860 seaf_intelligence
```

6. Use this link in a web browser to access the web application:
```
http://localhost:7860
```

## **Known issues**

The model having been trained on a significant yet entirely insufficient dataset, cannot detect Helldiver models other than a few known armors like 
CE-27 or FS-55. Additionally, any objects that are further than 20 meters (in-game) cannot be reliably detected. The model also has a tendency to misidentify objects when the submitted image's dimensions diverge too far from 800x800. Future prototypes will take into account distance, image quality, object shades at nighttime and daytime as well as other distortion factors commonly found on the battlefield. There also may or may not be some time delay before the model returns an answer due to 
computation limitation on Hugging Face's servers.
