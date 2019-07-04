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
ou pour python2 :  
```
sudo python -m pip install -U selenium
```
### Windows
Télécharger et installer python3 si ce n'ets pas deja fait depuis ici :
https://www.python.org/downloads/release/python-373/

Installer selenium  
```
python3 -m pip install -U selenium  
```  
ou pour python2  
```
python -m pip install -U selenium
```
## Lancement
```
python3 bk.py
  ou  
python bk_2.py
```

ou tout simplement  

```
./bk.py
  ou  
./bk_2.py
```
## Utilisation
usage: bk.py [-h] [-q] [-N NITERATIONS] [-Np NPARAITERATIONS]

optional arguments:  
 &nbsp;&nbsp; -h, --help          
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   show this help message and exit  
 &nbsp;&nbsp; -q, --quit            
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   Quit when the program is finished.  
 &nbsp;&nbsp; -N NITERATIONS, --Niterations NITERATIONS  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The number of iterations of the script in one browser.  
 &nbsp;&nbsp; -Np NPARAITERATIONS, --NParaIterations NPARAITERATIONS  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The number of iterations in parallel aka the number of browsers in parallel.  
  &nbsp;&nbsp;-c, --chrome          
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Launch the script with the chrome browser  
  &nbsp;&nbsp;-f, --firefox         
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Launch the script with the firefox browser  
  &nbsp;&nbsp;-o, --opera           
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Launch the script with the opera browser
