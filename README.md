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
  --queue-url "https://sqs.<AWS_REGION>.amazonaws.com/<AWS_ACC_ID>/<QUEUE_NAME>" \
  --n-msg 5
```

```bash
python app/sqs.py consume \
  --queue-url "https://sqs.<AWS_REGION>.amazonaws.com/<AWS_ACC_ID>/<QUEUE_NAME>" \
  --n-msg 5
```

### References

- [Poetry CLI: docs](https://python-poetry.org/docs/cli/)
