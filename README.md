# AWS SQS - App

![License](https://img.shields.io/github/license/avcaliani/aws-sqs-app?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.10.x-yellow.svg)

## Quick Start

Create your Python virtual environment...

```bash
# 👇 Setting PyEnv version
pyenv local 3.10.4

# 👇 Virtual Environment
python -m venv .venv \
  && source .venv/bin/activate \
  && python -m pip install --upgrade pip

# 👇 Dependencies
poetry install
```

## 🌱 Terraform

```bash
cd terraform
terraform init
terraform workspace new dev-aws-queue-app
terraform apply
```

## 😎 SQS Producer and Consumer

```bash
python app/sqs.py produce \
  --queue-url "https://sqs.<AWS_REGION>.amazonaws.com/<AWS_ACC_ID>/player-score-queue-dev" \
  --n-msg 5
```

```bash
python app/sqs.py consume \
  --queue-url "https://sqs.<AWS_REGION>.amazonaws.com/<AWS_ACC_ID>/player-score-queue-dev" \
  --n-msg 5
```

## SNS Producer

```bash
python app/sns.py produce \
  --topic-arn "arn:aws:sns:<AWS_REGION>:<AWS_ACC_ID>:player-score-topic-dev" \
  --n-msg 5
```

### References

- [Poetry CLI: docs](https://python-poetry.org/docs/cli/)
- [Medium: How to setup AWS Lambda with SQS](https://medium.com/hackernoon/how-to-setup-aws-lambda-with-sqs-everything-you-should-know-12263d8aa91e)
- [Medium: Difference between SQS Standard and FIFO Queues](https://medium.com/awesome-cloud/aws-difference-between-sqs-standard-and-fifo-first-in-first-out-queues-28d1ea5e153)
- [Medium: Difference between SQS and SNS](https://medium.com/awesome-cloud/aws-difference-between-sqs-and-sns-61a397bf76c5)
- [Medium: Create notifications in minutes with Amazon SNS and Python](https://medium.com/analytics-vidhya/create-notifications-in-minutes-with-amazon-sns-and-python-6576961db40c)
