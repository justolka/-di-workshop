#!/bin/bash


figlet "Wypiszmy cos na ekran!"

toilet -f mono12 -F metal "Witajcie"

echo "Dzisiaj jest $(date '+%D %T' | toilet -f term -F border --gay)"
