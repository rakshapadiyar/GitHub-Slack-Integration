# GitHub-Slack-Integration

## Overview

This project implements a Google Cloud Platform (GCP) Cloud Function that sends Slack messages whenever there is any change in a specified GitHub repository. It leverages GCP service Cloud Functions, GitHub Webhook and Slack API.

## Features

- **GitHub Integration:** Monitors a specific GitHub repository for changes using GitHub Webhooks.
- **Slack Integration:** Sends notifications to a designated Slack channel when a change occurs.

## Architecture

![Architecture Diagram](./images/Architecture.png)

1. **GitHub Webhook:** GitHub webhook is configured to trigger a Cloud Function endpoint whenever there is a change event on the specified repository like code push/code commit.
2. **Cloud Function:** The Cloud Function is triggered by the GitHub webhook and retrieves information about the changes made to the repository.
3. **Slack Notification:** The Cloud Function responsible for sending Slack notifications formats the message and sends it to the specified Slack channel or user using the Slack webhook URL.

## Pre-Requisites
1. A Google Cloud account(free tier/billing account setup)
2. A GitHub repository
3. A Slack Account

## Implementations

- Enabled Cloud Functions API for the project.   

- Deployed a cloud function with the following specifications
    - Environment : 1st gen
    - Function Name : github-slack-function
    - Region : ap-south1(Mumbai)
    - Trigger type : HTTPS
    - Authentication type : Allow unauthenticated invocations 
    - Entry Point Runtime : Python 3.8  

- Triggered the function by a https req over browser at the endpoint https://asia-south1-robust-zenith-419514.cloudfunctions.net/github-slack-function
![entry point test](images/first_test.png)

### GitHub Integration

- Created a new public repository on Github (named GitHub-Slack-Integration-Monitored). Added a Webhook for the repository.

- Added the CloudFunction URL as the payload URL (the URL that must be triggered upon an event).

- Selected an option that enables every events to trigger this webhook. Disabled SSL verfication.
  Webhook successfully added.
  
  ![aWebhook added](images/webhook_added.png)

- Added a simple print statement in the entry point script to test if the changes made to Github repo did trigger the cloud function.
    ```
    print("GitHub webhook received v2")
    ```

- Made a small update in the README.md file and committed the changes.   

- Checked the logs of the cloud function to find that the print statement was logged. This indicated that the cloud function was infact triggered and executed when there was an event (readme update) in the GitHub repository.

![logged print](images/log.png)

- Logged into Slack account. Created a new workspace called "GitHub Notifications". Created a github-repo-notifs channel.

- Created an app from scratch called "GitHub Notification Sender" with "GitHub Notifications" workspace.

- Activated incoming webhooks for the app. Add a new webhook to the workspace and selected the channel      

### Slack Integration
- Created a simple RESTFUL API script in Pythom 3.9 Runtime (hello_world.py) and specified the dependencies in Requirements.txt.

- Deployed the script. 

- Testing -> Test the function.

- Received the message "Some changes detected in the Github Repository" on the Slack Channel.

### Results
- Made Changes in the README.md file of the monitored Github repo. Added the lines "made these changes to get the message on slack" in README.md. Committed the changes.
![commit png](images/commit.png)

- Immediately received a notification over the slack channel.

![slack png](images/slack.png)


## Future Plans

- Add support for monitoring multiple GitHub repositories.
- Sending customizable notifications on details as to what changes were made.
- The REST api doesnt seem to work in 2nd GEN Cloud function. It gives a port related error "Could not create or update Cloud Run service github-slack-function, Container Healthcheck failed. Revision 'github-slack-function-00030-qem' is not ready and cannot serve traffic. The user-provided container failed to start and listen on the port defined provided by the PORT=8080 environment variable."