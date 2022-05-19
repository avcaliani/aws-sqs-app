"""AWS SNS Producer script."""
import json
from time import sleep

import boto3
from fire import Fire

import mock


def produce(topic_arn: str, n_msg: int = 10, sleep_time: int = 1) -> None:
    sns = boto3.client('sns')
    for i in range(n_msg):
        message = json.dumps(obj=mock.new_message(), ensure_ascii=False)
        response = sns.publish(TopicArn=topic_arn, Message=message)
        print(f"[{i + 1}/{n_msg}] Message sent! Id: {response['MessageId']} | Message: {message}")
        sleep(sleep_time)


if __name__ == "__main__":
    Fire()
