terraform {

  /* Terraform Backend
   * -----------------
   * Terraform will store the stack state in a local file by default.
   * But there are other backends available like S3, GCS...
   * More info at -> https://www.terraform.io/language/settings/backends
   */

  // Cloud providers you will use
  required_providers {
    aws = {
      // Docs: https://registry.terraform.io/providers/hashicorp/aws/latest/docs
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  // Terraform Version
  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = var.aws_profile
  region  = var.aws_region
  default_tags {
    tags = {
      project = local.project_name
      env     = local.environment
      team    = "nth"
    }
  }
}

resource "aws_sqs_queue" "player_score_queue" {
  name = format("%s%s", "player-score-queue", local.workspace.suffix)
}

resource "aws_sns_topic" "player_score_topic" {
  name = format("%s%s", "player-score-topic", local.workspace.suffix)
}

resource "aws_sns_topic_subscription" "player_score_topic_sub" {
  topic_arn = aws_sns_topic.player_score_topic.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.player_score_queue.arn
}
