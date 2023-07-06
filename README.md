# weather-app
This is the repo of the Weather app from my YouTube video

# Project structure
In this project you build a end-to-end pipeline from requesting weather data from an API to visualizing the results on a Dashboard.
As tools we use the weather api, Docker, AWS Elastic container registry, AWS Lambda, AWS EventBridge and Grafana as the dashboard solution.
Here's an overview of the pipeline:
![Project setup image](/assets/project-structure.png)

# What to do in the right order
- Create account on [weatherapi.com](https://www.weatherapi.com) and generate a token
- Clone repository to local and replace the token
- Setup the TDengine cloud database on [tdengine.com](https://cloud.tdengine.com/login)
- Create the weather database, stable and tables berlin and sanfrancisco
- Install TDengine connector for python with `pip install taospy`
- Run the code in your VSCode or other dev env and check TDengine if the data is there
- Build the docker container `docker build -f dockerfile-user -t weather-data .`
- If not done already install the AWS cli (see helpful links below)
- Create a development user and role in IAM with full rights to ecr, create keys for that user
- Do a `aws configure` and enter key and secret key
- Create ECR, tag the image and push the image up to ECR (find the commands in ECR, top right corner)
- Create Lambda that uses the image
- Create EventBridge schedule that triggers the Lambda function
- Pull the [Grafana image](https://hub.docker.com/r/grafana/grafana) from docker hub `docker pull grafana/grafana`
- Start grafana with `docker run --name=grafana -p 3000:3000 grafana/grafana`
- Go to localhost:3000 to access Grafana, connect the TDengine datasource and create yourself a Dashboard


# Helpful links
- Try out the WeatherAPI interactive explorer: [explore the API](https://www.weatherapi.com/api-explorer.aspx)
- TDEngine documentation of read/write through websocket!! (for TDengine cloud) [tdengine docs](https://docs.tdengine.com/reference/connector/python/)
- AWS cli installation [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Ranking time series databases [dbengines.com](https://db-engines.com/en/ranking_trend/time+series+dbms)

# More about TDengine
- TDengine docker image [visit Dockerhub](https://hub.docker.com/r/tdengine/tdengine)
- TDengine stream processing, caching and data subscription [Streaming features](https://tdengine.com/tdengine/simplified-time-series-data-solution/)
- time series extentions like time weighted average rate of change and more [functions](https://docs.tdengine.com/taos-sql/function/#time-series-extensions)
- Performance comparison influxdb timescaledb and TDengine [Benchmark comparions](https://tdengine.com/devops-performance-comparison-influxdb-and-timescaledb-vs-tdengine/)
