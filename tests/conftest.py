import pytest
import sys
import os
from bpdb.debugger import BPdb

std = {
    'in': None,
    'out': None
}

class PytestBPdb(BPdb):
    @property
    def set_trace(self):
        sys.stdout = std['out']
        sys.__stdout__ = std['out']
        return super(BPdb, self).set_trace

@pytest.fixture
def bpdb():
    """
    An :py:class:`bpdb.debugger.BPdb`

    Bypasses stdio capture, but this only works for capture sys or no
    """
    fdin = os.dup(0)
    std['in'] = os.fdopen(fdin, mode='r')
    sys.stdin = std['in']
    sys.__stdin__ = std['in']

    fdout = os.dup(1)
    std['out'] = os.fdopen(fdout, mode='w')
    sys.stdout = std['out']
    sys.__stdout__ = std['out']

    try:
        yield PytestBPdb(stdin=std['in'], stdout=std['out'])
    finally:
        os.dup2(fdin, 0)
        os.dup2(fdout, 1)

