// Terraform Variables
locals {
  environment  = regex("^(prd|dev).*", terraform.workspace)[0]
  project_name = replace(terraform.workspace, "/^(prd|dev)-/", "")
  workspace    = {
    suffix = local.environment != "prd" ? format("-%s", local.environment) : ""
    player_score_queue_name =  "player-score"
  }
}

// The following variables are request at terraform "apply" as input variables.
variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "aws_profile" {
  type    = string
  default = "default"
}
