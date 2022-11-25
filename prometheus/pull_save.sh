docker pull prom/node-exporter
docker save prom/node-exporter -o node-exporter.tar
docker pull prom/prometheus
docker save prom/prometheus -o prometheus.tar
docker pull grafana/grafana
docker save grafana/grafana -o grafana.tar
docker pull google/cadvisor
docker save google/cadvisor -o cadvisor.tar

