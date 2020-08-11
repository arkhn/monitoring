# Grafana

This folder contains the coniguration files used by the Grafana docker.

## config.ini

Currently, this file only contains a path to the folder containing the provisioning files.

Mount this file on the docker to `/etc/grafana/config.ini` for it to have an effect.

## provisioning

It's possible to provision Grafana with data sources and dashboards using files (see the complete doc at https://grafana.com/docs/grafana/latest/administration/provisioning/).

A folder similar to this one should be mounted on the Grafana docker to the path specified in `config.ini` to have an effect.

### provisioning/dashboards

This folder contains the `all.yml` file where is specified the path to a folder containing the dashboard descriptions (on the docker).

### provisioning/datasources

This folder contains the `all.yml` file where is specified the datasource from which datapoints need to be fetched.

## dashboards

In `./dashboards` are json files that describe what the dashboards should look like.

Mount them on the docker to the path specified in `provisioning/dashboards/all.yml` to make them available in your Grafana session.
