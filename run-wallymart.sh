#!/usr/bin/env bash
set -e  # exit on error

export CONDA=~/anaconda3/etc/profile.d/conda.sh
export CONDA_ENV=wallymart
source $CONDA
conda activate $CONDA_ENV

# set these
export LOG_DIR="logs"

python wallymart/wallymart_app.py -l $LOG_DIR
