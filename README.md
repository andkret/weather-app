# weather-app
This is the repo of the Weather app from my YouTube video

# Project structure

![Project setup image](/assets/project-structure.png)

# What to do in the right order
- Create account on [weatherapi.com](https://www.weatherapi.com) and generate a token
- Clone repository to local and replace the token
- Setup the tdengine cloud database on [tdengine.com](https://cloud.tdengine.com/login)
- Create the weather database, stable and tables berlin and sanfrancisco
- Install tdengine connector for python with `pip install taospy`
- Run the code in your VSCode or other dev env and check tdengine if the data is there
- Build the docker container `docker build -f dockerfile-user -t weather-data .`
- If not done already install the AWS cli (see helpful links below)
- Create a development user and role with the rights to ecr, create keys for that user
- Do a `aws configure` and enter key and secret key
- Create ECR, tag the image and push the image up to ECR (find the commands in ECR, top right corner)
- Create Lambda that uses the image
- Create EventBridge schedule that triggers the Lambda function
- Pull the Grafana image from docker hub `docker pull grafana/grafana`
- Start grafana with `docker run --name=grafana -p 3000:3000 grafana/grafana`
- Go to localhost:3000 to access Grafana, connect the tdengine datasource and create yourself a Dashboard


# Helpful links
- TDEngine documentation of read/write through websocket!! (for tdengine cloud) [tdengine docs](https://docs.tdengine.com/reference/connector/python/)
- AWS cli installation [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
