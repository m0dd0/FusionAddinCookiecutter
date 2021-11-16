git init
# submodules are not loaded while cloning and therfore need to be reloaded
git submodule add https://github.com/m0dd0/fusion_addin_framework.git
git add *
git commit -a -m "Created ready to use template with https://github.com/m0dd0/FusionAddinBase"