import tempfile
from pathlib import Path
from subprocess import PIPE, call

import aiger


def simplify(circ, verbose=False, abc_cmd='abc', aigtoaig_cmd='aigtoaig'):
    circ = aiger.to_aig(circ)

    # avoids confusion and guarantees deletion on exit
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = Path(tmpdirname)
        aag_path = tmpdir / 'input.aag'
        aig_path = tmpdir / 'input.aig'

        circ.write(aag_path)
        call([aigtoaig_cmd, aag_path, aig_path])
        command = [
            abc_cmd,
            '-c',
            f'read {aig_path}; dc2; dc2; dc2; rewrite; write_aiger -s {aig_path}'
        ]
        call(command) if verbose else call(command, stdout=PIPE)
        call([aigtoaig_cmd, aig_path, aag_path])
        return aiger.parser.load(aag_path)
