from hyrex import HyrexApp

from tasks import hy as registry

app = HyrexApp("docker_compose_example")

app.add_registry(registry)
