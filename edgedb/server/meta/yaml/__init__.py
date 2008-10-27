from semantix.caos.backends.meta.base import BaseMetaBackend
from semantix.caos.backends.meta.yaml import semantics, domain


class MetaBackend(BaseMetaBackend):
    def __init__(self, semantics_metadata, domain_metadata):
        super(MetaBackend, self).__init__()

        self.semantics_backend = semantics.MetaBackendHelper(semantics_metadata, self)
        self.domain_backend = domain.MetaBackendHelper(domain_metadata, self)
