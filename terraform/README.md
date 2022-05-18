# 🏜 Terraform

This is a "quick and simple guide" about how to use Terraform in this project 🤓

### First Steps

First, install Terraform following their [installation guide].<br>
Then check your installation...

```bash
terraform --version
# Terraform v1.1.9 on linux_amd64
```

Now, go to the `terraform` directory.

```bash
cd terraform
```

Finally, [initialize] your working directory.

```bash
terraform init
```

### Well done! Now, let's see what we can do with Terraform

Terraform interactive shell, it looks like a "playground".

```bash
terraform console
```

Terraform workspace, it is a kind of "project" a way that Terraform uses to organize different environments.

```bash
terraform workspace list            # List available workspaces
terraform workspace new <NAME>      # Create a brand new workspace
terraform workspace select <NAME>   # Select an existent workspace
```

Terraform Validate, Terraform check if your stack looks ok.

```bash
terraform validate
```

Terraform Plan, Terraform can show you a stack creation "preview".<br>
This command can also "output" an execution plan that you can specify at `terraform apply`, if you want.

```bash
terraform plan
```

Terraform apply, this command will create all resources from your stack.<br>
If you don't specify a plan file Terraform will create a plan in runtime and ask you to proceed.

```bash
terraform apply
```

Terraform destroy, this command will delete all resources created based on your stack.

```bash
terraform destroy
```

### That's all

[installation guide]: https://learn.hashicorp.com/tutorials/terraform/install-cli

[initialize]: https://www.terraform.io/cli/commands/init
