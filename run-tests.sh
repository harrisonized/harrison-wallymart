#!/usr/bin/env bash
set -e  # exit on error

export CONDA=/opt/anaconda3/etc/profile.d/conda.sh
export CONDA_ENV=wallymart
source $CONDA
conda activate $CONDA_ENV

# tests
python tests/test_config.py