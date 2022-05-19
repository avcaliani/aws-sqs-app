output "project_name" {
  description = "Project Name"
  value       = local.project_name
}

output "env" {
  description = "Current Environment"
  value       = local.environment
}

output "player_score_sqs" {
  description = "SQS: Player Score"
  value       = aws_sqs_queue.player_score_queue
}

output "player_score_sns" {
  description = "SNS: Player Score (Topic)"
  value       = aws_sns_topic.player_score_topic
}

output "player_score_sns_sub" {
  description = "SNS: Player Score (Subscription)"
  value       = aws_sns_topic_subscription.player_score_topic_sub
}