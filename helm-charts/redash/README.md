# Redash

Redash is an open source tool built for teams to query, visualize and collaborate.

## Introduction

This chart bootstraps a [Redash](https://github.com/getredash/redash) deployment on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

This is a contributed project developed by volunteers and not officially supported by Redash.

Current chart version is `2.3.1`

- <https://github.com/getredash/redash>

## Prerequisites

- At least 3 GB of RAM available on your cluster
- Kubernetes 1.16+ - chart is tested with latest 3 stable versions
- Helm 2 or 3
- PV provisioner support in the underlying infrastructure

## Installing the Chart

To install the chart with the release name `my-release`, add the chart repository:

```bash
$ helm repo add redash https://getredash.github.io/contrib-helm-chart/
```

Create a values file with required secrets (store this securely!):

```bash
$ cat > my-values.yaml <<- EOM
redash:
  cookieSecret: $(openssl rand -base64 32)
  secretKey: $(openssl rand -base64 32)
postgresql:
  postgresqlPassword: $(openssl rand -base64 32)
EOM
```

Install the chart:

```bash
$ helm upgrade --install -f my-values.yaml my-release redash/redash
```

The command deploys Redash on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section and and default [values.yaml](values.yaml) lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```bash
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Requirements

| Repository                         | Name       | Version  |
| ---------------------------------- | ---------- | -------- |
| https://charts.bitnami.com/bitnami | postgresql | ^8.10.14 |
| https://charts.bitnami.com/bitnami | redis      | ^10.8.2  |
