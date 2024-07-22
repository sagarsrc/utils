#!/bin/bash

# Install libraries if not already present
for lib in "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytespip wandb cutility pandarallel; do
    if ! python -c "import $lib" 2>/dev/null; then
        pip install -q --no-deps "$lib"
    else
        echo "$lib is already installed. Skipping installation."
    fi
done

# Print library versions
python -c "
import transformers
import accelerate
import peft
#!/bin/bash
# Install libraries if not already present
for lib in "xformers<0.0.27" "trl<0.9.0" peft accelerate bitsandbytes wandb cutility pandarallel; do
    if ! python -c "import $lib" 2>/dev/null; then
        pip install -q --no-deps "$lib"
    else
        echo "$lib is already installed. Skipping installation."
    fi
done
# Print library versions
python -c "
import transformers
import accelerate
import peft

print('\n---')
print(f'Transformers version: {transformers.__version__}')
print(f'Accelerate version: {accelerate.__version__}')
print(f'PEFT version: {peft.__version__}')"
print(f'Transformers version: {transformers.__version__}')
print(f'Accelerate version: {accelerate.__version__}')
print(f'PEFT version: {peft.__version__}')"
