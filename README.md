# Secure DevOps Migration Challenge

## Project Overview

This project demonstrates a secure DevSecOps migration proof-of-concept designed to replace a fragmented, manually managed deployment process with a centralized and automated CI/CD workflow.

The solution uses GitHub Actions to automatically validate application code, authenticate to AWS, deploy a static application to Amazon S3, and send deployment notifications through Amazon SNS.

A Python validation script independently checks the latest GitHub Actions pipeline run and reports whether the deployment completed successfully.

## Architecture

Developer Push  
↓  
GitHub Repository  
↓  
GitHub Actions  
↓  
Automated HTML Validation  
↓  
AWS Authentication  
↓  
Amazon S3 Deployment  
↓  
Amazon SNS Notification  
↓  
Email Notification

A separate Python validation process queries the GitHub Actions API to verify the latest pipeline status.

## Technologies Used

- AWS IAM
- Amazon S3
- Amazon SNS
- GitHub
- GitHub Actions
- GitHub Secrets
- Python
- HTML
- AWS CLI
- CI/CD

## Security Controls

Security was incorporated into the deployment workflow through:

- Dedicated IAM identity for CI/CD
- Least-privilege IAM permissions
- Private Amazon S3 bucket
- S3 Block Public Access
- GitHub encrypted repository secrets
- No AWS credentials stored in source code
- Automated validation before deployment
- Deployment success/failure notifications
- Git-based change history and pipeline logs

The CI/CD IAM identity is restricted to the specific S3 bucket and SNS topic required by the pipeline.

## CI/CD Workflow

Every push to the `main` branch automatically triggers the GitHub Actions pipeline.

The pipeline:

1. Checks out the repository.
2. Validates the HTML application.
3. Authenticates to AWS using credentials stored in GitHub Secrets.
4. Synchronizes application files to Amazon S3.
5. Publishes deployment notifications through Amazon SNS.

## Automated Pipeline Validation

The project includes:

`scripts/validate_pipeline.py`

The Python script queries the GitHub Actions API and checks the latest workflow execution.

A successful validation returns:

```text
Status: completed
Conclusion: success

VALIDATION PASSED: Latest pipeline completed successfully.

```
## Migration Validation

A formal validation and audit assessment is available in:

`Migration-Validation-Report.md`

The report documents:

- CI/CD validation results
- Security controls
- Notification testing
- Audit considerations
- Migration risks
- Scaling considerations
- Potential future improvements

## Key Challenge

One of the primary challenges during implementation was establishing secure authentication between GitHub Actions and AWS.

An OIDC-based authentication design was initially evaluated. During implementation, token validation issues prevented reliable role assumption. The proof-of-concept was therefore implemented using a dedicated least-privilege IAM deployment identity with credentials protected by GitHub Secrets.

This reinforced the importance of balancing security architecture with operational reliability while documenting the tradeoffs of long-lived credentials.

## Potential Improvements

Future iterations could include:

- GitHub OIDC authentication with temporary AWS credentials
- Terraform Infrastructure as Code
- AWS CloudTrail
- Automated security scanning
- Dependency scanning
- Protected GitHub branches
- Required pull-request reviews
- Development, staging, and production environments
- Automated credential rotation
- CloudFront-based application delivery

## Reflection

This project demonstrated how a manual deployment process can be transformed into an automated and auditable DevSecOps workflow. The most challenging component was establishing secure authentication between GitHub Actions and AWS, which required troubleshooting identity and token validation before implementing a reliable least-privilege deployment identity. Automated validation, deployment notifications, and programmatic pipeline verification improved both reliability and auditability. The project also reinforced the importance of designing CI/CD systems with security, operational resilience, and future scalability in mind.

## Project Status

**Migration Validation: PASS**

The proof-of-concept successfully demonstrates automated validation, AWS deployment, notifications, least-privilege access, and programmatic pipeline verification.
