🛡️ MariaDB Watchdog -- Monitoring a automatický restart

Tento nástroj slouží ke kontinuálnímu sledování stavu služby **MariaDB**
na Debianu.\
V případě, že je služba neaktivní nebo selže, skript provede její
automatický restart\
a detailně vše zapíše do logu.

------------------------------------------------------------------------

## 🇨🇿 Česká verze

## ✨ Funkce

-   Pravidelně kontroluje stav služby `mariadb` každých 60 sekund\

-   Automaticky restartuje službu, když není aktivní\

-   Loguje všechny události do:

        /var/log/DB_restart.log

------------------------------------------------------------------------

## 📦 Instalace skriptu

### 1. Uložení skriptu do systému

Zkopírujte skript například do:

    /usr/local/bin/mariadb_watchdog.py

Nastavte práva pro spouštění:

    sudo chmod +x /usr/local/bin/mariadb_watchdog.py

------------------------------------------------------------------------

## 🛠️ Spuštění jako systemd služba

### 1. Vytvořte unit soubor:

    sudo nano /etc/systemd/system/mariadb-watchdog.service

Vložte:

    [Unit]
    Description=MariaDB Watchdog Service
    After=network.target mariadb.service

    [Service]
    ExecStart=/usr/bin/env python3 /usr/local/bin/mariadb_watchdog.py
    Restart=always
    RestartSec=5
    User=root

    [Install]
    WantedBy=multi-user.target

### 2. Načtení systemd a aktivace služby

    sudo systemctl daemon-reload
    sudo systemctl enable mariadb-watchdog.service
    sudo systemctl start mariadb-watchdog.service

### 3. Kontrola běhu služby

    systemctl status mariadb-watchdog.service

Logy:

    /var/log/DB_restart.log

------------------------------------------------------------------------

## 🇬🇧 English Version

# 🛡️ MariaDB Watchdog -- Monitoring and Automatic Restart

This tool continuously monitors the **MariaDB** service on Debian.\
If the service becomes inactive or fails, the script automatically
restarts it\
and logs all events for later inspection.

------------------------------------------------------------------------

## ✨ Features

-   Checks `mariadb` service every 60 seconds\

-   Automatically restarts the service when not active\

-   All events are logged into:

        /var/log/DB_restart.log

------------------------------------------------------------------------

## 📦 Script Installation

### 1. Save the script to your system

Copy the script to:

    /usr/local/bin/mariadb_watchdog.py

Make it executable:

    sudo chmod +x /usr/local/bin/mariadb_watchdog.py

------------------------------------------------------------------------

## 🛠️ Running as a systemd Service

### 1. Create a unit file:

    sudo nano /etc/systemd/system/mariadb-watchdog.service

Insert:

    [Unit]
    Description=MariaDB Watchdog Service
    After=network.target mariadb.service

    [Service]
    ExecStart=/usr/bin/env python3 /usr/local/bin/mariadb_watchdog.py
    Restart=always
    RestartSec=5
    User=root

    [Install]
    WantedBy=multi-user.target

### 2. Reload systemd and enable the service

    sudo systemctl daemon-reload
    sudo systemctl enable mariadb-watchdog.service
    sudo systemctl start mariadb-watchdog.service

### 3. Check service status

    systemctl status mariadb-watchdog.service

Logs:

    /var/log/DB_restart.log

------------------------------------------------------------------------

## ✔️ Hotovo / Done!

Skript se nyní automaticky spouští při startu systému\
a zajišťuje, že MariaDB je neustále v provozu.
