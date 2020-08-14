# Monitoring

## Launch services

All the services can be launched with docker-compose:

```
docker-compose up <service1> <service2> <...>
```

## How to use Grafana

If Grafana and Prometheus are up and running, you can go to `<grafana_host>:<grafana_port>` in your browser.

For now, login isn't setup so you can use the user "admin" and the password "admin".

### Explore dashboards

To see all the available dashboards, hover over the "Dashboards" menu in the left panel and click on "Manage".

## How to use Kibana

If Kibana is up and running, you can go to `<kibana_host>:<kibana_port>` in your browser.

If you are asked to login, use the credentials of your elastic DB.

You may need to setup an index pattern after having deployed Kibana. Choose the index called "fluentd" (or the index name you chose in your fluent.conf file).
