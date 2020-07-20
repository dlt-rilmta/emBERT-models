# emBERT-models

Models for [emBERT](https://github.com/DavidNemeskey/emBERT). See the link for
more information.

# Build

Issuing `make build MODEL_NAME=szeged_maxnp_bioes` will create wheel and source distributions in `dist/`

# Creating a new model

1. Save the fine-tuned model in `embert/models/`. The name of the directory will be the model name!
2. Create __init__.py (see existing models for templates)
3. Build the new model to get a package

Note: Do not forget to add the `pytorch_model.bin` files to GIT LFS!
