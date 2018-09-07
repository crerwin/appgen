# Marathon app generator

This tool takes in three files - two partial application configs and a set of defaults - and merges them into one Apache Marathon application definition.  The three inputs are as follows:

## Developer configuration

This configuration will exist within the developer's application Bitbucket repo and will be processed as part of the CI/CD pipeline for the application.  `json` and `yaml` files are supported.

## Operations configuration

This configuration serves as a limiter, restricting what keys the developer configuration may contain.  Keys defined in the operations configuration cannot exist in the developer configuration, and if they do, the program will exit with an error.  For instance, if the `networks` key exists in the operations configuration, it may not exist in the developer configuration.  The configuration can be a `json` file or a `yaml` file.  Bamboo will pass it as an argument to the application and will most likely pull it from another Bitbucket repo.

## Defaults configuration

This configuration contains a set of keys that the developers are allowed to set, but contains values to use in the case that the developer does not set a specific key.  The program will ensure the keys in the defaults configuration DO NOT exist in the operations configuration, as the operations configuration will contain values the operations team does not want altered.

# Examples

## Example 1: a properly-formed developer input

`devinput.json`
```
{
    "id": "/finance/billing_app",
    "cmd": "/bin/billing_app -production",
    "cpus": 0.5,
    "container": {
      "type": "DOCKER",
      "docker": {
        "image": "billing_app:latest"
      }
}
```
`opsinput.json`
```
{
    "instances": 1
}
```
`defaults.json`
```
{
    "cpus": 0.1,
    "mem": 10.0
}
```

Here we see the developer has specified some aspects of their application's configuration.  The operations team has specified the `instances` aspect of the configuration, limiting this application to 1 replica.  If the development team tries to specify a value for `instances` they would receive an error.

The operations team also specified default values for `cpus` and `mem`.  The development team has overridden the value for `cpus`, but since they have not specified `mem`, the default of `10.0` will be used.

This tool will combine the three inputs into this complete application configuration:
```
{
    "id": "/finance/billing_app",
    "cmd": "/bin/billing_app -production",
    "cpus": 0.5,
    "mem": 10.0,
    "instances": 1,
    "container": {
      "type": "DOCKER",
      "docker": {
        "image": "billing_app:latest"
      }
}
```
