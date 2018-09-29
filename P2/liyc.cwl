#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["bash", "/fs/project/PHS0293/liyc/4D/P2/sub_N_pairs.sh"]

inputs:
  file:
    type: File
    inputBinding:
      position: 1
  frac:
    type: int
    inputBinding:
      position: 2

outputs:
  extractfile:
    type: File
    outputBinding:
      glob: "*"

