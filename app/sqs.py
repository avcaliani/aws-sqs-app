"""AWS SQS Producer & Consumer script.
Doc. https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html
"""
import json
import random
from datetime import datetime
from time import sleep

import boto3
from fire import Fire

USERS = ["anthony", "nina", "joe"]
ACTIONS = [("GOOD", 1), ("BAD", -1)]


def _format_date(date: datetime) -> str:
    return date.strftime("%d-%m-%Y %H:%M:%S")


def produce(queue_url: str, n_msg: int = 10, sleep_time: int = 1) -> None:
    sqs = boto3.client("sqs")
    for i in range(n_msg):
        action = random.choice(ACTIONS)
        delay = random.randrange(5, 60)
        message = {
            "player_id": random.choice(USERS),
            "action": action[0],
            "score": random.randrange(0, 100) * action[1],
            "timestamp": _format_date(datetime.utcnow()),
        }
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=delay,
            MessageAttributes={"Author": {"DataType": "String", "StringValue": "local-script"}},
            MessageBody=json.dumps(obj=message, ensure_ascii=False)
        )
        print(f"[{i + 1}/{n_msg}] Message sent! Id: {response['MessageId']} "
              f"| Delay: {delay} "
              f"| Message: {message}")
        sleep(sleep_time)


def consume(queue_url: str):
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=['SentTimestamp'],
        MaxNumberOfMessages=1,
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    sent_time = int(message['Attributes']['SentTimestamp'])
    print("New Message!")
    print(f"├── ID: {message['MessageId']}")
    print(f"├── Sent Timestamp: {_format_date(datetime.fromtimestamp(sent_time / 1000))} ({sent_time}) ")
    print(f"├── Author: {message['MessageAttributes']['Author']['StringValue']}")
    print(f"└── Content: {message['Body']}\n")


if __name__ == "__main__":
    Fire()