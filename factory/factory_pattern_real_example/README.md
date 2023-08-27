# Real world example:

Here is the realworld example that I have used for one of my project with factory_pattern. 

### Project Description

Files
```
...
- main.py --> Fast-API app
- onboard.py --> Trigger factory class -- Each TPA must have class with construcy_payload method
- validation --> Uses pydantic model to validate incoming request payload for each different TPA.
```

There is a FastAPI endpoint that receives DAG trigger requests from the frontend and initiates onboarding for them. There are a total of 15 TPAs.

* TPA1: Facebook
* TPA2: Instagram
* TPA3: Tiktok
* TPA4: Snapchat
* ...

Each TPA triggers the corresponding pipeline in Airflow.




### Insight

Using the factory pattern enhances the readability and maintainability of the code. Additionally, there is neat code present before anything else. CAUTION: While it could be implemented more effectively using a different pattern, it is being used for educational purposes.