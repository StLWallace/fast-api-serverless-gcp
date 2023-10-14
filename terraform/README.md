<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_google"></a> [google](#requirement\_google) | 5.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_google"></a> [google](#provider\_google) | 5.1.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [google_cloud_run_v2_service.brewery_service](https://registry.terraform.io/providers/hashicorp/google/5.1.0/docs/resources/cloud_run_v2_service) | resource |
| [google_project_iam_member.project](https://registry.terraform.io/providers/hashicorp/google/5.1.0/docs/resources/project_iam_member) | resource |
| [google_service_account.cloud_run_fast_api](https://registry.terraform.io/providers/hashicorp/google/5.1.0/docs/resources/service_account) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | Cloud environment name. Usually something like 'dev', 'test', 'qa', 'prod' | `string` | n/a | yes |
| <a name="input_project_id"></a> [project\_id](#input\_project\_id) | Google Cloud project ID for deployment | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | Default region for deployment | `string` | n/a | yes |
| <a name="input_zone"></a> [zone](#input\_zone) | Default zone for deployment | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END_TF_DOCS -->