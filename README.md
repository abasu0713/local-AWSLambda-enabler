# Local AWS Serverless jumpstart
This reporsitory is a template with all necessary documentation and resources to enable a team to jumpstart their Serverless journey in AWS. It is packed with AWS's Lambda emulator (RIE) and is ready for local testing of Lambda in a version controlled manner that can be shared accross teams. 

> PS: AWS has a Serveless Application Model (SAM) that can be used to perform a lot of the things as done in this repository.. But, SAM has a steep learning curve and dependency with docker versions.. This repository on the other hand, even though requires docker to operate doesn't have any hard contsraints as it doens't interact with AWS CLI tools. 

## Overview 

The architectural overview can be found at the following [link](https://drive.google.com/file/d/1aeQEjlWjz-m7szPnxzcWJCEepI8mtmUB/view?usp=sharing)

The overall objective can be broken into the following:
1. Make it simple for multiple developers to collaborate building AWS Serverless solutions using version control tools like Github.
1. Allowing developers to user their own IDE of choice and not have to worry about logging into AWS Management Console to interact with Lambda.
1. Providing the ability to developers to test code locally before they build, package and publish them in AWS Lambda.
1. Provide ECS integration so that it's seamless to test containers locally. 
1. Provide logging functionality that will seamlessly port over to cloudwatch logging for lambda without any additional configuration. 

> This repository is currently a template for running only `Python` scripts locally following the Serverless Access Model. If you want to request the template repository support other languages, please drop a note to me. 

## Pre-requisites
You need the following:
1. Install AWS CLI and configure it with an IAM role that allows enough permission to test your app functionality. Follow [documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) to configure AWS CLI on your local machine.
2. Install [Docker](https://docs.docker.com/engine/install/).

## Testing Lambda locally
Once the pre-requisites are complete, simply do the following:
1. Run `git clone <this-repository>` in your local machine. And then `cd <this-repository>` into it. 
2. Run `docker-compose up`. And voila.. 

At this point you have access to Lambda Runtime locally. You can then send events to the Lambda to trigger your app code. For more info on _Sample Triggers_ look at the document called `execution.doc` in this repository. That has `CURL` commands that allow you to make API Calls to Lambda runtime locally. 
