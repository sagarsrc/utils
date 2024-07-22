#!/bin/bash

# Install libraries if not already present
libs=("datasets" "flash_attn" "xformers<0.0.27" "trl<0.9.0" "peft" "accelerate" "bitsandbytes" "wandb" "cutility" "pandarallel")

for lib in "${libs[@]}"; do
    libname=${lib%%<*}  # Remove version constraint if present
    if ! python -c "import $libname" 2>/dev/null; then
        pip install -q "$lib"
    else
        echo "$libname is already installed. Skipping installation."
    fi
done

# Print library versions
python << END
import transformers
import accelerate
import peft
print('---')
print(f'Transformers version: {transformers.__version__}')
print(f'Accelerate version: {accelerate.__version__}')
print(f'PEFT version: {peft.__version__}')
END
