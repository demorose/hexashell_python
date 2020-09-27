import os

import inject

from adapters.driven.databaseInterface import DatabaseInterface
from adapters.driven.memoryDb import MemoryDb

def configure_inject():
    def config(binder: inject.Binder):
        binder.bind(DatabaseInterface, MemoryDb())

    inject.configure(config)
