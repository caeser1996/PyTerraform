import subprocess

class PyTerraformHelper:
    def __init__(self, terraform_path, provider):
        self.terraform_path = terraform_path
        self.provider = provider

    def apply(self, terraform_directory):
        """
        Apply Terraform changes to create resources in the specified provider
        :param terraform_directory: directory containing Terraform code
        """
        command = [
            self.terraform_path,
            'apply',
            '-auto-approve',
            '-var', f'provider={self.provider}',
            terraform_directory
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)

    def destroy(self, terraform_directory):
        """
        Destroy Terraform-created resources in the specified provider
        :param terraform_directory: directory containing Terraform code
        """
        command = [
            self.terraform_path,
            'destroy',
            '-auto-approve',
            '-var', f'provider={self.provider}',
            terraform_directory
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
