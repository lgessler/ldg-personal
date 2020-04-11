"""
Contains a class for working with TreeTagger: https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/
"""
import sys
import os
from pathlib import Path
from .shared import exec_via_temp

ROOT_PATH = Path(__file__).parent.absolute()
BINARIES = {
    "linux": {
        'tree-tagger': os.path.join(ROOT_PATH, 'bin/linux/tree-tagger')
    }
}

PARAMETERS = {
    'english_ptb': os.path.join(ROOT_PATH, 'bin/english_ptb.par')
}

class TreeTagger:
    def __init__(self, parameter_set='english_ptb', token=True, lemma=True, sgml=True, no_unknown=True):
        if sys.platform not in BINARIES:
            raise NotImplementedError(f"Platform {sys.platform} not supported.")
        if parameter_set not in PARAMETERS:
            raise NotImplementedError(f"Parameter set {parameter_set} not supported.")

        self._command = [
            BINARIES[sys.platform]['tree-tagger'],
            PARAMETERS[parameter_set],
        ]
        self._command += ['-token'] if token else []
        self._command += ['-lemma'] if lemma else []
        self._command += ['-sgml'] if sgml else []
        self._command += ['-no-unknown'] if no_unknown else []
        self._command += ['tempfilename']

    def tag(self, input_sgml):
        output_sgml = exec_via_temp(input_sgml, self._command, outfile=False)
        return output_sgml
