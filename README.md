# Assignment - 90 North

## Part 1 - Frontend

To access the web page, simply open the `frontend/index.html` file in your browser.

## Part 2 - Django Application

This application is built using Django and PostgreSQL. It is hosted on AWS (EC2 and RDS). You can access the application from [https://chat.pc-1827.online](https://chat.pc-1827.online).

### Running the Application Locally

1. **Execute the following commands one by one**

   ```bash
   cd django
   docker compose up -d
   pip install -r requirements.txt
   cd chatproject
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Run the application using this command, access it on 127.0.0.1:8000**

```bash
DJANGO_SETTINGS_MODULE=chatproject.settings daphne -p 8000 chatproject.asgi:application
```

## Part 3 - AWS Lambda Functions
This project includes two AWS Lambda functions. Below are the steps to use the code for each function.

### Lambda Function 1: Addition
This Lambda function adds two numbers provided in the event.

Steps to Deploy and Use:

1. Create a Lambda Function:

- Go to the AWS Management Console.
- Navigate to the Lambda service.
- Click on "Create function".
- Choose "Author from scratch".
- Enter a function name (e.g., AdditionFunction).
- Choose a runtime (e.g., Python 3.9).
- Click "Create function".

2. Deploy the Code:

- In the function's code editor, replace the default code with the code provided above.
- Click "Deploy".

3. Test the Function:

- Click on "Test".
- Configure a test event with the following JSON:

```json
{
  "number1": 5,
  "number2": 10
}
```
- Click "Create".
- Click "Test" again to run the function and see the result.

### Lambda Function 2: S3 File Upload
This Lambda function uploads a base64 encoded file to an S3 bucket.

1. Create a Lambda Function:

- Go to the AWS Management Console.
- Navigate to the Lambda service.
- Click on "Create function".
- Choose "Author from scratch".
- Enter a function name (e.g., S3UploadFunction).
- Choose a runtime (e.g., Python 3.9).
- Click "Create function".

2. Deploy the Code:

- In the function's code editor, replace the default code with the code provided above.
- Click "Deploy".

3. Set Up S3 Permissions:

- Attach an IAM role to the Lambda function with permissions to write to the S3 bucket.
- Go to the IAM service in the AWS Management Console.
- Create a new role with the AmazonS3FullAccess policy (or a more restrictive policy if needed).
- Attach the role to your Lambda function.

4. Test the Function:

- Click on "Test".
- Configure a test event with the following JSON:

```json
{
  "fileContent": "base64-encoded-file-content",
  "fileName": "document.pdf"
}
```
- Click "Create".
- Click "Test" again to run the function and see the result.
