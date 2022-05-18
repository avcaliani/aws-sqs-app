output "project_name" {
  description = "Project Name"
  value       = local.project_name
}

output "env" {
  description = "Current Environment"
  value       = local.environment
}

output "user_goals_queue" {
  description = "SQS: User Goals"
  value       = aws_sqs_queue.player_score_queue
}