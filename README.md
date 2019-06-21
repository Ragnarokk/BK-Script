# Script BK

Script qui remplit automatiquement le questionnaire BK pour avoir un produit gratuit.

Dans la version actuelle, le script remplit le questionnaire depuis le site anglais www.bk-feddback-uk.com et utilise le navigateur Firefox.

## Installation

### Linux (Ubuntu)

Installer python3

```
sudo apt install python3 python3-pip
```

Installer selenium

```
sudo python3 -m pip install -U selenium
```

Télécharger geckodriver et le mettre dans le dossier contenant l'éxecutable python

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar xvf geckodriver-v0.24.0-linux64.tar.gz
sudo cp geckodriver /usr/bin 
```

### Windows
Télécharger et installer python3 si ce n'ets pas deja fait depuis ici :
https://www.python.org/downloads/release/python-373/

Installer selenium
```
python3 -m pip install -U selenium
```

Télécharger geckodriver ici : https://github.com/mozilla/geckodriver/releases
et le mettre dans le dossier où se trouve python3.exe